import tempLogo from '../assets/temp_logo.png';


const HomePage = () => {

    return (
        <>
            <section className="hero">
                <div className="hero-content">
                    <img src={tempLogo} alt="COMPASS logo" className="mx-auto mb-8 w-75 max-w-md" />
                    <h1 className="hero-title">Welcome to COMPASS</h1>
                    <p className="hero-description">Your all-in-one tool for navigating the Code Platoon curriculum and community.</p>
                </div>
                <div className="start-btn">
                    <button className="btn-primary" onClick={() => window.location.href = '/auth'}>Get Started</button>
                </div>
            </section>
            <h1>hi i'm the homepage</h1>
            
            
            
        </>
    );
}

export default HomePage;
