<<<<<<< HEAD
import CheckIn from "../components/widgets/CheckIn";
import Vocab from "../components/Vocab";
import DailyLinks from "../components/widgets/DailyLinks";
=======
import tempLogo from '../assets/temp_logo.png';
>>>>>>> dab7715 (updated styling and fixed token error in google auth)


const HomePage = () => {

<<<<<<< HEAD
  return (
    <>
      <h1>hi i'm the homepage</h1>
      <Vocab /> 
      <CheckIn url="https://example.com" />
      <DailyLinks url="/api/links" />
    </>
  );
};
=======
    return (
        <>
            <section className="hero">
                <div className="hero-content">
                    <img src={tempLogo} alt="COMPASS logo" className="mx-auto mb-8 w-75 max-w-md" />
                    <h1 className="hero-title">Welcome to COMPASS</h1>
                    <p className="hero-description">Your all-in-one tool for navigating the Code Platoon curriculum and community.</p>
                </div>
                <div>
                    <button className="btn-primary" onClick={() => window.location.href = '/auth'}>Get Started</button>
                </div>
            </section>
            <h1>hi i'm the homepage</h1>
            
            
            
        </>
    );
}
>>>>>>> dab7715 (updated styling and fixed token error in google auth)

export default HomePage;
