import { useEffect, useMemo, useState } from "react";
import "./App.css";
import "./MusiquepyApiClient";
import { MusiquepyApiClient } from "./MusiquepyApiClient";

function App() {
  const [message, setMessage] = useState("");
  const [sessionData, setSessionData] = useState("");
  const [sessionStatus, setSessionStatus] = useState("");

  const client = useMemo(() => new MusiquepyApiClient(), []);

  useEffect(() => {
    client.getMessage().then((resp) => {
      setMessage(resp);
    }, err => {

    });
  }, [client]);

  const onGetSessionData = () => {
    client.getSessionValue().then((result) => {
      setSessionData(result);
    });
  };
  const onSetSessionData = () => {
    client.setSessionValue().then((result) => {
      setSessionStatus(result);
    });
  };

  return (
    <div className="App">
      <h2>Testing get requests</h2>
      <p>{message}</p>

      <hr />

      <h2>Request with session data</h2>

      <button onClick={onSetSessionData}>Set data</button>

      <p>{sessionStatus}</p>

      <button onClick={onGetSessionData} disabled={!sessionStatus}>
        Get data
      </button>

      <p>{sessionData}</p>
    </div>
  );
}

export default App;
