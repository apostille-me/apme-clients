#include "apme/client.hpp"

#include <cassert>
#include <stdexcept>

int main() {
  apme::ClientConfig config;
  config.base_url = "https://api.example.test/";
  config.bearer_token = "test-token";

  const apme::Client client{config};
  assert(client.url("/health") == "https://api.example.test/health");
  assert(client.config().bearer_token.has_value());

  config.base_url = "http://localhost:8787/";
  const apme::Client local_client{config};
  assert(local_client.url("/health") == "http://localhost:8787/health");

  for (const char* invalid : {"http://example.com", "http://localhost.evil"}) {
    bool rejected = false;
    try {
      config.base_url = invalid;
      const apme::Client insecure{config};
      (void)insecure;
    } catch (const std::invalid_argument&) {
      rejected = true;
    }
    assert(rejected);
  }
  return 0;
}
