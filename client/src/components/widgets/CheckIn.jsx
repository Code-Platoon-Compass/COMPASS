import { useState } from "react";

const lastOpenedKey = "codeplatoon-compass-check-in-form-last-opened";

export default function CheckIn({ url }) {
  /**
   * Is the form ready to be completed today?
   * @returns false if already completed
   */
  const canOpen = () => {
    const unparsedLastOpened = localStorage.getItem(lastOpenedKey);
    if (!unparsedLastOpened) return true;

    // date on which form was last opened
    const lastOpened = new Date(unparsedLastOpened);

    // today at midnight central
    const today = new Date().setUTCHours(5, 0, 0, 0);

    console.log(new Date(today));

    // was it opened no later than midnight today?
    return lastOpened < today;
  };

  const [isFormEnabled, setIsFormEnabled] = useState(canOpen());

  /**
   * Update local storage
   */
  const onOpenedForm = () => {
    localStorage.setItem(lastOpenedKey, new Date().toISOString());
    setIsFormEnabled(false);
  };

  return (
    <>
      <a
        style={{
          pointerEvents: isFormEnabled ? "" : "none",
          textDecoration: isFormEnabled ? "" : "none",
          backgroundColor: isFormEnabled ? "#ff600d" : "#3b7f82",
          color : isFormEnabled ? "white" : "white",
          padding: "0.5rem 1rem",
          borderRadius: "0.375rem",
          fontWeight: "500",
          fontSize: "0.875rem",
          transition: "background-color 0.3s, color 0.3s",
        }}
        tabIndex={isFormEnabled ? undefined : -1}
        href={url}
        disabled={!isFormEnabled}
        onClick={onOpenedForm}
        target="_blank"
      >
        {isFormEnabled ? "Complete Check-In" : "Completed"}
      </a>
    </>
  );
}
