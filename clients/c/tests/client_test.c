#include "apme/client.h"

#include <assert.h>
#include <string.h>

int main(void) {
  apme_client_config_t config = apme_client_default_config();
  config.base_url = "https://api.example.test/";

  char output[128];
  assert(apme_client_build_url(&config, "/health", output, sizeof(output)) == 0);
  assert(strcmp(output, "https://api.example.test/health") == 0);

  char too_small[4];
  assert(apme_client_build_url(&config, "/health", too_small, sizeof(too_small)) == -2);
  return 0;
}
