// components/Navbar.tsx
import Link from 'next/link';

const Navbar: React.FC = () => {
  return (
    <nav className="navbar navbar-expand-lg sticky-top">
      <Link href="/">
        <a className="navbar-brand FW-bold fst-italic">U ARE IN MORROS SPACE ; Start here</a>
      </Link>

      <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span className="navbar-toggler-icon"></span>
      </button>

      <div className="collapse navbar-collapse" id="navbarNavDropdown">
        <ul className="navbar-nav ms-auto">
          <li className="nav-item mr-2">
            <Link href="/projects">
              <a className="nav-link">Projects</a>
            </Link>
          </li>

          <li className="nav-item mr-2">
            <Link href="/blog">
              <a className="nav-link">Blog</a>
            </Link>
          </li>

          <li className="nav-item">
            <a className="nav-link" href="https://www.github.com/morroshub" target="_blank" rel="noopener noreferrer">Github Profile</a>
          </li>

          <li className="nav-item mr-2">
            <a className="nav-link" href="/static/porfolio/LucasMorrone-Dev-python-data.pdf" target="_blank" rel="noopener noreferrer">Certifications PDF</a>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
