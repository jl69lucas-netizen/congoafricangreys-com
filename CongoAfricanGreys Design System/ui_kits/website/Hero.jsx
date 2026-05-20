// Hero — warm-gradient banner with eyebrow tag, Lora headline with italic accent, lead, two CTAs.
const Hero = ({ onPrimary, onSecondary }) => (
  <section className="hero" data-screen-label="Hero">
    <span className="hero-eyebrow">🦜 Captive-bred · Midland, TX · Est. 2014</span>
    <h1>
      Bringing home an <em>African Grey</em><br/>
      is a thirty-year decision.
    </h1>
    <p className="lead">
      We've spent the last decade helping families make it well.
      Every bird is hand-fed, DNA-sexed, and arrives with full CITES
      Appendix&nbsp;II documentation.
    </p>
    <div className="hero-ctas">
      <button className="btn btn-primary" onClick={onPrimary}>Reserve Your Grey →</button>
      <button className="btn btn-outline" onClick={onSecondary}>View Available Birds</button>
    </div>
  </section>
);

window.Hero = Hero;
