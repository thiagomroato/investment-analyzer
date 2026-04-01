def lynch_score(pl, growth):
    if growth == 0:
        return 0
    peg = pl / growth
    return 10 if peg < 1 else 5 if peg < 2 else 0

def buffett_score(roe, debt):
    score = 0
    if roe > 15:
        score += 5
    if debt < 0.5:
        score += 5
    return score

def barsi_score(dy):
    if dy > 6:
        return 10
    elif dy > 3:
        return 5
    return 0

def nigro_score(growth):
    return 10 if growth > 10 else 5 if growth > 5 else 0

def dalio_score(debt):
    return 10 if debt < 0.3 else 5 if debt < 0.6 else 0

def final_decision(score):
    if score >= 35:
        return "BUY"
    elif score >= 20:
        return "HOLD"
    return "SELL"