# Console colors
PNK = '\033[95m'  # Pink (Head)
BLU = '\033[94m'  # Blue
CYN = '\033[96m'  # Cyan
DCN = '\033[36m'  # Dark cyan
GRN = '\033[92m'  # Green
YEL = '\033[93m'  # Yellow (Warning)
RED = '\033[91m'  # Red (Fail)
WHT = '\033[0m'  # White (plain)
BLD = '\033[1m'  # Bold
LIN = '\033[4m'  # Underline


def beauty_output(pos, neg):
    """Transforms NN result to readable format"""
    result = ' '
    result += rate_to_bar(pos)
    result += f' {GRN}' if pos > neg else f' {RED}'
    result += f' {round(max(pos, neg) * 100, 3):>6}% '
    result += 'P' if pos > neg else 'N'
    result += '\n'
    return result


def rate_to_bar(positive, size=20):
    """Returns colored bar of NN result"""
    l, f, s, r = '(=|)'
    positive_size = round(positive * size)
    negative_size = size - positive_size
    bar = WHT + l
    bar += BLD + GRN + f * positive_size
    bar += WHT + s
    bar += BLD + RED + f * negative_size
    bar += WHT + r
    return bar
