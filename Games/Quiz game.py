
#python quiz code

score = 0
print("Welcome to Quizspace!")
print("Enter a username:")
var1 = input()
print("What is 1 + 1?")
var2 = int(input())
if var2 == 2:
    print("Correct!")
    score += 10
else:
    print("Incorrect!")

print("What is 12 x 2?")
var3 = int(input())
if var3 == 24:
    print("Correct!")
    score += 10
else:
    print("Incorrect!")
    
print("What is 81 ÷ 9?")
var4 = int(input())
if var4 == 9:
    print("Correct!")
    score += 10
else:
    print("Incorrect!")
    
print("What is 202 ÷ 2?")
var5 = int(input())
if var5 == 101:
    print("Correct!")
    score += 10
else:
    print("Incorrect!")
    
print("What is the word that means happy (choose from sad, contented and furious)?")
var5 = input()
if var5 == "contented":
    print("Correct!")
    score += 20
else:
    print("Incorrect!")
    
print("What is the word that means to support needed help(choose from administer, betray and check)?")
var6 = input()
if var6 == "administer":
    print("Correct!")
    score += 20
else:
    print("Incorrect!")
print(str(score) + "/80")
print("very great, " + var1)


