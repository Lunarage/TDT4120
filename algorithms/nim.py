"""
    NIM
    Start with N pieces
    Two players takes turns taking pieces
    A player must take at least one stick and at most 7 pieces
    The player who takes the last piece loses
"""


def take_pieces(n_pieces):
    """
        A winning strategy given n pieces are left
    """
    return (n_pieces-1) % 8 if (n_pieces-1) % 8 > 0 else 1
