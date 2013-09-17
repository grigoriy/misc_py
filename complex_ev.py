def complex_4b_ev(FEq, Eq, DM = 1.5, OR = 2.5, RR = 7.0, RRR = 15.0, stack = 45.0):
    '''
    FEq: float, 0.0 <= FEq <= 1.0, fold-equity of Hero's 4-bet
    Eq: float, 0.0 <= FEq <= 1.0, Hero's equity vs Villain's 5-bet range
    DM: initial dead money
    OR: size of Hero's open-raise
    RR: size of Villain's 3-bet
    RRR: size of Hero's 4-bet
    stack: effective stack

    returns: tuple, total expected values of Hero's 4-bet/call and 4-bet/fold
    '''
    # amounts for Hero to make 4-bet and to call after Villain's 5-bet respectively
    real_RRR = RRR - OR
    call_RRRR = stack - RRR
    # pots after Villain's 3-bet and 5-bet respectively
    pot_RR = DM + OR + RR
    pot_RRRR = DM + stack * 2 - call_RRRR

    def helper(FEq, Eq, real_RRR, call_RRRR, pot_RR, pot_RRRR):
        # expected value of Hero's 4-bet/call
        EV_call = FEq * pot_RR + (1.0 - FEq) * (Eq * pot_RRRR + (1 - Eq) * (0 - call_RRRR))
        # expected value of Hero's 4-bet/fold
        EV_fold = FEq * pot_RR + (1.0 - FEq) * (0 - real_RRR)

        return (round(EV_call, 2), round(EV_fold, 2))

    return helper(FEq, Eq, real_RRR, call_RRRR, pot_RR, pot_RRRR)
