def record_to_win_percentage(w, L, d):
    """If win is worth 10, draw worth 4, loss worth 1
    loss worth 1 because even winless teams have a chance to win in the future"""
    best = (w + L + d)*3
    if best == 0: return 0
    score = (w*3.) + (d)
    return score/best

def norm_percentages(percent1, percent2):
    """returns percent1, percent2, normed"""
    total = percent1 + percent2
    return (percent1/total, percent2/total)

