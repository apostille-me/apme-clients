# frozen_string_literal: true

require "json"
require "net/http"
require "uri"

class ApostilleMeClient
  def initialize(base_url:, token: nil, headers: {})
    @base_url = base_url.sub(%r{/+$}, "")
    @token = token
    @headers = headers
  end

  def request(method, path, body: nil)
    uri = URI("#{@base_url}/#{path.sub(%r{^/+}, "")}")
    request_class = Net::HTTP.const_get(method.to_s.capitalize)
    req = request_class.new(uri)
    @headers.each { |key, value| req[key] = value }
    req["Authorization"] ||= "Bearer #{@token}" if @token
    if body
      req["Content-Type"] ||= "application/json"
      req.body = JSON.generate(body)
    end

    response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: uri.scheme == "https") { |http| http.request(req) }
    raise "Apostille Me request failed: #{response.code}" unless response.is_a?(Net::HTTPSuccess)
    return nil if response.body.nil? || response.body.empty?

    JSON.parse(response.body)
  end
end
