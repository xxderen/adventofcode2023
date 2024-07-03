import re
from collections import Counter

def calculate_total_winnings(hands, card_order, joker_transform=False):
    def sort_hand(hand):
        if joker_transform and 'J' in hand:
            non_joker_cards = [card for card in hand if card!= 'J']
            highest_card = max(non_joker_cards, key=lambda c: card_order.index(c), default='2')
            if hand.count('J') < 5:
                most_common_card = Counter(non_joker_cards).most_common(1)[0][0]
                hand = hand.replace('J', most_common_card)
            else:
                hand = hand.replace('J', highest_card)
        card_counts = Counter(hand)
        sorted_card_counts = tuple(sorted(card_counts.values(), reverse=True))
        card_order_indices = tuple(card_order.index(c) for c in hand)
        return sorted_card_counts, card_order_indices

    sorted_hands = sorted(hands.keys(), key=sort_hand)
    total_winnings = sum(w * (i + 1) for i, hand in enumerate(sorted_hands) for w in [hands[hand]])
    return total_winnings

def load_hands(file_path):
    with open(file_path, 'r') as file:
        hand_data = file.read()
        hand_pattern = r'(\w{5}) (\d+)'
        hands = re.findall(hand_pattern, hand_data)
        return {hand: int(score) for hand, score in hands}

file_path = 'day7_input.txt'
hands = load_hands(file_path)

print("Total Winnings Part 1:", calculate_total_winnings(hands, '23456789TJQKA'))
print("Total Winnings Part 2:", calculate_total_winnings(hands, 'J23456789TQKA', joker_transform=True))