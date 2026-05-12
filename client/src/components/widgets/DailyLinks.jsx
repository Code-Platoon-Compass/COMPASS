import { useState } from "react";

export default function DailyLinks() {
  const [links] = useState([
    { id: 1, label: "Course Syllabus", url: "https://codeplatoon.org" },
    { id: 2, label: "Daily Standup Notes", url: "https://example.com/standup" },
    { id: 3, label: "Cohort Slack", url: "https://slack.com" },
  ]);

  return (
    <>
      <header>Daily Links and Resources</header>
      <ul>
        {links.map((link) => (
          <li key={link.id}>
            <a href={link.url} target="_blank" rel="noopener noreferrer">{link.label}</a>
          </li>
        ))}
      </ul>
    </>
  );
}