import miniLogo from '../assets/compass-mini.svg';
import { useNavigate, useOutletContext } from 'react-router-dom';
import LogoutButton from './LogoutButton';
import TimezoneClock from './TimezoneClock';

export default function Nav() {
    const navigate = useNavigate();
    const { user } = useOutletContext();

  return (
    <div className="sticky top-0 z-50"> {/* NAV */}
          <nav className="cp-nav">
            <div className="nav-logo" onClick={() => navigate('/')} style={{ cursor: 'pointer' }}>
              <img src={miniLogo} alt="COMPASS logo" width="50" height="50" />
              <div>
                <div className="nav-logo-text">COMPASS</div>
                <div className=" text-white">Code Platoon Hub</div>
              </div>
            </div>
            <div className="nav-right">
              {user && <TimezoneClock />}
              {user
                ? <LogoutButton />
                : <button className="btn-primary" onClick={() => navigate('/auth')}>Get Started</button>
              }
            </div>
          </nav>
    </div>
  )
}
