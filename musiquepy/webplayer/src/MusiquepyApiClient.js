export class MusiquepyApiClient {
  serverUrl = "http://localhost:5001";

  getMessage() {
    return fetch(`${this.serverUrl}/echo/hello`).then((resp) => resp.text());
  }

  setSessionValue() {
    return fetch(`${this.serverUrl}/echo/session/value-set`, {
      method: "POST",
      credentials: "include",
    }).then((resp) => resp.text());
  }

  getSessionValue() {
    return fetch(`${this.serverUrl}/echo/session/value-get`, {
      credentials: "include",
    }).then((resp) => resp.text());
  }
}
