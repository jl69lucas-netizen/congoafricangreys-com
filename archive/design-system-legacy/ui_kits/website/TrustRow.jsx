// TrustRow — horizontal row of pill chips with documentation + service guarantees.
const TrustRow = ({ items }) => {
  const defaults = [
    { ico: '✅', em: 'USDA-Licensed', text: 'Breeder' },
    { ico: '✅', em: 'CITES',         text: 'Appendix II Documented' },
    { ico: '✅', em: 'DNA-Sexed',     text: '& Vet-Certified' },
    { ico: '✈️', em: 'Ships',         text: 'Nationwide from $185' },
    { ico: '🕐', em: '24–48 hr',      text: 'Response Guarantee' },
  ];
  const data = items || defaults;
  return (
    <div className="trust-row" data-screen-label="TrustRow">
      {data.map((t, i) => (
        <span className="trust-pill" key={i}>
          <span className="ico">{t.ico}</span>
          <span><span className="em">{t.em}</span> {t.text}</span>
        </span>
      ))}
    </div>
  );
};

window.TrustRow = TrustRow;
