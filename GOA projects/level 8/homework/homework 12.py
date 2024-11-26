# შეამოწმე, არის თუ არა მომხმარებლის შემოტანილი ორი რიცხვი ერთმანეთზე მეტი და 10-ის ჯერადი.

num1 = int(input("your number: "))
num2 = int(input("your number: "))

if num1 > num2 and num1 % 10 == 0 and num2 % 10 == 0:
    print(str(num1) + " is higher than " + str(num2))
elif num1 < num2 and num1 % 10 == 0 and num2 % 10 == 0:
    print(str(num1) + " is higher than " + str(num2))
else:
    print("One of the numbers is not multipe of 10")
