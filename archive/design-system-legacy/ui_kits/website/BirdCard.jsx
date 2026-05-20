// BirdCard — product-like card for an available bird.
// Warm-tinted photo placeholder (real photo drops in later), green tag, Lora name, specs, price, CTA.
const BirdCard = ({ bird, onInquire }) => {
  return (
    <article className="card-std" data-screen-label={`BirdCard:${bird.name}`}>
      <div className="photo" aria-label={`${bird.name} — photo placeholder`}>
        <span>🦜</span>
        <span className="ph-note">Bird photo · drop in</span>
      </div>
      <div className="body">
        <div className="meta">
          <span className="tag-green">{bird.tag}</span>
        </div>
        <h3>{bird.name} <span style={{fontFamily:'var(--font-display)', fontStyle:'italic', fontWeight:400, color:'var(--mid)', fontSize:'18px'}}>— {bird.species}</span></h3>
        <p className="specs">
          {bird.age} · {bird.sex} · {bird.weaned ? 'Weaned onto pellet + fresh' : 'Still hand-feeding'}<br/>
          DNA cert · Vet-checked · Banded
        </p>
        <div className="price">{bird.price}</div>
      </div>
      <div className="foot">
        <span className="meta" style={{fontFamily:'var(--font-sans)', fontSize:12, color:'var(--light)'}}>
          Ready {bird.ready}
        </span>
        <a className="more" href="#" onClick={(e)=>{ e.preventDefault(); onInquire(bird); }}>
          Inquire about {bird.name.split(' ')[0]} →
        </a>
      </div>
    </article>
  );
};

window.BirdCard = BirdCard;
