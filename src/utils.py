def score_to_grade(score):
    if score >= 8:
        return 'A'
    elif score >= 7:
        return 'B'
    elif score >= 5:
        return 'C'
    elif score >= 4:
        return 'D'
    else:
        return 'F'
