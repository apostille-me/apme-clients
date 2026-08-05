#include "apme/client.h"

#include <assert.h>
#include <string.h>

int main(void) {
  apme_client_config_t config = apme_client_default_config();
  config.base_url = "https://api.example.test/";

  char output[128];
  assert(apme_client_build_url(&config, "/health", output, sizeof(output)) == 0);
  assert(strcmp(output, "https://api.example.test/health") == 0);

  config.base_url = "http://localhost:8787/";
  assert(apme_client_build_url(&config, "/health", output, sizeof(output)) == 0);
  assert(strcmp(output, "http://localhost:8787/health") == 0);

  config.base_url = "http://example.com";
  assert(apme_client_build_url(&config, "/health", output, sizeof(output)) == -1);
  config.base_url = "http://localhost.evil";
  assert(apme_client_build_url(&config, "/health", output, sizeof(output)) == -1);

  config.base_url = "https://api.example.test/";
  char too_small[4];
  assert(apme_client_build_url(&config, "/health", too_small, sizeof(too_small)) == -2);
  return 0;
}
