// Static parity audit; Atto guest execution is a separate compiler check.
#[test]
fn atto_route_specs_match_rust_client() {
    let atto = include_str!("../../../experimental/atto/client.atto");
    let rust = include_str!("../src/lib.rs");
    for (method, path, verb) in [
        ("health", "/healthz", "GET"),
        ("config", "/api/config", "GET"),
        ("events", "/api/events", "POST"),
        ("alerts", "/api/alerts", "POST"),
    ] {
        assert!(atto.contains(&format!("pub {method}_path(): string {{ return \"{path}\"; }}")));
        assert!(atto.contains(&format!("pub {method}_method(): string {{ return \"{verb}\"; }}")));
        assert!(rust.contains(&format!("pub fn {method}(&self) -> RequestSpec")));
        assert!(rust.contains(&format!("\"{path}\"")));
    }
    assert!(atto.contains("// expect-exit: 42"));
}
