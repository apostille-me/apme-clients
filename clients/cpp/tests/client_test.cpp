#include "apme/client.hpp"

#include <cassert>

int main() {
  apme::ClientConfig config;
  config.base_url = "https://api.example.test/";
  config.bearer_token = "test-token";

  const apme::Client client{config};
  assert(client.url("/health") == "https://api.example.test/health");
  assert(client.config().bearer_token.has_value());
  return 0;
}
