import random

# Create a random list selector
print("...rock...\n..paper..\n...scissors...")

items = ['rock', 'paper', 'scissors']

player_one = random.choice(items)

print("(Enter player 1's choice): " + player_one)

for x in range(60):
    print("...NO CHEATING...")

player_two = input("(Enter Player 2's choice): ").lower()

while player_two != 'rock' and player_two != 'paper' and player_two != 'scissors':
    print("Enter a valid Choice")
    player_two = input("(Enter Player 2's choice): ").lower()

print("SHOOT!")

# if p1 == rock and p2 == paper > p2 wins
if player_one == 'rock' and player_two == 'paper':
    print('Player 2 wins!')
# if p1 == rock and p2 == scissors > p1 wins
elif player_one == 'rock' and player_two == 'scissors':
    print("Player 1 wins!")
# if p1 == paper and p2 == scissors > p2 wins
elif player_one == 'paper' and player_two == 'scissors':
    print("Player 2 wins!")
# if p1 == paper and p2 == rock > p1 wins
elif player_one == 'paper' and player_two == 'rock':
    print("Player 1 wins!")
# if p1 == scissors and p2 == rock > p2 wins
elif player_one == 'scissors' and player_two == 'rock':
    print('Player 2 wins!')
# if p1 == scissors and p2 == paper > p1 wins
elif player_one == 'scissors' and player_two == 'paper':
    print('Player 1 wins')
else:
    print("Draw!")
