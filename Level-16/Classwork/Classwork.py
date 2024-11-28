#საკლასო დავალება: მომხმარებელს შემოატანინეთ რიცხვი და შეინახეთ ის ცვლადში მთელი რიცხვის სახით.
#შემდეგ შექმენით დიაპაზონი 0-დან ამ რიცხვამდე და დაბეჭდეთ დიაპაზონის ყველა რიცხვის ჯამი.
#გამოიყენეთ for ციკლი

num1 = int(input("Enter number: "))
sum1 = 0
for i in range(0 , num1):
    sum1 = sum1+i
    print(sum1)




#საკლასო დავალება: 
#შექმენით correct_password ცვლადი და მასში შეინახეთ ნებისმიერი სთრინგი.
#სანამ მომხმარებლის შემოტანილი პაროლი არ იქნება correct_password-ის ტოლი, თავიდან შეეკითხეთ.
#საბოლოოდ, დაუბეჭდეთ access granted და ასევე რამდენჯერ მოუწია პაროლის შემოტანა.
#დაგჭირდებათ while loop, counter variable
correct_passwrod = "Lagosha!"
user_guess = input("Enter passwrod: ")

while user_guess != correct_passwrod:
    user_guess = input("Enter passwrod: ")
    counter = 1
print("accsess granted")
#print("Your guess count: ", str(counter)



#საკლასო დავალება:
#რიცხვის გამოცნობის პროგრამა:
#შექმენით my_num ცვლადი და 1-დან 10-მდე ნებისმიერი რიცხვი მიანიჭეთ მნიშვნელობად.
#სანამ მომხმარებლის შემოტანილი რიცხვი არ იქნება my_num-ის ტოლი, ისევ შეეკითხეთ მომხმარებელს ეს რიცხვი.
#საბოლოოდ დაუბეჭდეთ "you guessed" და რამდენი ცდა დაჭირდა


my_num = 7
user_num = int(input("Enter number: "))
counter = 0

while user_num != my_num:
    user_num = int(input("Enter number: "))
    counter += 1

print("you guessed")
print("Your guess count:", str(counter))