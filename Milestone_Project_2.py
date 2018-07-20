import random
import time

class Deck(object):
    import random
    numbers = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    suits = ['club','clover','diamond','heart']
    def __init__(self,deck=[]):
        self.deck = deck
    def create_deck(self):
        for num in self.numbers:
            for suit in self.suits:
                if num + " " + suit not in self.deck:
                    self.deck.append(num + " " + suit)
    def shuffle_deck(self):
        random.shuffle(self.deck)

class Player(Deck):
    def __init__(self,name,money=1000,rounds = 0,wins=0,losses=0,ties = 0,points = 0,amount = 0,bet = 0,hand1 = [],hand2 = []):
        Deck.__init__(self)
        self.name = name
        self.money = money
        self.rounds = rounds
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.points = points
        self.bet = bet
        self.hand1 = hand1
        self.hand2 = hand2
                
    def gain_money(self):
        self.money += self.amount

    def lose_money(self):
        self.money -= self.amount

    def win(self):
        self.wins += 1

    def lose(self):
        self.losses += 1

    def draw_card_p1(self):
        self.hand2.append(self.deck.pop())
    def draw_card_d(self):
        self.hand1.append(self.deck.pop())

    def count_points_p(self):
        for card in self.hand2:
            try:
                self.points += int(card[0:2])
            except:
                if card[0:4] == 'Jack':
                    self.points += 10
                elif card[0:5] == 'Queen':
                    self.points += 10
                elif card[0:4] == 'King':
                    self.points += 10
                elif card[0:3] == 'Ace':
                    if self.points + 11 <= 21:
                        self.points += 11
                    else:
                        self.points += 1
    def count_points_d(self):
        for card in self.hand1:
            try:
                self.points += int(card[0:2])
            except:
                if card[0:4] == 'Jack':
                    self.points += 10
                elif card[0:5] == 'Queen':
                    self.points += 10
                elif card[0:4] == 'King':
                    self.points += 10
                elif card[0:3] == 'Ace':
                    if self.points + 11 > 17 and self.points + 11 <= 21:
                        self.points += 11
                    else:
                        self.points += 1
        
    def reset_points(self):
        self.points = 0

    def dealer_play(self):
        while True:
            time.sleep(1.5)  
            dealer.reset_points()
            dealer.count_points_d()
            if dealer.points >= 17:
                print("\nThis is the dealer's hand: \n%s.\nSince dealer has 17 or more points, dealer stands" % dealer.hand1)
                break
            elif dealer.points < 17:
                dealer.draw_card_d()
                print("\nDealer draws a card. This is the dealer's hand: \n%s" % dealer.hand1)
                continue

playernames = []
while True:
    
    player1 = input("What is your name player 1?: ")
    playernames.append(player1)
    
    player2 = input("\nWhat is your name player 2?: \nif you do not wish to add players, type '1' \n")
    if player2 == '1':
        break
    playernames.append(player2)
    
    player3 = input("\nWhat is your name player 3?: \nif you do not wish to add players, type '1' \n")
    if player3 == '1':
        break
    playernames.append(player3)
    
    player4 = input("\nWhat is your name player 4?: \nif you do not wish to add players, type '1' \n")
    if player4 == '1':
        break
    playernames.append(player4)
    break


try:
    player1 = Player(playernames[0])
    player2 = Player(playernames[1])
    player3 = Player(playernames[2])
    player4 = Player(playernames[3])
except:
    pass

dealer = Player('Dealer')

def player1_play():    
    while True:
        decision = input("%s, do you want to stand or hit?: \n" % player1.name)
        player1.reset_points()
        if decision == 'stand' or decision == 'Stand' or decision == 'STAND':
            player1.count_points_p()
            
            if player1.points > 21:
                print("%s busted!\n" % player1.name)
                break
            break
        elif decision == 'hit' or decision == 'Hit' or decision == 'HIT':
            player1.draw_card_p1()
            print("%s is given a card.  This is your hand: %s\n" % (player1.name,player1.hand2))
            player1.count_points_p()
            
            if player1.points > 21:
                print("%s busted!\n" % player1.name)
                break
            continue
        else:
            print("Command not understood please try again.")
            continue

def play_game():
    
    again = 'y'

    while again == 'y' and player1.money >= 2:
        player1.hand2 = []
        dealer.hand1 = []

        deck1 = Deck()
        deck1.create_deck()
        deck1.shuffle_deck()

        while True:
            
            try:
                while True:
                    player1.bet = int(input("%s, please place your bet (between $2 and $500). " % player1.name))
                    if 2 <= player1.bet and player1.bet <= 500:
                        break
                    elif player1.bet < 2 or player1.bet > 500:
                        print("That is not a valid amount. Please enter a valid bet. ")
                        continue
                break
            except:
                print("Please enter a valid integer. ")

        time.sleep(1.5)    
        player1.draw_card_p1()
        print("%s is given a card.  This is your hand %s: \n%s\n" % (player1.name,player1.name,player1.hand2))
        time.sleep(1.5)
        dealer.draw_card_d()
        print("Dealer draws a card.  This is the dealer's hand: \n%s\n" % dealer.hand1)
        time.sleep(1.5)
        player1.draw_card_p1()
        print("%s is given a card.  This is your hand %s: \n%s\n" % (player1.name,player1.name,player1.hand2))
        time.sleep(1.5)
        dealer.draw_card_d()
        print("Dealer draws a card.\n")
        time.sleep(1)

        player1_play()
        dealer.dealer_play()
        time.sleep(1.5)  
        
        print("\n%s's points: %s" % (player1.name,player1.points))
        print("Dealer's points: %s" % dealer.points)

        time.sleep(1.5)          
        if player1.points > 21:
            player1.amount = player1.bet
            player1.lose_money()
            player1.lose()
            print("\n%s lost the round! %s loses %s dollars. " % (player1.name,player1.name,player1.amount))

        elif dealer.points < player1.points:
            if player1.points < 21:
                player1.amount = player1.bet
                player1.gain_money()
                player1.win()
                print("\n%s won the round! %s wins %s dollars. " % (player1.name,player1.name,player1.amount))
            elif player1.points == 21:
                player1.amount = 1.5 * player1.bet
                player1.gain_money()
                player1.win()
                print("\n%s won the round! %s wins %s dollars. " % (player1.name,player1.name,player1.amount))
        elif dealer.points > 21:
            if player1.points == 21:
                player1.amount = 1.5 * player1.bet
            if player1.points < 21:
                player1.amount = player1.bet
            player1.gain_money()
            player1.win()
            print("\n%s won the round! %s wins %s dollars. " % (player1.name,player1.name,player1.amount))
        elif dealer.points == player1.points:
            player1.ties += 1
            print("\nThis round is a push/tie! %s wins $0 this round. " % (player1.name))
        elif 21 >= dealer.points > player1.points:
            player1.amount = player1.bet
            player1.lose_money()
            player1.lose()
            print("\n%s lost the round! %s loses %s dollars. " % (player1.name,player1.name,player1.amount))

        player1.rounds += 1

        print("\n%s's money: %s" % (player1.name, player1.money))
        print("%s's rounds played: %s" % (player1.name,player1.rounds))
        print("%s's wins: %s" % (player1.name,player1.wins))
        print("%s's losses: %s" % (player1.name,player1.losses))
        print("%s's ties: %s" % (player1.name,player1.ties))
        while True:
            try:
                while True:
                    if player1.money < 2:
                        print("\n%s, You do not have enough money to continue playing.  Thank you for playing!" % player1.name)
                        again = 'no_money'
                        break
                    again = input("\nDo you want to play again? (y/n): ")
                    if again == 'y':
                        break
                    elif again == 'n':
                        break
                    else:
                        print("\nCommand not recognized.")
                        continue
                break
            except:
                continue
play_game()
