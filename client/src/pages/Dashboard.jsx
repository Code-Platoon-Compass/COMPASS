import CheckIn from "../components/widgets/CheckIn";
import Vocab from "../components/Vocab";
import LogoutButton from '../components/LogoutButton';
import TimezoneClock from '../components/TimezoneClock';

export default function Dashboard() {
    return (
        <>
            <h1>hi i'm the dashboard</h1>
            <Vocab /> 
            <CheckIn url="https://example.com" />
            <TimezoneClock />
            <LogoutButton />
        </>
    )
}