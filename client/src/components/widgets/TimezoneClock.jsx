import axios from "axios";
import { useEffect, useState } from "react";

const TIMEZONE = "America/Chicago";
const API_URL = "https://time.now/developer/api";

export default function TimezoneClock() {
  const [time, setTime] = useState();

  const getTime = async () => {
    const time = await axios.get(`${API_URL}/timezone/${TIMEZONE}`);
    setTime(time.data.datetime.split(/[T.]/)[1]);
  };

  useEffect(() => {
    setTimeout(getTime, 1000);
  }, [time]);

  const formatted = time
    ? (() => {
        const [h, m] = time.split(":");
        const hour = parseInt(h, 10);
        const ampm = hour >= 12 ? "PM" : "AM";
        const display = hour % 12 || 12;
        return `Chicago: ${display}:${m} ${ampm}`;
      })()
    : null;

  return (
    <div className="flex items-center gap-2 border border-white text-white text-sm px-3 py-1">
      <svg xmlns="http://www.w3.org/2000/svg" className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
        <circle cx="12" cy="12" r="10" />
        <path strokeLinecap="round" strokeLinejoin="round" d="M12 6v6l4 2" />
      </svg>
      {formatted}
    </div>
  );
}
