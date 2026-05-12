import compassLogo from '../assets/COMPASS.svg';
import { useNavigate } from 'react-router-dom';

export default function Hero() {
    const navigate = useNavigate();
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
                  COMPASS is a student-built hub designed to give every Code Platoon cohort a single,
                  reliable place to find what they need &mdash; from curriculum links to live AI-powered
                  tools that make the learning experience smoother.
                </p>
                <div className="hero-btns">
                  <button className="btn-primary" onClick={() => navigate('/auth')}>&#8594; Explore resources</button>
                 
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
                <img src={compassLogo} alt="COMPASS logo" width="320" height="320" />
              </div>
            </div>
          </div></div>
  )
}
