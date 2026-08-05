const std = @import("std");

pub const Client = struct {
    allocator: std.mem.Allocator,
    base_url: []const u8 = "https://api.apostille.me",
    bearer_token: ?[]const u8 = null,

    pub fn url(self: Client, path: []const u8) ![]u8 {
        const clean_base = std.mem.trimRight(u8, self.base_url, "/");
        const clean_path = std.mem.trimLeft(u8, path, "/");
        if (clean_path.len == 0) {
            return self.allocator.dupe(u8, clean_base);
        }
        return std.fmt.allocPrint(self.allocator, "{s}/{s}", .{ clean_base, clean_path });
    }
};

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
