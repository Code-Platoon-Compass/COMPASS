import { useEffect, useState } from "react";

export default function DailyLinks({ url }) {
  const [links, setLinks] = useState([]);
  const [status, setStatus] = useState("loading");
  const [error, setError] = useState(null);

  useEffect(() => {
    const controller = new AbortController();

    async function fetchLinks() {
      try {
        setStatus("loading");
        const res = await fetch(url, { signal: controller.signal });
        if (!res.ok) throw new Error(`Request failed (${res.status})`);
        const data = await res.json();
        const list = Array.isArray(data) ? data : data.links ?? [];
        setLinks(list);
        setStatus("ready");
      } catch (err) {
        if (err.name === "AbortError") return;
        setError(err.message);
        setStatus("error");
      }
    }

    fetchLinks();
    return () => controller.abort();
  }, [url]);

  return (
    <>
      <header>Daily Links and Resources</header>

      {status === "loading" && <p>Loading links...</p>}

      {status === "error" && <p>Couldn't load links: {error}</p>}

      {status === "ready" && links.length === 0 && (
        <p>No links posted yet.</p>
      )}

      {status === "ready" && links.length > 0 && (
        <ul>
          {links.map((link) => (
            <li key={link.id ?? link.url}>
              <a href={link.url} target="_blank" rel="noopener noreferrer">{link.label}</a>
            </li>
          ))}
        </ul>
      )}
    </>
  );
}