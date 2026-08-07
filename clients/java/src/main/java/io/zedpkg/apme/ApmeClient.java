package io.zedpkg.apme;
import java.net.URI;
public record ApmeClient(URI baseUri, String bearerToken) {}
