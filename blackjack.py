import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
player_hand = []
dealer_hand = []


def deal_cards():  # Handing out cards to the dealer and player in the proper order
    random.shuffle(deck)
    card = deck.pop()
    player_hand.append(card)
    card = deck.pop()
    dealer_hand.append(card)
    card = deck.pop()
    player_hand.append(card)
    card = deck.pop()
    dealer_hand.append(card)


def hand_totals(hand):  # Sums the total of the current hand that is provided either the dealer or the player
    total = 0
    for ace in hand:
        if ace == 'A':  # Rearrange the hand so that the Ace is last and the total is correctly computed
            hand.append(hand.pop(hand.index('A')))
    for card in hand:
        if card == 'J' or card == 'Q' or card == 'K':
            total += 10
        elif card == 'A':
            if total < 11:
                total += 11
            else:
                total += 1
        else:
            total += card
    return total


def hit_card(hand):  # If a player decides to hit and if the dealer is under 17
    random.shuffle(deck)
    card = deck.pop()
    hand.append(card)
    print("The next card was a " + str(card))


def game():  # The entire game of Blackjack for one player against the dealer
    choice = '-'
    deal_cards()
    print("Time to play some Blackjack!")
    print()
    print("The dealer is showing " + str(dealer_hand[0]))  # Showing just one of the dealer's cards
    print()
    print("You currently have " + str(player_hand[0]) + " and a " + str(player_hand[1]))  # both player cards
    print("Your hand total is " + str(hand_totals(player_hand)))  # Show player total
    if hand_totals(player_hand) == 21:  # If player gets a blackjack on initial cards
        print('Black jack! You win!')
        play_again()
    while choice != 'q'.casefold():
        print()
        choice = input("What would you like to do? (Press h for hit, s for stay and q for quit): ")
        print()
        if choice == 's'.casefold():
            print("The dealer has " + str(dealer_hand[0]) + " and " + str(dealer_hand[1]) + " for a total of " +
                  str(hand_totals(dealer_hand)))
            while hand_totals(dealer_hand) < 17:
                hit_card(dealer_hand)
                print("The dealer's new total is " + str(hand_totals(dealer_hand)))
            if hand_totals(dealer_hand) > 21:
                print()
                print("The dealer has busted! You win!")
                play_again()
            elif 17 <= hand_totals(dealer_hand) < 21:
                if hand_totals(dealer_hand) < hand_totals(player_hand):  # Player win
                    print("You win!")
                    play_again()
                elif hand_totals(player_hand) < hand_totals(dealer_hand):  # Player loses
                    print("You lose!")
                    play_again()
                elif hand_totals(player_hand) == hand_totals(dealer_hand):  # A tie game
                    print("It's a tie!")
                    play_again()
            elif hand_totals(dealer_hand) == 21:  # Dealer black jack
                print("Sorry you lose! The dealer got blackjack!")
                play_again()
        elif choice == 'h':  # If player decides to hit
            hit_card(player_hand)
            hand_totals(player_hand)
            if hand_totals(player_hand) == 21:  # If the player gets blackjack on hit
                print("You win! You got black jack!")
                play_again()
            print("Your total is now " + str(hand_totals(player_hand)))
            if hand_totals(player_hand) > 21:  # Player bust
                print()
                print("Sorry you lose! You busted!")
                play_again()


def play_again():  # Checking if the player would like to play again
    option = input("Do you want to play again? y/n")
    global deck
    if option == 'y':  # Clearing the hands and resetting the deck to play again
        player_hand.clear()
        dealer_hand.clear()
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
        game()
    else:
        exit()


game()
