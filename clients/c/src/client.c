#include "apme/client.h"

#include <string.h>

static int starts_with(const char *value, const char *prefix) {
  return strncmp(value, prefix, strlen(prefix)) == 0;
}

static int loopback_authority(const char *value, const char *prefix) {
  const size_t prefix_length = strlen(prefix);
  if (strncmp(value, prefix, prefix_length) != 0) {
    return 0;
  }
  const char next = value[prefix_length];
  return next == '\0' || next == ':' || next == '/';
}

static int allowed_base_url(const char *base_url) {
  return starts_with(base_url, "https://") ||
         loopback_authority(base_url, "http://localhost") ||
         loopback_authority(base_url, "http://127.0.0.1") ||
         loopback_authority(base_url, "http://[::1]");
}

apme_client_config_t apme_client_default_config(void) {
  apme_client_config_t config = {APME_CLIENT_DEFAULT_BASE_URL, NULL};
  return config;
}

int apme_client_build_url(
    const apme_client_config_t *config,
    const char *path,
    char *output,
    size_t output_capacity) {
  if (config == NULL || config->base_url == NULL || path == NULL || output == NULL ||
      !allowed_base_url(config->base_url)) {
    return -1;
  }

  size_t base_length = strlen(config->base_url);
  while (base_length > 0 && config->base_url[base_length - 1] == '/') {
    base_length--;
  }

  while (*path == '/') {
    path++;
  }
  const size_t path_length = strlen(path);
  const size_t separator_length = path_length == 0 ? 0 : 1;
  const size_t required = base_length + separator_length + path_length + 1;
  if (output_capacity < required) {
    return -2;
  }

  memcpy(output, config->base_url, base_length);
  size_t cursor = base_length;
  if (separator_length != 0) {
    output[cursor++] = '/';
    memcpy(output + cursor, path, path_length);
    cursor += path_length;
  }
  output[cursor] = '\0';
  return 0;
}
