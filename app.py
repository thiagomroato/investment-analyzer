from flask import Flask, request, jsonify
from comparator import analyze_stock

app = Flask(__name__)

@app.route('/analyze')
def analyze():
    ticker = request.args.get('ticker')

    results = analyze_stock_api(ticker)

    return jsonify(results)


def analyze_stock_api(ticker):
    from data_provider import get_stock_data, get_sector_stocks
    from comparator import calculate_score

    target = get_stock_data(ticker)
    peers = get_sector_stocks(target["setor"])

    results = []

    scores, final = calculate_score(target)
    results.append({"nome": ticker, "final": final, "tipo": "SUA ESCOLHA"})

    for p in peers:
        if p == ticker:
            continue
        try:
            stock = get_stock_data(p)
            scores, final = calculate_score(stock)
            results.append({"nome": p, "final": final, "tipo": "MERCADO"})
        except:
            continue

    results.sort(key=lambda x: x["final"], reverse=True)

    conclusao = (
        "Sua ação é a melhor do setor"
        if results[0]["nome"] == ticker
        else f"Melhor alternativa: {results[0]['nome']}"
    )

    return {
        "results": results,
        "conclusao": conclusao
    }


if __name__ == "__main__":
    app.run(debug=True)
