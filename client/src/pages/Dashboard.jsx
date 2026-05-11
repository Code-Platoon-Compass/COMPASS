import CheckIn from "../components/widgets/CheckIn";
import Vocab from "../components/Vocab";
import LogoutButton from '../components/LogoutButton';
import  DailyLinks from "../components/widgets/DailyLinks";

export default function Dashboard() {
    return (
        <>
            <h1>hi i'm the dashboard</h1>
            <Vocab /> 
            <CheckIn url="https://example.com" />
            <DailyLinks />
            <div className="logout-btn-wrapper">
                <LogoutButton />
            </div>
        </>
    )
}