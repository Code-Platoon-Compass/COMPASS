export async function fetchInviteLink(cohortId, apiKey) {
  const res = await fetch(
    `http://localhost:8000/cohort_app/${cohortId}/invite-link/`,
    {
      method: "GET",
      headers: {
        "X-API-Key": apiKey,
      },
    }
  );

  if (!res.ok) {
    const errorText = await res.text();
    throw new Error(`Error fetching invite link: ${errorText}`);
  }

  return res.json();
}
