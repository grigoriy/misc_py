import random

class Card(object):
    def __init__(self, value, suit):
        '''
        value, suit: strings
        '''
        self.value = value
        self.suit = suit

    def __str__(self):
        return self.value + self.suit

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in ('h', 'd', 'c', 's'):
            for value in 'AKQJT98765432':
                self.cards.append(Card(value, suit))

    def shuffle(self):
        return random.shuffle(self.cards)

    def __str__(self):
        result = ''
        for card in self.cards:
            result += str(card) + ' '
        return result

class PokerPlayer(object):
    def __init__(self, vpip = 0.15, pre_r = 0.13, pre_3b = 0.06, pre_ft_3b = 65.0, \
                 pst_agr = 0.35, f_cb = 0.65, t_cb = 0.5, r_cb = 0.5, f_ft_cb = 0.5):
        self.vpip = vpip
        self.pre_r = pre_r
        self.pre_3b = pre_3b
        self.pre_ft_3b = pre_ft_3b
        self.pst_agr = pst_agr
        self.f_cb = f_cb
        self.t_cb = t_cb
        self.r_cb = r_cb
        self.f_ft_cb = f_ft_cb
