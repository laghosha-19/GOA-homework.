#for ციკლის გამოყენებით 20-ჯერ დაბეჭდეთ თქვენი სახელი და გვარი
for x in range (20):
    print("Laghoshvili luka")


#მომხმარებელს შემოატანინეთ რიცხვი და შეინახეთ მთელი რიცხვის სახით. იგივე გაიმეორეთ მემეორე ცვლადზე.
#for ციკლით იტერაცია მოახდინეთ დიაპაზონზე, რომლის საწყისი რიცხვია პირველი ცვლადი და საბოლოო რიცხვია მეორე ცვლადი.
#ციკლის ყოველ იტერაციაზე დაბეჭდეთ საიტერაციო ცვლადის კვადრატი
#num1 = int(input("Enter Num1 "))
#num2 = int(input("Enter Num2 "))
num1, num2 = int(input("Enter Num1 ")), int(input("Enter Num2 "))
for i in range(num1):
    print(i**2)
    print(num1)
for x in range(num2):
    print(x**2)
    print(num2)

#Task: Print the Squares of Numbers
#Write a Python program that:
#Asks the user to enter a number 𝑛
#Uses a for loop to print the square of each number from 1 to n.

n = int(input("Enter Number: "))
for i in range(n):
    print(i**2)

