from deck_of_cards import deck_of_cards

print("Yes, here we go!")

dealer_hand = []
user_hand = []

i = 0
while (i<2):
    dealer_hand.append(deck_of_cards.DeckOfCards().give_random_card())
    user_hand.append(deck_of_cards.DeckOfCards().give_random_card())
    i+=1

print("In your hand, you will find:")
for card in user_hand:
    print(card.name)

print("And the dealer is showing a ")
print(dealer_hand[1].name)

user_response = input("Would you like to hit or stick? ")

while (user_response == "hit"):
    user_hand.append(deck_of_cards.DeckOfCards().give_random_card())
    print("In your hand, you will find:")
    for card in user_hand:
        print(card.name)
    user_response = input("Would you like to hit or stick? ")