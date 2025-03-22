import art
import random

# Initialise a deck of cards
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def main():
    while input("Do you want to play a game of Blackjack?(Type y/n): ").lower() == "y":
        print(art.logo)

        # Deal two cards each
        player_cards = deal(2)
        computer_cards = deal(2)

        # If player gets 21 right away - they win, game over
        if sum(player_cards) == 21:
            show_hand(player_cards, computer_cards)
            print("Blackjack! You got 21. You win! :)")
            continue

        show_hand(player_cards, computer_cards)

        # Ask if player wants another card
        while sum(player_cards) < 21:
            another = input("Would you like another card (type y/n): ").lower()
            if another == "y":
                player_cards += deal(1)
                ace(player_cards)
                show_hand(player_cards, computer_cards)
            else:
                break

        if sum(player_cards) > 21:
            print("You went over. You lose :(")
            continue

        # Dealer's turn
        while sum(computer_cards) < 17:
            computer_cards += deal(1)
            ace(computer_cards)

        # Print the final result
        final_result(player_cards, computer_cards)


def deal(n):
    '''Deal n cards from the deck'''
    return [random.choice(cards) for _ in range(n)]

def ace(player_cards):
    '''Convert ace from 11 to 1 if score is over 21'''
    while sum(player_cards) > 21 and 11 in player_cards:
        ace_index = player_cards[2:].index(11) + 2
        player_cards[ace_index] = 1

def show_hand(player, computer):
    '''Display players hand and computer's first card'''
    print(f"Your cards: {player}, current score: {sum(player)}")
    print(f"Computer's first card: {computer[0]}")

def final_result(player, computer):
    '''Calculate and print the final result'''
    print(f"Your final hand: {player}, final score: {sum(player)}")
    print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
    if sum(computer) > 21 or sum(player) > sum(computer):
        print("You win! :)")
    elif sum(computer) > sum(player):
        print("You lose :(")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    main()