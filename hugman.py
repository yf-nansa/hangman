

#str_pgname = "test"
#
#print(str_pgname)
#
#for char_pgname in str_pgname:
#    print(char_pgname)

#import random
#
#a=random.randint(0,100)
#print(a)
#------------------------------
#import  math
#
#a = math.sqrt(9)
#print(a)
#print(a)
#------------------------------
#import os
#print(os.getcwd())
#with open(r"\Users\s2556\Desktop\python\test.txt","r") as f:
#    print(f.read())
#------------------------------
# import csv

# with open(r"\Users\s2556\Desktop\python\test.csv","r") as f:
#     r = csv.reader(f,delimiter=",")
#     for row in r:
#         print("+".join(row))


# def hangman(word):
#     wrong = 0
#     stages = ["",
#             "________        ",
#             "|               ",
#             "|        |      ",
#             "|        0      ",
#             "|       /|\     ",
#             "|       / \     ",
#             "|               "
#             ]
#     rletters = list(word)
#     board = ["__"] * len(word)
#     win = False
#     print("Welcome to Hangman")
#     while wrong < len(stages) - 1:
#         print("\n")
#         msg = "Guess a letter"
#         char = input(msg)
#         if char in rletters:
#             cind = rletters \
#                 .index(char)
#             board[cind] = char
#             rletters[cind] = '$'
#         else:
#             wrong += 1
#         print((" ".join(board)))
#         e = wrong + 1
#         print("\n"
#             .join(stages[0: e]))
#         if "__" not in board:
#             print("You win!")
#             print(" ".join(board))
#             win = True
#             break
#     if not win:
#         print("\n"
#             .join(stages[0: \
#             wrong]))
#         print("You lose! It was {}."
#             .format(word))

# hangman("cat")


#    class Square:
#        pass
#    print(Square)

# -----------------------------------------

class Rectangle:
    recs  = []
    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width,self.len))

    def print_size(self):
        print("{} by {}".format(self.width,self.len))

class Lion:
    def __init__(self , name):
        self.name = name
    
    def __repr__(self):
        return self.name


r1 = Rectangle(10,23)
r2 = Rectangle(11,24)
r3 = Rectangle(12,25)

print(Rectangle.recs)

lion = Lion("Dilbert")
print(lion)

# -----------------------------------------
