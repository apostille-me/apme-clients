// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    name: "ApmeClient",
    platforms: [.macOS(.v12), .iOS(.v15)],
    products: [.library(name: "ApmeClient", targets: ["ApmeClient"])],
    targets: [
        .target(name: "ApmeClient"),
        .testTarget(name: "ApmeClientTests", dependencies: ["ApmeClient"])
    ]
)
