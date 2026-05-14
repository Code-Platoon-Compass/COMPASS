import compassLogo from '../assets/COMPASS.svg';
import { useNavigate, useOutletContext } from 'react-router-dom';

export default function Hero() {
    const navigate = useNavigate();
    const { user } = useOutletContext();
  return (
    <div>
          <div className="hero">
            <div className="hero-inner">
              <div className="hero-left">
                <div className="hero-crumb">
                  &#8962; Home &rsaquo; <span>About</span>
                </div>
                <div className="hero-eyebrow">Code Platoon &middot; Student Resource Hub</div>
                <h1 className="hero-title">About <em>COMPASS</em></h1>
                <p className="hero-desc">
                  COMPASS is a student-built hub designed to give every Code Platoon cohort a single, reliable place to find what you need. Combining everything from curriculum links to live AI-powered tools, so you can spend less time hunting and more time learning . 
                  </p>
                  <p className="hero-desc">
                    <strong>Built by students, for students:</strong> this app demonstrates the full-stack skills taught in the program so you can learn them faster than we did.
                  </p>
                <div className="hero-btns">
                  <button className="btn-primary" onClick={() => navigate(user ? '/dashboard' : '/auth')}>&#8594; Explore resources</button>
                 
                </div>
                <div className="hero-stats">
                  <div className="stat">
                    <div className="stat-val">6+</div>
                    <div className="stat-label">Resources</div>
                  </div>
                  <div className="stat">
                    <div className="stat-val">AI</div>
                    <div className="stat-label">Vocab engine</div>
                  </div>
                  <div className="stat">
                    <div className="stat-val">24/7</div>
                    <div className="stat-label">Always on</div>
                  </div>
                </div>
              </div>
              <div className="hero-logo">
                <img src={compassLogo} alt="COMPASS logo" width="520" height="320" />
              </div>
            </div>
          </div></div>
  )
}
