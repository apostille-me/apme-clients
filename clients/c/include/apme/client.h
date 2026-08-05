#ifndef APME_CLIENT_H
#define APME_CLIENT_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define APME_CLIENT_DEFAULT_BASE_URL "https://api.apostille.me"

typedef struct apme_client_config {
  const char *base_url;
  const char *bearer_token;
} apme_client_config_t;

apme_client_config_t apme_client_default_config(void);

/*
 * Builds a normalized endpoint URL in caller-owned storage.
 * Returns 0 on success, -1 for invalid arguments, and -2 when the buffer is too small.
 */
int apme_client_build_url(
    const apme_client_config_t *config,
    const char *path,
    char *output,
    size_t output_capacity);

#ifdef __cplusplus
}
#endif

#endif
