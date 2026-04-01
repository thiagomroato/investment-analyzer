from comparator import analyze_stock

def main():
    print("=== ANALISADOR DE AÇÕES ===")
    ticker = input("Digite o ticker (ex: PETR4): ").upper()
    analyze_stock(ticker)

if __name__ == "__main__":
    main()
