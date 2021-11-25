export class MusiquepyApiClient {
  serverUrl = "http://localhost:5001";

  getMessage() {
    return fetch(`${this.serverUrl}/echo/hello`).then((resp) => resp.text());
  }
}
