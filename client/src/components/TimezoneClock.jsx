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

  return (
    <>
      <header>Time in Chicago</header>
      {time}
    </>
  );
}
