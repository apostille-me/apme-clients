#include "apme/client.hpp"

#include <stdexcept>
#include <utility>

namespace apme {

Client::Client(ClientConfig config) : config_(std::move(config)) {
  if (config_.base_url.empty()) {
    throw std::invalid_argument("Apostille Me base URL cannot be empty");
  }
  while (config_.base_url.size() > 1 && config_.base_url.back() == '/') {
    config_.base_url.pop_back();
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
