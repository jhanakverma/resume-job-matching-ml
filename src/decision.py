def make_decision(score):
    """
    Decide resume status based on score
    """

    if score >= 0.70:
        return "SHORTLIST"
    elif score >= 0.50:
        return "REVIEW"
    else:
        return "REJECT"
