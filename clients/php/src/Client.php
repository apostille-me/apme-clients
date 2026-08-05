<?php

declare(strict_types=1);

namespace ApostilleMe;

use RuntimeException;

final class Client
{
    public function __construct(
        private readonly string $baseUrl,
        private readonly ?string $token = null,
        private readonly array $headers = [],
    ) {}

    public function request(string $method, string $path, mixed $body = null): mixed
    {
        $headers = array_merge(['Accept: application/json'], $this->headers);
        if ($this->token !== null) $headers[] = 'Authorization: Bearer ' . $this->token;
        $content = null;
        if ($body !== null) {
            $headers[] = 'Content-Type: application/json';
            $content = json_encode($body, JSON_THROW_ON_ERROR);
        }

        $context = stream_context_create(['http' => [
            'method' => strtoupper($method),
            'header' => implode("\r\n", $headers),
            'content' => $content ?? '',
            'ignore_errors' => true,
            'timeout' => 30,
        ]]);
        $url = rtrim($this->baseUrl, '/') . '/' . ltrim($path, '/');
        $response = file_get_contents($url, false, $context);
        if ($response === false) throw new RuntimeException('Apostille Me request failed');
        return $response === '' ? null : json_decode($response, true, 512, JSON_THROW_ON_ERROR);
    }
}
