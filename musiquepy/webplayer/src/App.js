import { useEffect, useState } from "react";
import "./App.css";
import "./MusiquepyApiClient";
import { MusiquepyApiClient } from "./MusiquepyApiClient";

function App() {
  const [message, setMessage] = useState("");
  useEffect(() => {
    const client = new MusiquepyApiClient();
    client.getMessage().then((resp) => {
      setMessage(resp);
    });
  }, []);

  return (
    <div className="App">
      <h2>Message</h2>
      <p>{message}</p>
    </div>
  );
}

export default App;
