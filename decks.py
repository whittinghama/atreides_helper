class SpiceDeck:
    def __init__(self):
        self.card_types = {"Spice" : 15,
                           "Worm" : 6}
        
        self.deck = self._generate_deck()
        self.drawn_cards = []

    def _generate_deck(self):
        deck = []
        for card_type, count in self.card_types.items():
            deck.extend([card_type] * count)
        return deck
    
    def draw_card(self, card: str):
        if not self.deck:
            raise ValueError("All cards have been drawn")
        if card:
            if card in self.deck:
                self.deck.remove(card)
            else:
                raise ValueError("Card not in deck")
        else:
            raise ValueError("Card must be specified")
        self.drawn_cards.append(card)

    def get_stats(self):
        stats = {}
        for card_type in self.card_types.keys():
            prob = self.probability_of_card(card_type)
            prob = round(prob * 100, 2)
            stats[card_type] = prob
        return stats


    def probability_of_card(self, card_type):
        drawn_count = self.drawn_cards.count(card_type)
        total_count = self.card_types[card_type]
        if drawn_count >= total_count:
            return 0
        remaining = len(self.deck)
        remaining_known = sum(1 for card in self.deck if card == card_type)
        return remaining_known / remaining if remaining > 0 else 0