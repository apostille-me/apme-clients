const std = @import("std");

pub const ClientError = error{InvalidBaseUrl};

pub const Client = struct {
    allocator: std.mem.Allocator,
    base_url: []const u8 = "https://api.apostille.me",
    bearer_token: ?[]const u8 = null,

    pub fn url(self: Client, path: []const u8) ![]u8 {
        const clean_base = std.mem.trimRight(u8, self.base_url, "/");
        if (!validBaseUrl(clean_base)) return ClientError.InvalidBaseUrl;

        const clean_path = std.mem.trimLeft(u8, path, "/");
        if (clean_path.len == 0) {
            return self.allocator.dupe(u8, clean_base);
        }
        return std.fmt.allocPrint(self.allocator, "{s}/{s}", .{ clean_base, clean_path });
    }
};

fn loopbackAuthority(base_url: []const u8, prefix: []const u8) bool {
    if (!std.mem.startsWith(u8, base_url, prefix)) return false;
    if (base_url.len == prefix.len) return true;
    const next = base_url[prefix.len];
    return next == ':' or next == '/';
}

fn validBaseUrl(base_url: []const u8) bool {
    return std.mem.startsWith(u8, base_url, "https://") or
        loopbackAuthority(base_url, "http://localhost") or
        loopbackAuthority(base_url, "http://127.0.0.1") or
        loopbackAuthority(base_url, "http://[::1]");
}

test "normalizes endpoint URLs" {
    const client = Client{
        .allocator = std.testing.allocator,
        .base_url = "https://api.example.test/",
        .bearer_token = "test-token",
    };
    const endpoint = try client.url("/health");
    defer std.testing.allocator.free(endpoint);
    try std.testing.expectEqualStrings("https://api.example.test/health", endpoint);
}

test "allows loopback HTTP" {
    const client = Client{
        .allocator = std.testing.allocator,
        .base_url = "http://localhost:8787/",
    };
    const endpoint = try client.url("/health");
    defer std.testing.allocator.free(endpoint);
    try std.testing.expectEqualStrings("http://localhost:8787/health", endpoint);
}

test "rejects non-loopback plaintext endpoints" {
    for ([_][]const u8{ "http://example.com", "http://localhost.evil" }) |invalid| {
        const client = Client{
            .allocator = std.testing.allocator,
            .base_url = invalid,
        };
        try std.testing.expectError(ClientError.InvalidBaseUrl, client.url("/health"));
    }
}
