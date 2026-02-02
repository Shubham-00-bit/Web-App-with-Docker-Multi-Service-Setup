import { useEffect, useState } from "react";

function App() {
  const [msg, setMsg] = useState("");

  useEffect(() => {
    fetch("/api/health")
      .then(res => res.json())
      .then(data => setMsg(data.status));
  }, []);

  return <h1>{msg}</h1>;
}

export default App;
