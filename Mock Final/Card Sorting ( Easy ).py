from functools import cmp_to_key

def card_value(card):
    rank_order = {"K": 13, "Q": 12, "J": 11, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "1": 1, "A": 14}
    return rank_order[card[:-1]]

def compare_cards(card1, card2):
    suit_order = {"S": 1, "H": 2, "D": 3, "C": 4}
    if suit_order[card1[-1]] != suit_order[card2[-1]]:
        return suit_order[card1[-1]] - suit_order[card2[-1]]
    return card_value(card2) - card_value(card1)

def calculate_score(cards):
    score = 0
    for card in cards:
        rank, suit = card[:-1], card[-1]
        if card == "2C" or card == "QS":
            score += 50
        elif rank == "A":
            score += 15
        elif rank in ["10", "J", "K", "Q"] and card != "QS":
            score += 10
        elif rank in ["2", "3", "4", "5", "6", "7", "8", "9", "1"] and card != "2C":
            score += 5
    return score

def sort_and_rank_players(players):
    sorted_players = []
    for name, cards in players:
        sorted_cards = sorted(cards, key=cmp_to_key(compare_cards))
        score = calculate_score(sorted_cards)
        sorted_players.append((name, sorted_cards, score))
    sorted_players.sort(key=lambda x: x[2], reverse=True)
    return sorted_players

n = int(input().strip())
m = int(input().strip())

players = []
for _ in range(n):
    name, cards = eval(input().strip())
    players.append((name, cards))

sorted_players = sort_and_rank_players(players)

for name, sorted_cards, score in sorted_players:
    print(f"{name} -> {score} -> {sorted_cards}")

