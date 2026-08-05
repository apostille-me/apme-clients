package io.zedpkg.apme
import java.net.URI
data class ApmeClient(val baseUri: URI, val bearerToken: String? = null)
