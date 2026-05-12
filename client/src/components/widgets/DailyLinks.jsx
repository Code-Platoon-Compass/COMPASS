import { useEffect, useState } from "react";
import {
  FaCalendarAlt, FaVideo, FaSlack, FaBook, FaYoutube,
  FaGithub, FaComments, FaCode, FaLink,
} from "react-icons/fa";
import { SiGoogledrive } from "react-icons/si";

const ICON_MAP = [
  ["calendar", FaCalendarAlt],
  ["zoom",     FaVideo],
  ["slack",    FaSlack],
  ["curriculum", FaBook],
  ["youtube",  FaYoutube],
  ["github",   FaGithub],
  ["retro",    FaComments],
  ["codewars", FaCode],
  ["drive",    SiGoogledrive],
];

function getIcon(label) {
  const lower = label.toLowerCase();
  for (const [key, Icon] of ICON_MAP) {
    if (lower.includes(key)) return Icon;
  }
  return FaLink;
}

export default function DailyLinks({ url, columns = 2, layout = "row" }) {
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

  const gridCols = columns === 5 ? "grid-cols-5" : "grid-cols-2";

  return (
    <>
      {status === "loading" && <p className="text-gray-400 text-sm py-4">Loading links...</p>}
      {status === "error"   && <p className="text-red-400 text-sm py-4">Couldn't load links: {error}</p>}
      {status === "ready" && links.length === 0 && (
        <p className="text-gray-400 text-sm py-4">No links posted yet.</p>
      )}
      {status === "ready" && links.length > 0 && (
        <div className={`grid gap-3 ${gridCols}`}>
          {links.map((link) => {
            const Icon = getIcon(link.label);
            return (
              <a
                key={link.id ?? link.url}
                href={link.url}
                target="_blank"
                rel="noopener noreferrer"
                className={`border border-gray-200 bg-white hover:bg-gray-50 transition-colors flex ${
                  layout === "column"
                    ? "flex-col items-center justify-center py-6 gap-3"
                    : "flex-row items-center gap-4 px-4 py-4"
                }`}
              >
                <Icon className={`text-[#e7771e] ${layout === "column" ? "text-2xl" : "text-xl"}`} />
                <span className={`font-semibold text-gray-800 tracking-wide uppercase ${layout === "column" ? "text-xs" : "text-sm"}`}>
                  {link.label}
                </span>
              </a>
            );
          })}
        </div>
      )}
    </>
  );
}