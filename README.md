# 📊 Investment Analyzer

Aplicação web para análise de ações baseada em estratégias de grandes investidores.

## 🚀 Funcionalidades

- Lista de ações BR e EUA
- Input manual de métricas
- Score baseado em:
  - Peter Lynch
  - Warren Buffett
  - Ray Dalio
  - Thiago Nigro
  - Luiz Barsi
- Decisão automática: BUY / HOLD / SELL
- Histórico mensal salvo

## 🛠️ Tecnologias

- Python
- Flask
- SQLite

## ▶️ Como rodar

```bash
git clone https://github.com/seu-usuario/investment-analyzer.git
cd investment-analyzer

python -m venv venv
venv\Scripts\activate  # Windows

pip install -r requirements.txt

python app.py