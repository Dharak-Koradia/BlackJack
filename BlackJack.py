#!/usr/bin/env python
# coding: utf-8

# **The only change is that the** `player_chips` **is a *GLOBAL* variable, now.**<br>
# **This means that everytime the player bets, the total chips will be evaluated from the last game -- whether the player won or lost.**<br><br>
# **In short, the total chips will be counted like real chips**<br><br>

# In[3]:


import random

# Global variable
playing = True
player_busted = False


# In[4]:


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':1}


# In[5]:


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.card_value = values[rank]
        
    # overloading the print function for the class.
    def __str__(self):
        return self.rank + " of " + self.suit


# In[6]:


class Deck:
    
    def __init__(self):
        
        self.deck = []
        
        for suit in suits:
            for rank in ranks:
                # create a new card
                created_card = Card(suit,rank)
                # add it to the deck
                self.deck.append(created_card)
                
                
    def __str__(self):
        return f"Size of the deck: {len(self.deck)}\nThe first card is: {self.deck[0]}.\nThe last card is: {self.deck[-1]}."
        
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal_one(self):
        return self.deck.pop()  # pops the last element in the list


# In[7]:
# new_deck = Deck()

# In[8]:
# print(new_deck)


# ## Hand class

# In[9]:


class Hand:
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        self.total_value = 0
        
    def add_card(self,card):
        
        self.cards.append(card)
        self.value = card.card_value
        
        if self.value == 11:
            self.aces += 1
            
        self.total_value += self.value
        
    
    # def adjust_for_ace(self):
    
    
    
    def printCards(self):
        for card in self.cards:
            print(card)
        


# In[10]:
#player_hand = Hand()


# In[11]:
#player_hand.add_card(Card("Hearts","Five"))


# In[12]:
#player_hand.value


# In[13]:
#print(player_hand.cards[0])


# In[14]:
#player_hand.total_value


# In[15]:
#player_hand.add_card(Card("Spades","Ace"))


# In[16]:
#player_hand.printCards()


# In[17]:
#player_hand.total_value


# In[18]:
#player_hand.aces = 0


# In[19]:
#player_hand.aces


# In[ ]:

# In[20]:


class Chips:
    
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        self.bet = 0   # once total is calculated, the bet should be back to 0
        
    def lose_bet(self):
        self.total -= self.bet
        self.bet = 0  # once total is calculated, the bet should be back to 0
    
    def printChips(self):
        print(f"Total: ${self.total}")
        print(f"Bet: ${self.bet}")


# In[21]:
#some_chips = Chips()


# In[22]:
#some_chips.printChips()


# In[23]:
#some_chips.bet = 50


# In[24]:
#some_chips.printChips()


# In[25]:
#some_chips.lose_bet()


# In[26]:
#some_chips.printChips()


# In[27]:
#some_chips.win_bet()


# In[28]:
#some_chips.printChips()


# In[ ]:





# In[29]:


def take_bet(total_balance):
        
    boolVal = True
        
    print("------------------------")
    print(f"Total: ${total_balance}")
    print("------------------------")
        
    while boolVal:        
        try:
            user_bet = int(input("Please enter the bet amount: $"))
        except:
            print("Sorry, please enter an integer bet.")
            continue
        else:
            if user_bet > total_balance:
                print("Sorry, bet amount doesn't comply with the total amount.")
                continue
            else:
                print(f"\nThe bet amount is ${user_bet}.\n")
                return user_bet


# In[30]:
#chips_obj = Chips()


# In[31]:
#type(chips_obj)


# In[32]:


#take_bet(chips_obj.total)


# [Hand class](http://localhost:8888/notebooks/Documents/PythonCourse-1/Section-11--Milestone_Project_2/BlackJack.ipynb#Hand-class)<br>

# In[33]:


def hit(deckObj,handObj):
    
    # remove one card from the deck
    one_card = deckObj.deal_one()
    # add it to the hand (or table)
    handObj.add_card(one_card)
    
    '''
    if handObj.total_value > 21:
        #print("\nA bust has occurred!\n")
        #print("The cards that made the bust: ")
        #handObj.printCards()
        return False
    else:
        return True
    '''


# In[34]:
#new_deck = Deck()


# In[35]:
#new_player = Hand()


# In[36]:
#new_deck.shuffle()


# In[37]:
#hit(new_deck,new_player)


# In[ ]:
# In[ ]:
# In[ ]:

# In[38]:

def dealer_hitting(deck, dealer):
    
    print("\nDealer hitting...")
    hit(deck,dealer)


# In[ ]:
# In[39]:


def hit_or_stand(deckObj, handObj):
    
    global playing
    
    print("\n===========")
    print("1 - Hit")
    print("2 - Stand")
    print("===========\n")
    
    boolVal = True
    
    while boolVal:
        try:
            choice = int(input("Please enter a choice (1 or 2): "))
        except:
            print("Sorry, enter a integer choice.")
            continue
        else:
            if choice in [1,2]:
                if choice == 1:   # Hit option chosen!
                    print("\n==> Hit the card!\n")
                    hit(deckObj,handObj)
                    
                    boolVal = False
                    break
                    
                else:         # Stand option chosen!
                    print("\n==> Standing...\n")
                    playing = False
                    
                    boolVal = False
                    break
                    
            else:
                print("Sorry, choose between 1 and 2 only.")
                continue


# In[40]:


#new_deck = Deck()
#new_player = Hand()
#new_deck.shuffle()


# In[41]:
#hit_or_stand(new_deck,new_player)
# In[ ]:
# In[42]:
# playing

# In[43]:


# player and dealer - in the arguments - are Hand objects
def show_some(player,dealer):
    
    print("\nDealer's first card is hidden:")
    dealer_list = dealer.cards[1:]
    for card in dealer_list:
        print(card)
        
    print("\nPlayer's all cards: ")
    player.printCards()
    print("\n")


# In[44]:

def show_all(player,dealer):
    
    print("\nPlayer's cards: ")
    player.printCards()
    print(f"\nPlayer's total value: {player.total_value}\n\n")
    
    print("Dealer's cards: ")
    dealer.printCards()
    print(f"\nDealer's total value: {dealer.total_value}\n\n")



def dealer_wins(players_chips,player,dealer):
    print("\n=====================")
    print("THE DEALER WON!!!")
    print("=====================\n")
        
    print("Player's cards: ")
    player.printCards()
    print("\nDealer's cards: ")
    dealer.printCards()
    
    # print Player's chips before and after one was busted
    print("\nBefore the dealer won, player's chips:")
    players_chips.printChips()
    players_chips.lose_bet()
    print("After the dealer won, player's chips:")
    players_chips.printChips()
    
    show_all(player,dealer)
    
        
    print(f"\n\nDealer's total value: {dealer.total_value}")
    print(f"Player's total value: {player.total_value}")
    
    print("\n==========")
    print("GAME OVER!")
    print("==========\n\n\n")



def dealer_busts(player_chips,player,dealer):
    print("\n====================================")
    print("The dealer was busted!!! ")
    print("THE PLAYER WON!")
    print("====================================\n")
    
    # print Player's chips before and after one was busted
    print("Before the dealer busted, player's chips:")
    player_chips.printChips()
    
    player_chips.win_bet()
    
    print("After the dealer busted, player's chips:")
    player_chips.printChips()
    
    show_all(player,dealer)
    
    
    print("\n==========")
    print("GAME OVER!")
    print("==========\n\n\n")
    


# In[47]:


def player_busts(player_chips,player,dealer):
    print("\n\n--------------------")
    print("Player was busted!!!")
    print("THE DEALER WON!")
    print("--------------------\n\n")
    
    # print Player's chips before and after one was busted
    print("Before the player lost:")
    player_chips.printChips()
    
    
    # Chips class has the lose_bet() function, which will subtract the bet from the total
    # and set back the bet attribute to 0 after calculating total
    player_chips.lose_bet()
    
    print("After the player lost:")
    player_chips.printChips()
    
    show_all(player,dealer)
    
    
    print("\n==========")
    print("GAME OVER!")
    print("==========\n\n\n")



players_chips = Chips()

def play_game():
    global players_chips

    while True:
        
        while players_chips.total <= 0:
            print("\n\nSorry, can't play without chips.")
            try:
                players_chips.total = int(input("Please enter your NEW total chips balance: "))
            except:
                print("Sorry, integers only.")
                continue
            else:
                break  # breaks out of the inner while loop
        
        # Print an opening statement
        print("\n\n**********************")
        print("Welcome to BlackJack!")
        print("**********************\n\n")

        global playing
        global player_busted

        playing = True
        player_busted = False

        # Create & shuffle the deck, deal two cards to each player
        new_deck = Deck()
        new_deck.shuffle()

        player = Hand()
        dealer = Hand()

        for x in range(2):
            player.add_card(new_deck.deal_one())
            dealer.add_card(new_deck.deal_one())


        # Setup player's chips
        ## global players_chips is done
        # Prompt the player for their bet
        user_bet = take_bet(players_chips.total)
        players_chips.bet = user_bet

        print("________________________________________________________________________")

        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)


        # This while loop should run at least once for a new game
        while playing:
            print("\n\nInside the 'while playing' loop.\n\n")
            # Prompt for "Player" to Hit or Stand
            hit_or_stand(new_deck,player)
            # if stand is chosen from the hit_or_stand, then playing = False,
            # and while loop will end



            # Show cards (but keep one dealer card hidden)
            show_some(player,dealer)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player.total_value > 21:
                player_busts(players_chips,player,dealer)
                player_busted = True
                break


        # If Player hasn't busted, play Dealer's hand until Dealer either wins or loses
        if player_busted == False:

            # Show all cards
            print("\n\nAll cards are shown.\n\n")
            show_all(player,dealer)


            # Run different winning scenarios:

            # 1. If Dealer keeps hitting and exceeds player's total AND Dealer's 
            # total is under 21, then Dealer won
            # 2. If Dealer busted, then the Player won

            dealer_hit = True


            while dealer_hit == True:
                # Check if dealer can win before hitting
                if dealer.total_value < 21 and dealer.total_value > player.total_value:
                    dealer_wins(players_chips,player,dealer)
                    dealer_hit = False
                    break    # Don't hit if dealer already won

                dealer_hitting(new_deck,dealer)

                # If Dealer won
                if dealer.total_value < 21 and dealer.total_value > player.total_value:
                    dealer_wins(players_chips,player,dealer)
                    dealer_hit = False

                # Else If the Dealer was busted (which means the Player won)    
                elif dealer.total_value > 21:
                    dealer_busts(players_chips,player,dealer)
                    dealer_hit = False

                else:
                    pass


        yes_or_no = input("\n\nDo you want to play another game (Y or N)?: ")

        if yes_or_no not in ['Y','N']:
            while yes_or_no not in ['Y','N']:
                print("Sorry, please enter Y or N.")
                yes_or_no = input("Do you want to play another game (Y or N)?: ")

        print("________________________________________________________________________")

        if yes_or_no == "N":
            print("\n\nGOODBYE!\n\n")
            break
        else:
            playing = True
            player_busted = False
            continue



play_game()


print(f"\nPlayer's chips total:  {players_chips.total}")





