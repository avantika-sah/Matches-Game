matches_left = 13

print(f"\n*****************\nWe start with {matches_left} matches, and players take turns removing 1, 2, or 3 matche(s) at a time.\nThe person who removes the last match wins.")

player1 = input("\nEnter player 1's name: ")
player2 = input("Enter player 2's name: ")

matches_taken = 0
current_player = player1

while matches_left:
    print("| " * matches_left )
    print(f"There are {matches_left} matche(s) left \nHow many do you take, {current_player}?")
    matches_taken = int(input())
    
    while matches_taken > 3 or matches_taken <= 0:
        print("You can only take 1, 2 or 3 matche(s):")
        matches_taken = int(input())
    
    while  matches_taken > matches_left:
        print(f"You can only take at most {matches_left} matche(s)!")
        matches_taken = int(input())
    
    
    matches_left -= matches_taken
    
    if (matches_left == 0):
        print(f"\n********************\n{current_player.upper()} WINS!!\nGAME OVER!")
        break   
    
    if current_player == player1:
        current_player = player2
    else :
        current_player = player1

    