// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    name: "ApmeClient",
    platforms: [.iOS(.v15), .macOS(.v12)],
    products: [.library(name: "ApmeClient", targets: ["ApmeClient"])],
    targets: [.target(name: "ApmeClient")]
)
