import CheckIn from "../components/widgets/CheckIn";
import Vocab from "../components/Vocab";
import LogoutButton from '../components/LogoutButton';
import TimezoneClock from '../components/TimezoneClock';
import DailyLinks from "../components/widgets/DailyLinks";
import { useOutletContext } from "react-router-dom";

export default function Dashboard() {
    const { user } = useOutletContext();

    console.log(user);

    return (
        <>
            { user && <h1>Welcome, {user.name.split(" ")[0]}</h1> }
            <h1>hi i'm the dashboard</h1>
            <Vocab /> 
            <CheckIn url="https://example.com" />
            <TimezoneClock />
            <LogoutButton />
            { user && <DailyLinks headerText={"Daily Links"} url={`/api/v1/cohorts/${user["cohort_id"]}/daily-links`} />}
            { user && <DailyLinks headerText={"Resources"} url={`/api/v1/cohorts/${user["cohort_id"]}/resource-links`} />}
        </>
    )
}


