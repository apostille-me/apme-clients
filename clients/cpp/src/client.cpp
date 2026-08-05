#include "apme/client.hpp"

#include <stdexcept>
#include <string_view>
#include <utility>

namespace {

bool starts_with(std::string_view value, std::string_view prefix) {
  return value.size() >= prefix.size() && value.substr(0, prefix.size()) == prefix;
}

bool loopback_authority(std::string_view value, std::string_view prefix) {
  if (!starts_with(value, prefix)) {
    return false;
  }
  if (value.size() == prefix.size()) {
    return true;
  }
  const char next = value[prefix.size()];
  return next == ':' || next == '/';
}

bool allowed_base_url(std::string_view value) {
  return starts_with(value, "https://") ||
         loopback_authority(value, "http://localhost") ||
         loopback_authority(value, "http://127.0.0.1") ||
         loopback_authority(value, "http://[::1]");
}

}  // namespace

namespace apme {

Client::Client(ClientConfig config) : config_(std::move(config)) {
  if (config_.base_url.empty()) {
    throw std::invalid_argument("Apostille Me base URL cannot be empty");
  }
  while (config_.base_url.size() > 1 && config_.base_url.back() == '/') {
    config_.base_url.pop_back();
  }
  if (!allowed_base_url(config_.base_url)) {
    throw std::invalid_argument("Apostille Me base URL must use HTTPS or loopback HTTP");
  }
}

const ClientConfig& Client::config() const noexcept { return config_; }

std::string Client::url(std::string_view path) const {
  while (!path.empty() && path.front() == '/') {
    path.remove_prefix(1);
  }
  if (path.empty()) {
    return config_.base_url;
  }

  std::string result;
  result.reserve(config_.base_url.size() + path.size() + 1);
  result.append(config_.base_url);
  result.push_back('/');
  result.append(path.data(), path.size());
  return result;
}

}  // namespace apme
