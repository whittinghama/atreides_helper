from maps import cardMap

class TreacheryDeck:

    def __init__(self):
        self.card_types = {"tcard_weap_poi" : 4,
                           "tcard_weap_pro" : 4,
                           "tcard_weap_las" : 1,
                           "tcard_def_poi" : 4,
                           "tcard_def_pro" : 4,
                           "tcard_spec_kara" : 2,
                           "tcard_spec_hero" : 3,
                           "tcard_spec_move" : 1,
                           "tcard_spec_rev" : 1,
                           "tcard_spec_storm" : 1,
                           "tcard_spec_truth" : 2,
                           "tcard_spec_wall" : 1,
                           "tcard_worthless" : 5}
        
        self.deck = self._generate_deck()
        self.drawn_cards = []
        self.unknown_cards = 0

    def _generate_deck(self):
        deck = []
        for card_type, count in self.card_types.items():
            deck.extend([card_type] * count)
        return deck

    def draw_card(self, known=True, card=None):
        if not self.deck and self.unknown_cards == 0:
            raise ValueError("All cards have been drawn")
        if known:
            if card:
                if card in self.deck:
                    self.deck.remove(card)
                elif self.unknown_cards > 0:
                    self.unknown_cards -= 1
                else:
                    raise ValueError("Card not in deck, and can't be unknown")
            else:
                raise ValueError("If card is known, card must be specified")
            self.drawn_cards.append(card)
        else:
            self.unknown_cards += 1

    def discard_card(self, card):
        if card not in self.drawn_cards:
            if self.unknown_cards > 0:
                self.unknown_cards -= 1
            else:
                raise ValueError("Cannot discard, card wasn't drawn and can't be unknown")
        else:
            self.drawn_cards.remove(card)

    def get_stats(self):
        stats = {}
        stats["Remaining Cards"] = self.remaining_cards()
        stats["Unknown Cards"] = self.unknown_cards
        for card_type in self.card_types.keys():
            prob = self.probability_of_card(card_type)
            prob = round(prob * 100, 2)
            stats[cardMap[card_type]] = prob
        return stats

    def remaining_cards(self):
        return len(self.deck) - self.unknown_cards

    def drawn_cards_count(self):
        return len(self.drawn_cards) + self.unknown_cards

    def reset_deck(self):
        self.deck = self._generate_deck()
        self.drawn_cards = []
        self.unknown_cards = 0

    def probability_of_card(self, card_type):
        drawn_count = self.drawn_cards.count(card_type)
        total_count = self.card_types[card_type]
        if drawn_count >= total_count:
            return 0
        remaining = self.remaining_cards()
        remaining_known = sum(1 for card in self.deck if card == card_type)
        return remaining_known / remaining if remaining > 0 else 0

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
        stats = {
            "Spice" : self.probability_of_card("Spice"),
            "Worm" : self.probability_of_card("Worm")
        }
        return stats

    def probability_of_card(self, card_type):
        drawn_count = self.drawn_cards.count(card_type)
        total_count = self.card_types[card_type]
        if drawn_count >= total_count:
            return 0
        remaining = self.remaining_cards()
        remaining_known = sum(1 for card in self.deck if card == card_type)
        return remaining_known / remaining if remaining > 0 else 0