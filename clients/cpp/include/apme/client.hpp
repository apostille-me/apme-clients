#pragma once

#include <optional>
#include <string>
#include <string_view>

namespace apme {

struct ClientConfig {
  std::string base_url{"https://api.apostille.me"};
  std::optional<std::string> bearer_token{};
};

class Client {
 public:
  explicit Client(ClientConfig config = {});

  [[nodiscard]] const ClientConfig& config() const noexcept;
  [[nodiscard]] std::string url(std::string_view path) const;

 private:
  ClientConfig config_;
};

}  // namespace apme
