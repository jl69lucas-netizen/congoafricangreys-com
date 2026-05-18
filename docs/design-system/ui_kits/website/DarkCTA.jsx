// DarkCTA — bottom-of-page conversion block. Uppercase clay headline on near-black bg.
const DarkCTA = ({ onClick }) => (
  <section className="dark-cta" data-screen-label="DarkCTA">
    <h2>Reserve Your<br/>African Grey</h2>
    <p>Captive-bred, hand-fed, fully documented. Tell us about your home — we read every inquiry personally.</p>
    <button className="btn btn-primary" onClick={onClick}>Start an Inquiry</button>
  </section>
);

window.DarkCTA = DarkCTA;
