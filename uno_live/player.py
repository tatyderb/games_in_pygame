from uno_live.cardlist import Hand


class Player:
    def __init__(self, name, cards):
        self.name = name
        self.hand = Hand(cards)

    def __repr__(self):
        return f'{self.name}: {self.hand}'

    def get_payable_card(self, top):
        """Возвращает ОДНУ карту, которую сыграли на top или None, если играть нельзя (нет подходящих карт)"""
        card_list = self.hand.playable_list(top)
        if not card_list:
            # подходящих карт нет, возвращаем None
            return None
        else:
            # играем первую в этом списке, потому что мне лень писать код для поиска лучшей карты
            removable_card = card_list[0]
            self.hand.remove(removable_card)
            return removable_card

    def add_card(self, card):
        self.hand.add(card)
