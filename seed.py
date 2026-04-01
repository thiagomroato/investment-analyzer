from models import connect

def seed_assets():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM assets")
    count = cursor.fetchone()[0]

    if count > 0:
        return

    assets = [
        ("Petrobras", "PETR4", "Energia", "BR"),
        ("Vale", "VALE3", "Mineração", "BR"),
        ("Itaú", "ITUB4", "Financeiro", "BR"),
        ("Banco do Brasil", "BBAS3", "Financeiro", "BR"),
        ("WEG", "WEGE3", "Industrial", "BR"),
        ("Ambev", "ABEV3", "Consumo", "BR"),
        ("Taesa", "TAEE11", "Energia", "BR"),
        ("BB Seguridade", "BBSE3", "Financeiro", "BR"),

        ("Apple", "AAPL", "Tecnologia", "US"),
        ("Microsoft", "MSFT", "Tecnologia", "US"),
        ("Google", "GOOGL", "Tecnologia", "US"),
        ("Amazon", "AMZN", "Consumo", "US"),
        ("Coca-Cola", "KO", "Consumo", "US"),
        ("Johnson & Johnson", "JNJ", "Saúde", "US"),
        ("Berkshire Hathaway", "BRK.B", "Financeiro", "US"),
        ("Tesla", "TSLA", "Automotivo", "US"),
    ]

    cursor.executemany("""
    INSERT INTO assets (name, ticker, sector, market)
    VALUES (?, ?, ?, ?)
    """, assets)

    conn.commit()
    conn.close()