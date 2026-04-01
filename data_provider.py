import fundamentus

def safe_float(value, default=0.0):
    try:
        return float(value)
    except:
        return default

def get_stock_data(ticker):
    df = fundamentus.get_papel(ticker)
    data = df.to_dict()

    return {
        "nome": ticker,
        "roe": safe_float(data["roe"][ticker]),
        "divida_patrimonio": safe_float(data["divida_liquida_patrimonio"][ticker]),
        "margem_liquida": safe_float(data["margem_liquida"][ticker]),
        "dy": safe_float(data["dy"][ticker]),
        "lucro_crescimento": safe_float(data.get("crescimento_receita", {}).get(ticker, 10)),
        "anos_dividendos": 5,
        "setor": data["setor"][ticker],
        "volatilidade": 20
    }

def get_sector_stocks(setor):
    df = fundamentus.get_resultado()
    setor_df = df[df["setor"] == setor]
    return list(setor_df.index)[:5]
