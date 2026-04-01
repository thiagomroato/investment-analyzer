document.addEventListener("DOMContentLoaded", () => {
  const select = document.getElementById("asset");

  assets.forEach((a, i) => {
    const option = document.createElement("option");
    option.value = i;
    option.textContent = `${a.name} (${a.ticker})`;
    select.appendChild(option);
  });
});

function analyze() {
  const assetIndex = document.getElementById("asset").value;

  const pl = parseFloat(document.getElementById("pl").value);
  const roe = parseFloat(document.getElementById("roe").value);
  const dy = parseFloat(document.getElementById("dy").value);
  const debt = parseFloat(document.getElementById("debt").value);
  const growth = parseFloat(document.getElementById("growth").value);

  const score =
    lynchScore(pl, growth) +
    buffettScore(roe, debt) +
    barsiScore(dy) +
    nigroScore(growth) +
    dalioScore(debt);

  const decision = finalDecision(score);

  document.getElementById("result").innerText =
    "Decisão: " + decision + " | Score: " + score;

  saveData(assetIndex, pl, roe, dy, debt, growth, decision);
}

function saveData(assetIndex, pl, roe, dy, debt, growth, decision) {
  const history = JSON.parse(localStorage.getItem("history")) || [];

  history.push({
    asset: assets[assetIndex].ticker,
    pl,
    roe,
    dy,
    debt,
    growth,
    decision,
    date: new Date().toLocaleDateString(),
  });

  localStorage.setItem("history", JSON.stringify(history));
}