"""Simple Poker implementation."""


class Card:
    """A card in a poker game."""

    def __init__(self, value, suit):
        """Initialze Card."""
        self.value = value
        self.suit = suit

    def __repr__(self):
        """
        Return a string representation of the card.

        "{value} of {suit}"
        "2 of hearts" or "Q of spades"

        """
        return f"{self.value} of {self.suit}"

class Hand:
    """The hand in a poker game."""

    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        """Initialize Hand."""
        self.cards = [] 

    def can_add_card(self, card: Card) -> bool:
        """ Check if the card is valid and can be added to the hand. """
        if card.value not in self.values or card.suit not in self.suits:
            return False
        for c in self.cards:
            if c.value == card.value and c.suit == card.suit:
                return False
        if len(self.cards) >= 5:
            return False
        return True

    def add_card(self, card: Card):
        """Add a valid card to the hand."""
        if self.can_add_card(card):
            self.cards.append(card)
        else:
            print(f"Cannot add {card}. Invalid card or hand is full.")

    def can_remove_card(self, card: Card):
        """Check if a card can be removed from the hand."""
        return card in self.cards

    def remove_card(self, card: Card):
        """Remove a card from the hand."""
        if self.can_remove_card(card):
            self.cards.remove(card)

    def get_cards(self):
        """Return a list of cards in the hand."""
        return self.cards

    def is_straight(self):
        """ Check if the hand is a straight. """
        values = [card.value for card in self.cards]
        values.sort(key=lambda v: self.values.index(v))
        for i in range(1, len(values)):
            if self.values.index(values[i]) != self.values.index(values[i - 1]) + 1:
                return False
        return True

    def is_flush(self):
        """ Check if the hand is a flush. """
        suits = [card.suit for card in self.cards]
        return len(set(suits)) == 1 

    def is_straight_flush(self):
        """ Check if the hand is a straight flush. """
        return self.is_straight() and self.is_flush()

    def is_full_house(self):
        """ Check if the hand is a full house. """
        values = [card.value for card in self.cards]
        value_counts = {value: values.count(value) for value in values}
        return sorted(value_counts.values()) == [2, 3]

    def is_four_of_a_kind(self):
        """ Check if the hand is four of a kind. """
        values = [card.value for card in self.cards]
        value_counts = {value: values.count(value) for value in values}
        return 4 in value_counts.values()

    def is_three_of_a_kind(self):
        """ Check if the hand is three of a kind. """
        values = [card.value for card in self.cards]
        value_counts = {value: values.count(value) for value in values}
        return 3 in value_counts.values()

    def is_pair(self):
        """ Check if the hand is a pair. """
        values = [card.value for card in self.cards]
        value_counts = {value: values.count(value) for value in values}
        return 2 in value_counts.values()

    def get_hand_type(self):
        """ Return the type of the hand. """
        if len(self.cards) < 5:
            return None
        if self.is_straight_flush():
            return "straight flush"
        elif self.is_flush():
            return "flush"
        elif self.is_straight():
            return "straight"
        elif self.is_full_house():
            return "full house"
        elif self.is_four_of_a_kind():
            return "four of a kind"
        elif self.is_three_of_a_kind():
            return "three of a kind"
        elif self.is_pair():
            return "pair"
        else:
            return "high card"

    def __repr__(self):
        """ Return a string representation of the hand. """
        hand_type = self.get_hand_type()
        if hand_type:
            return f"I got a {hand_type} with cards: {', '.join(str(card) for card in self.cards)}"
        else:
            return f"I'm holding {', '.join(str(card) for card in self.cards)}"

if __name__ == "__main__":
    hand = Hand()
    cards = [Card("2", "diamonds"), Card("4", "spades"), Card("5", "clubs"), Card("3", "diamonds"), Card("6", "hearts")]
    [hand.add_card(card) for card in cards]
    print(hand.get_hand_type())

    hand = Hand()
    cards = [Card("10", "diamonds"), Card("2", "diamonds"), Card("A", "diamonds"), Card("6", "diamonds"), Card("9", "diamonds")]
    [hand.add_card(card) for card in cards]
    print(hand.get_hand_type())

    hand = Hand()
    cards = [Card("A", "hearts"), Card("A", "clubs"), Card("A", "spades"), Card("A", "diamonds"), Card("9", "diamonds")]
    [hand.add_card(card) for card in cards]
    print(hand.get_hand_type()) 