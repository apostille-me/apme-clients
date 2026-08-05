export interface ClientOptions {
  baseUrl: string;
  token?: string;
  headers?: Readonly<Record<string, string>>;
  fetchImpl?: typeof fetch;
}

export class ApostilleMeClient {
  readonly baseUrl: string;
  readonly token?: string;
  readonly headers: Readonly<Record<string, string>>;
  readonly fetchImpl: typeof fetch;

  constructor(options: ClientOptions) {
    this.baseUrl = options.baseUrl.replace(/\/+$/, "");
    this.token = options.token;
    this.headers = options.headers ?? {};
    this.fetchImpl = options.fetchImpl ?? fetch;
  }

  async request<T = unknown>(path: string, init: RequestInit = {}): Promise<T> {
    const headers = new Headers(this.headers);
    for (const [key, value] of new Headers(init.headers).entries()) headers.set(key, value);
    if (this.token && !headers.has("authorization")) headers.set("authorization", `Bearer ${this.token}`);
    if (init.body && !headers.has("content-type")) headers.set("content-type", "application/json");

    const response = await this.fetchImpl(`${this.baseUrl}/${path.replace(/^\/+/, "")}`, { ...init, headers });
    if (!response.ok) throw new Error(`Apostille Me request failed: ${response.status}`);
    if (response.status === 204) return undefined as T;
    return (await response.json()) as T;
  }
}
