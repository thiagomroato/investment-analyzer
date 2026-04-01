function lynchScore(pl, growth) {
  if (growth === 0) return 0;
  const peg = pl / growth;
  return peg < 1 ? 10 : peg < 2 ? 5 : 0;
}

function buffettScore(roe, debt) {
  let score = 0;
  if (roe > 15) score += 5;
  if (debt < 0.5) score += 5;
  return score;
}

function barsiScore(dy) {
  if (dy > 6) return 10;
  if (dy > 3) return 5;
  return 0;
}

function nigroScore(growth) {
  return growth > 10 ? 10 : growth > 5 ? 5 : 0;
}

function dalioScore(debt) {
  return debt < 0.3 ? 10 : debt < 0.6 ? 5 : 0;
}

function finalDecision(score) {
  if (score >= 35) return "BUY";
  if (score >= 20) return "HOLD";
  return "SELL";
}