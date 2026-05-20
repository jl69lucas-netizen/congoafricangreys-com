// Navbar — forest green, sticky, with brand mark + nav links + CTA
const Navbar = ({ current = 'home', onNavigate }) => {
  const links = [
    { id: 'home',     label: 'Home' },
    { id: 'birds',    label: 'Available Birds' },
    { id: 'about',    label: 'Our Aviary' },
    { id: 'shipping', label: 'Shipping & Care' },
    { id: 'contact',  label: 'Contact' },
  ];
  return (
    <nav className="nav" data-screen-label="Navbar">
      <div className="nav-inner">
        <a className="nav-brand" href="#" onClick={(e) => { e.preventDefault(); onNavigate('home'); }}>
          <span className="mark">🦜</span>
          <span>CongoAfricanGreys</span>
        </a>
        <div className="nav-links">
          {links.map(l => (
            <a key={l.id}
               href={`#${l.id}`}
               className={current === l.id ? 'active' : ''}
               onClick={(e) => { e.preventDefault(); onNavigate(l.id); }}>
              {l.label}
            </a>
          ))}
        </div>
        <button className="nav-cta" onClick={() => onNavigate('contact')}>Reserve Your Grey</button>
      </div>
    </nav>
  );
};

window.Navbar = Navbar;
