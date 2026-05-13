import CheckIn from "../components/widgets/CheckIn";
import Vocab from "../components/Vocab";
import DailyLinks from "../components/widgets/DailyLinks";
import Nav from '../components/Nav';
import Footer from '../components/Footer';
import { useOutletContext } from "react-router-dom";

function getGreeting() {
    const hour = new Date().getHours();
    if (hour < 12) return "Good morning";
    if (hour < 17) return "Good afternoon";
    return "Good evening";
}

export default function Dashboard() {
    const { user } = useOutletContext();
    const firstName = user?.name?.split(" ")[0];

    return (
        <div className="min-h-screen flex flex-col bg-[#f0f2f5]">
            <Nav />

            {/* Hero welcome section */}
            <div className="bg-[#0d2e4a] px-8 py-10 flex items-center justify-between">
                <div>
                    <p className="text-[#e7771e] text-xs font-semibold tracking-widest uppercase mb-2">
                        CODE PLATOON · STUDENT RESOURCE HUB
                    </p>
                    {user && (
                        <h1 className="text-white text-4xl font-bold">
                            {getGreeting()},{" "}
                            <span className="text-[#e7771e] italic">{firstName}.</span>
                        </h1>
                    )}
                </div>
            </div>

            {/* Main content */}
            <main className="flex-1 px-8 py-8 space-y-6">

                {/* Row 1: Daily Links + Check-In */}
                <div className="grid grid-cols-2 gap-6">

                    {/* Daily Links card */}
                    <div className="bg-white border border-gray-200 rounded-none overflow-hidden">
                        <div className="flex items-center justify-between px-6 py-4 border-b border-gray-200">
                            <span className="text-[#3b7f82] text-xs font-semibold tracking-widest uppercase">Daily Links</span>
                            <span className="border border-gray-300 text-gray-500 text-xs px-3 py-1">QUICK ACCESS</span>
                        </div>
                        <div className="px-6 py-4">
                            {user && <DailyLinks url={`/api/v1/cohorts/${user["cohort_id"]}/daily-links`} columns={2} layout="row" />}
                        </div>
                    </div>

                    {/* Check-In card */}
                    <div className="bg-white border border-gray-200 rounded-none overflow-hidden">
                        <div className="flex items-center justify-between px-6 py-4 border-b border-gray-200">
                            <span className="text-[#3b7f82] text-xs font-semibold tracking-widest uppercase">Daily Check-In</span>
                            <span className="border border-gray-300 text-gray-500 text-xs px-3 py-1">REQUIRED</span>
                        </div>
                        <div className="px-6 py-4 flex flex-col items-center justify-center text-center min-h-[220px] gap-4">
                            <div>
                                <p className="text-[#0d2e4a] font-bold text-lg leading-snug">Have you completed your</p>
                                <p className="text-[#e7771e] font-bold italic text-lg leading-snug">daily check-in form?</p>
                            </div>
                            <p className="text-gray-400 text-sm">Takes less than 2 minutes · Helps the team support you</p>
                            <CheckIn url="https://example.com" />
                        </div>
                    </div>

                </div>

                {/* Row 2: Resource Links */}
                <div className="bg-white border border-gray-200 rounded-none overflow-hidden">
                    <div className="flex items-center justify-between px-6 py-4 border-b border-gray-200">
                        <span className="text-[#3b7f82] text-xs font-semibold tracking-widest uppercase">Resource Links</span>
                    </div>
                    <div className="px-6 py-4">
                        {user && <DailyLinks url={`/api/v1/cohorts/${user["cohort_id"]}/resource-links`} columns={5} layout="column" />}
                    </div>
                </div>

                {/* Row 3: Vocab */}
                <Vocab />

            </main>

            <Footer />
        </div>
    );
}


