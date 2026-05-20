// Footer — dark, four-column. Brand block, sitemap, contact, legal.
const Footer = () => (
  <footer className="footer" data-screen-label="Footer">
    <div className="footer-inner">
      <div>
        <div className="brand"><span>🦜</span><span>CongoAfricanGreys</span></div>
        <p className="tagline">
          A small family aviary in Midland, Texas. Captive-bred, hand-fed
          African Greys since 2014.
        </p>
        <span className="tag-green">USDA Licensed</span>
      </div>
      <div>
        <h4>Site</h4>
        <a href="#">Available Birds</a>
        <a href="#">Our Aviary</a>
        <a href="#">Shipping &amp; Care</a>
        <a href="#">FAQ</a>
        <a href="#">Contact</a>
      </div>
      <div>
        <h4>Contact</h4>
        <a href="tel:+14325550114">📞 (432) 555-0114</a>
        <a href="mailto:hello@congoafricangreys.com">✉️ hello@congoaf…</a>
        <a href="#">📍 Midland, TX 79703</a>
        <a href="#">🕐 Tue–Sat, 10a–5p</a>
      </div>
      <div>
        <h4>Trust</h4>
        <a href="#">CITES Appendix II</a>
        <a href="#">USDA AWA License</a>
        <a href="#">Health Guarantee</a>
        <a href="#">Return Policy</a>
      </div>
    </div>
    <div className="legal">
      <span>© 2014–2026 Mark &amp; Teri Benjamin · CongoAfricanGreys.com</span>
      <span>Captive-bred · Fully documented · No wild-caught birds.</span>
    </div>
  </footer>
);

window.Footer = Footer;
