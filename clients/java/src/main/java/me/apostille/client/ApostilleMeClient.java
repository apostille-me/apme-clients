package me.apostille.client;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.Duration;
import java.util.Map;
import java.util.Objects;

public final class ApostilleMeClient {
    private final String baseUrl;
    private final String token;
    private final Map<String, String> headers;
    private final HttpClient http;

    public ApostilleMeClient(String baseUrl, String token, Map<String, String> headers) {
        this.baseUrl = Objects.requireNonNull(baseUrl).replaceAll("/+$", "");
        this.token = token;
        this.headers = Map.copyOf(headers == null ? Map.of() : headers);
        this.http = HttpClient.newBuilder().connectTimeout(Duration.ofSeconds(30)).build();
    }

    public HttpResponse<String> request(String method, String path, String jsonBody)
            throws IOException, InterruptedException {
        HttpRequest.Builder builder = HttpRequest.newBuilder()
            .uri(URI.create(baseUrl + "/" + path.replaceFirst("^/+", "")))
            .timeout(Duration.ofSeconds(30))
            .header("Accept", "application/json");
        headers.forEach(builder::header);
        if (token != null && !token.isBlank()) builder.header("Authorization", "Bearer " + token);
        HttpRequest.BodyPublisher body = jsonBody == null
            ? HttpRequest.BodyPublishers.noBody()
            : HttpRequest.BodyPublishers.ofString(jsonBody);
        if (jsonBody != null) builder.header("Content-Type", "application/json");
        return http.send(builder.method(method.toUpperCase(), body).build(), HttpResponse.BodyHandlers.ofString());
    }
}
