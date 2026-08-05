from __future__ import annotations

from dataclasses import dataclass, field
import json
from typing import Any, Mapping
from urllib import error, request


class ApostilleMeError(RuntimeError):
    """Raised when the Apostille Me API returns a non-success response."""


@dataclass(frozen=True, slots=True)
class ApostilleMeClient:
    base_url: str
    token: str | None = None
    headers: Mapping[str, str] = field(default_factory=dict)
    timeout_seconds: float = 30.0

    def request(self, method: str, path: str, body: Any | None = None) -> Any:
        url = f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"
        headers = {"Accept": "application/json", **dict(self.headers)}
        if self.token:
            headers.setdefault("Authorization", f"Bearer {self.token}")
        payload = None
        if body is not None:
            headers.setdefault("Content-Type", "application/json")
            payload = json.dumps(body).encode("utf-8")

        req = request.Request(url, data=payload, headers=headers, method=method.upper())
        try:
            with request.urlopen(req, timeout=self.timeout_seconds) as response:
                raw = response.read()
                return None if not raw else json.loads(raw)
        except error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise ApostilleMeError(f"HTTP {exc.code}: {detail}") from exc


__all__ = ["ApostilleMeClient", "ApostilleMeError"]
