import random as rand

#for printing the word completed by the player
def round_out(l = []):
    for i in range(len(l)):
        print(l[i],end=" ")

print("===HANG MAN===")
print("Life values")
print("Total Life values = 7")
"""
print("7. Everything left")
print("6. Head drawn")
print("5. Neck drawn")
print("4. Left-arm drawn")
print("3. Right-arm drawn")
print("2. Body drawn")
print("1. Left-leg drawn")
print("0. Right-leg drawn")
print("After each wrong guess life value will be deducted by one")

"""
life_val = 7
word_list = []
alpha = 'a'
for i in range(0 , 26):
    word_list.append(alpha)
    alpha = chr(ord(alpha)+1)

#We will choose a randoom word with or without meaning in between length of 5 to 10 only
word_len = rand.choice([5 , 6 , 7 , 8 , 9 , 10])

#continue and game number
out = "G"
game = 1
while out != "0":
    print("Game Number : ",game)
    game += 1
    life_val = 7
    #random word used for hang man
    hang_word = []
    dashed_output = []
    for j in range(0, word_len):
        r = rand.randrange(0, 26)
        hang_word.append(word_list[r])
        dashed_output.append("_")

    print("Your guessed word : ",end="")
    round_out(dashed_output)
    #print(dashed_output)

    while(life_val > 0):
        user_check = input("\nEnter your best guess : ")
        flag = False
        for k in range(0, word_len):
            if user_check == hang_word[k]:
                dashed_output[k] = user_check
                flag = True
        if flag == False:
            life_val -= 1
        round_out(dashed_output)
        print("\nLife left = ",life_val)

    #result of the game
    if life_val > 0:
        print("Hurrah! You won")
    else:
        print("Better luck next time")

    out = input("Press any key to continue or 0 to exit : ")



#www.github.com/iaman0004
