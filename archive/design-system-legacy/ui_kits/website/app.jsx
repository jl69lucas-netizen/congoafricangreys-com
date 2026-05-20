// CongoAfricanGreys.com — interactive prototype
// Routes between Home, Birds, Contact, and a Confirmation state.
// Components are loaded as siblings; they expose themselves via window.

const { useState, useEffect } = React;

const BIRDS = [
  { id:'otis',  name:'Otis',   species:'Congo Grey',  sex:'Hen',  age:'18 weeks', weaned:true,  ready:'now',         tag:'Available', price:'Inquire for pricing' },
  { id:'juno',  name:'Juno',   species:'Congo Grey',  sex:'Cock', age:'14 weeks', weaned:false, ready:'in 2 weeks',  tag:'Reserved hold', price:'Inquire for pricing' },
  { id:'rumi',  name:'Rumi',   species:'Timneh Grey', sex:'Hen',  age:'16 weeks', weaned:true,  ready:'now',         tag:'Available', price:'Inquire for pricing' },
  { id:'pip',   name:'Pip',    species:'Congo Grey',  sex:'Hen',  age:'11 weeks', weaned:false, ready:'in 5 weeks',  tag:'Hand-feeding', price:'Inquire for pricing' },
  { id:'wren',  name:'Wren',   species:'Congo Grey',  sex:'Cock', age:'20 weeks', weaned:true,  ready:'now',         tag:'Available', price:'Inquire for pricing' },
  { id:'sage',  name:'Sage',   species:'Timneh Grey', sex:'Cock', age:'13 weeks', weaned:false, ready:'in 3 weeks',  tag:'Hand-feeding', price:'Inquire for pricing' },
];

const App = () => {
  const [route, setRoute] = useState('home');
  const [selectedBird, setSelectedBird] = useState(null);
  const [confirmation, setConfirmation] = useState(null);

  useEffect(() => { window.scrollTo(0, 0); }, [route]);

  const navigate = (id) => { setSelectedBird(null); setConfirmation(null); setRoute(id); };
  const inquire = (bird) => { setSelectedBird(bird); setConfirmation(null); setRoute('contact'); };
  const onSubmitted = (data) => { setConfirmation({ ...data, bird: selectedBird }); };

  return (
    <>
      <Navbar current={route} onNavigate={navigate} />

      {route === 'home' && (
        <main>
          <Hero
            onPrimary={() => navigate('contact')}
            onSecondary={() => navigate('birds')}
          />
          <section className="section">
            <div className="container">
              <TrustRow />
            </div>
          </section>

          <div className="divider">❋</div>

          <section className="section">
            <div className="container">
              <span className="sect-eyebrow">Available now</span>
              <h2 className="sect-title">Our current <em>clutch</em></h2>
              <p className="sect-sub">
                Each bird is DNA-sexed, vet-checked, and hand-fed in our home.
                We update this page as birds wean and become ready to place.
              </p>
              <div className="card-grid">
                {BIRDS.slice(0, 3).map(b => (
                  <BirdCard key={b.id} bird={b} onInquire={inquire} />
                ))}
              </div>
              <div style={{ textAlign:'center', marginTop: 36 }}>
                <button className="btn btn-outline" onClick={() => navigate('birds')}>
                  See all {BIRDS.length} available birds
                </button>
              </div>
            </div>
          </section>

          <section className="section" style={{ background: 'var(--card-bg)', borderTop: '1px solid var(--border)', borderBottom: '1px solid var(--border)' }}>
            <div className="container" style={{ display:'grid', gridTemplateColumns:'1.1fr .9fr', gap: 40, alignItems:'start' }}>
              <div>
                <span className="sect-eyebrow" style={{ textAlign:'left' }}>Our family</span>
                <h2 className="sect-title" style={{ textAlign:'left' }}>Mark &amp; Teri <em>Benjamin</em></h2>
                <p style={{ color:'var(--mid)', fontSize: 16, lineHeight: 1.65 }}>
                  We started CongoAfricanGreys in 2014 out of our home aviary
                  in Midland, Texas — a small, captive-bred-only operation
                  that has placed birds with families across the country.
                  We hand-feed every chick ourselves and stay in touch for
                  the lifetime of the bird.
                </p>
                <p style={{ color:'var(--mid)', fontSize: 16, lineHeight: 1.65 }}>
                  Every bird leaves with USDA paperwork, CITES Appendix II
                  documentation, a DNA-sex certificate, and an avian-vet
                  wellness check. No wild-caught birds, ever.
                </p>
                <button className="btn btn-primary" onClick={() => navigate('about')}>About our aviary →</button>
              </div>
              <InfoCard
                title="Visit our aviary"
                sub="By appointment, Midland TX"
                rows={[
                  { ico:'📍', key:'Midland, TX 79703', val:'Exact address shared after we connect' },
                  { ico:'🕐', key:'Tuesday–Saturday',  val:'10:00 AM – 5:00 PM CT' },
                  { ico:'📞', key:'(432) 555-0114',    val:'Voice or text · 24–48 hr reply' },
                  { ico:'✉️', key:'hello@congoaf…',    val:'We read every inquiry personally' },
                ]}
              />
            </div>
          </section>

          <DarkCTA onClick={() => navigate('contact')} />
          <Footer />
        </main>
      )}

      {route === 'birds' && (
        <main>
          <section className="hero" style={{ padding: '64px 48px 56px' }}>
            <span className="hero-eyebrow">🦜 Updated weekly</span>
            <h1 style={{ fontSize: '2.4rem' }}>Available <em>African Greys</em></h1>
            <p className="lead">
              Six birds in our current clutch. Reach out about any one — we'll
              walk you through what's right for your home.
            </p>
          </section>
          <section className="section">
            <div className="container">
              <TrustRow items={[
                { ico: '✅', em: 'USDA-Licensed', text: 'Breeder' },
                { ico: '✅', em: 'CITES',         text: 'Appendix II Documented' },
                { ico: '✅', em: 'DNA-Sexed',     text: '& Vet-Certified' },
                { ico: '✈️', em: 'Ships',         text: 'Nationwide from $185' },
              ]} />
              <div style={{ height: 40 }} />
              <div className="card-grid">
                {BIRDS.map(b => <BirdCard key={b.id} bird={b} onInquire={inquire} />)}
              </div>
            </div>
          </section>
          <DarkCTA onClick={() => navigate('contact')} />
          <Footer />
        </main>
      )}

      {route === 'contact' && !confirmation && (
        <main>
          <section className="hero" style={{ padding: '64px 48px 56px' }}>
            <span className="hero-eyebrow">✉️ 24–48 hour reply</span>
            <h1 style={{ fontSize: '2.4rem' }}>
              {selectedBird ? <>About <em>{selectedBird.name}</em></> : <>Start an <em>inquiry</em></>}
            </h1>
            <p className="lead">
              {selectedBird
                ? <>Tell us about your home and we'll get back to you about {selectedBird.name} — usually within a day.</>
                : <>Tell us about your home and we'll get back to you — usually within a day. We read every inquiry personally.</>
              }
            </p>
          </section>
          <section className="section">
            <div className="container" style={{ display:'grid', gridTemplateColumns:'1.4fr 1fr', gap: 32, alignItems:'start' }}>
              <ContactForm
                defaultBird={selectedBird && selectedBird.species.includes('Timneh') ? 'timneh' : 'congo'}
                onSubmitted={onSubmitted}
              />
              <InfoCard
                title="Reach us directly"
                sub="Mark &amp; Teri Benjamin"
                rows={[
                  { ico:'📞', key:'(432) 555-0114', val:'Voice or text · Tue–Sat 10–5 CT' },
                  { ico:'✉️', key:'hello@congoaf…', val:'We reply within 24–48 hours' },
                  { ico:'📍', key:'Midland, TX',    val:'Aviary visits by appointment' },
                  { ico:'✈️', key:'Ships nationwide', val:'Air shipping from $185 · live-arrival guarantee' },
                ]}
              />
            </div>
          </section>
          <Footer />
        </main>
      )}

      {confirmation && (
        <main>
          <section className="hero" style={{ padding: '96px 48px' }}>
            <span className="hero-eyebrow">✅ Inquiry received</span>
            <h1>Thank you, <em>{confirmation.name || 'friend'}</em>.</h1>
            <p className="lead">
              We'll be in touch at <strong style={{color:'var(--text)'}}>{confirmation.email}</strong> within 24–48 hours.
              {confirmation.bird ? <> In the meantime, <strong style={{color:'var(--text)'}}>{confirmation.bird.name}</strong> has a soft hold under your name.</> : null}
            </p>
            <div className="hero-ctas">
              <button className="btn btn-primary" onClick={() => navigate('birds')}>See available birds</button>
              <button className="btn btn-outline" onClick={() => navigate('home')}>Back to home</button>
            </div>
          </section>
          <Footer />
        </main>
      )}

      {(route === 'about' || route === 'shipping') && (
        <main>
          <section className="hero" style={{ padding: '64px 48px 56px' }}>
            <span className="hero-eyebrow">{route === 'about' ? '🏡 Our family' : '✈️ Shipping & care'}</span>
            <h1>{route === 'about' ? <>Our <em>aviary</em></> : <>Shipping &amp; <em>care</em></>}</h1>
            <p className="lead">
              This page is part of the kit scaffold — drop in real content from
              the production WordPress site here, or ask the design agent to
              build it out.
            </p>
          </section>
          <section className="section">
            <div className="container">
              <TrustRow />
            </div>
          </section>
          <DarkCTA onClick={() => navigate('contact')} />
          <Footer />
        </main>
      )}
    </>
  );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
