import compassLogo from '../assets/COMPASS.svg';

export default function Footer() {
  return (
    <div className="cp-footer">
        <div className="footer-text">COMPASS &middot; Code Platoon Student Hub &middot; Built by cohort</div>
        <div className="footer-logo">
            <img src={compassLogo} alt="COMPASS logo" width="32" height="32" />
            COMPASS
        </div>
    </div>
  )
}
