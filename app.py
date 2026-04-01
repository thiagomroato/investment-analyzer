from flask import Flask, render_template, request
from models import create_tables, connect
from strategies import *
from seed import seed_assets

app = Flask(__name__)
create_tables()

# Popular banco (executa uma vez)
try:
    seed_assets()
except:
    pass

@app.route("/", methods=["GET", "POST"])
def index():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, ticker FROM assets")
    assets = cursor.fetchall()

    decision = None

    if request.method == "POST":
        asset_id = request.form["asset"]

        pl = float(request.form["pl"])
        roe = float(request.form["roe"])
        dy = float(request.form["dy"])
        debt = float(request.form["debt"])
        growth = float(request.form["growth"])

        score = (
            lynch_score(pl, growth) +
            buffett_score(roe, debt) +
            barsi_score(dy) +
            nigro_score(growth) +
            dalio_score(debt)
        )

        decision = final_decision(score)

        cursor.execute("""
        INSERT INTO metrics (asset_id, pl, roe, dy, debt, growth, date)
        VALUES (?, ?, ?, ?, ?, ?, DATE('now'))
        """, (asset_id, pl, roe, dy, debt, growth))

        conn.commit()

    conn.close()

    return render_template("index.html", assets=assets, decision=decision)

if __name__ == "__main__":
    app.run(debug=True)