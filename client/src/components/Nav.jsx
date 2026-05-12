import navLogo from '../assets/compass_logo.svg';
import { useNavigate } from 'react-router-dom';

export default function Nav() {
    const navigate = useNavigate();
  return (
    <div> {/* NAV */}
          <nav className="cp-nav">
            <div className="nav-logo">
              <img src={navLogo} alt="COMPASS logo" width="50" height="50" />
              <div>
                <div className="nav-logo-text">COMPASS</div>
                <div className="nav-logo-sub">Code Platoon Hub</div>
              </div>
            </div>
            <div className="nav-right">
              <button className="btn-primary" onClick={() => navigate('/auth')}>Get Started</button>
            </div>
          </nav>
    </div>
  )
}
