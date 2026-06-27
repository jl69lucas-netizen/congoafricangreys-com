// ContactForm — fake-submit form mirroring the contact-us page.
// Pill selectors for bird type + shipping. Fields with proper labels. Square-radius primary submit.
const ContactForm = ({ defaultBird, onSubmitted }) => {
  const [name, setName] = React.useState('');
  const [email, setEmail] = React.useState('');
  const [phone, setPhone] = React.useState('');
  const [bird, setBird] = React.useState(defaultBird || 'congo');
  const [shipping, setShipping] = React.useState('air');
  const [home, setHome] = React.useState('');

  const submit = (e) => {
    e.preventDefault();
    onSubmitted({ name, email, phone, bird, shipping, home });
  };

  return (
    <form className="form-card" onSubmit={submit} data-screen-label="ContactForm">
      <div className="form-row">
        <div className="field">
          <label className="lbl">Your Name</label>
          <input value={name} onChange={e=>setName(e.target.value)} placeholder="Mark Benjamin" required />
        </div>
        <div className="field">
          <label className="lbl">Email</label>
          <input type="email" value={email} onChange={e=>setEmail(e.target.value)} placeholder="you@example.com" required />
        </div>
      </div>
      <div className="form-row">
        <div className="field">
          <label className="lbl">Phone</label>
          <input value={phone} onChange={e=>setPhone(e.target.value)} placeholder="(432) 555-0114" />
        </div>
        <div className="field">
          <label className="lbl">Bird of interest</label>
          <div className="pill-group">
            {[
              ['congo',  'Congo Grey'],
              ['timneh', 'Timneh Grey'],
              ['either', 'Either / no pref'],
            ].map(([v, l]) => (
              <div key={v} className={`pill-opt ${bird===v ? 'checked' : ''}`} onClick={()=>setBird(v)}>
                {l}
              </div>
            ))}
          </div>
        </div>
      </div>
      <div className="field" style={{marginBottom:16}}>
        <label className="lbl">How would you like to receive your bird?</label>
        <div className="pill-group">
          {[
            ['air',     '✈️ Air shipping'],
            ['local',   '🚗 Local delivery'],
            ['pickup',  '📍 Pickup in Midland'],
          ].map(([v, l]) => (
            <div key={v} className={`pill-opt ${shipping===v ? 'checked' : ''}`} onClick={()=>setShipping(v)}>
              {l}
            </div>
          ))}
        </div>
      </div>
      <div className="field" style={{marginBottom:24}}>
        <label className="lbl">Tell us about your home</label>
        <textarea value={home} onChange={e=>setHome(e.target.value)}
          placeholder="First-time parrot owner? Other pets? Schedule? We read every inquiry personally and reply within 24–48 hours." />
      </div>
      <button className="btn btn-primary-sq" type="submit">Send Inquiry →</button>
    </form>
  );
};

window.ContactForm = ContactForm;
