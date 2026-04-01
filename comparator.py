from data_provider import get_stock_data, get_sector_stocks
from models.lynch import lynch_score
from models.buffett import buffett_score
from models.dalio import dalio_score
from models.nigro import nigro_score
from models.barsi import barsi_score


def calculate_score(stock):
    scores = {
        "Lynch": lynch_score(stock),
        "Buffett": buffett_score(stock),
        "Dalio": dalio_score(stock),
        "Nigro": nigro_score(stock),
        "Barsi": barsi_score(stock),
    }

    final = sum(scores.values()) / len(scores)
    return scores, final


def analyze_stock(ticker):
    try:
        target = get_stock_data(ticker)
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        return

    peers_tickers = get_sector_stocks(target["setor"])

    results = []

    scores, final = calculate_score(target)
    results.append({
        "nome": ticker,
        "final": final,
        "tipo": "SUA ESCOLHA",
        "scores": scores
    })

    for t in peers_tickers:
        if t == ticker:
            continue

        try:
            stock = get_stock_data(t)
            scores, final = calculate_score(stock)

            results.append({
                "nome": t,
                "final": final,
                "tipo": "MERCADO",
                "scores": scores
            })
        except:
            continue

    results.sort(key=lambda x: x["final"], reverse=True)

    print("\n=== RANKING ===")
    for i, r in enumerate(results, 1):
        print(f"{i}º {r['nome']} ({r['tipo']}) - {r['final']:.2f}")

    best = results[0]

    print("\n=== CONCLUSÃO ===")
    if best["nome"] == ticker:
        print("✅ Sua ação está entre as melhores do setor")
    else:
        print(f"⚠️ Melhor alternativa encontrada: {best['nome']}")

    print("\n=== DETALHES ===")
    for r in results:
        print(f"\n{r['nome']}:")
        for k, v in r["scores"].items():
            print(f"{k}: {v:.2f}")
