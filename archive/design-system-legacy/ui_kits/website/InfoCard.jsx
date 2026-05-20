// InfoCard — white card with forest-green header, list of icon+key+value rows. Used for contact info, visit info, shipping info.
const InfoCard = ({ title, sub, rows }) => (
  <div className="info-card" data-screen-label={`InfoCard:${title}`}>
    <div className="hdr">
      <h3>{title}</h3>
      <p>{sub}</p>
    </div>
    <div className="body">
      <ul>
        {rows.map((r, i) => (
          <li key={i}>
            <span className="ico">{r.ico}</span>
            <span style={{flex:1}}>
              <span className="key">{r.key}</span>
              <span className="val">{r.val}</span>
            </span>
          </li>
        ))}
      </ul>
    </div>
  </div>
);

window.InfoCard = InfoCard;
