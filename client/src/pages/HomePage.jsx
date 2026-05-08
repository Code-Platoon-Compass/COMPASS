import CheckIn from "../components/widgets/CheckIn";
import Vocab from "../components/Vocab";
import { useState, useEffect } from "react";
import { fetchInviteLink } from "../utilities/cohortUtilities";

const HomePage = () => {
  const [inviteUrl, setInviteUrl] = useState(null);

  // Temporary placeholder values — replace with real ones later
  const cohortId = "8b0e9f4e-3e4a-4f0a-9a3d-123456789abc";
  const apiKey = "instructor_test_api_key_12345";

  useEffect(() => {
    async function loadInvite() {
      try {
        const data = await fetchInviteLink(cohortId, apiKey);
        setInviteUrl(data.invite_url);
      } catch (err) {
        console.error("Error fetching invite link:", err);
      }
    }

    loadInvite();
  }, []);

  return (
    <>
      <h1>hi i'm the homepage</h1>

      {inviteUrl ? (
        <p>Invite Link: {inviteUrl}</p>
      ) : (
        <p>Loading invite link...</p>
      )}

      <Vocab />
      <CheckIn url="https://example.com" />
    </>
  );
};

export default HomePage;
