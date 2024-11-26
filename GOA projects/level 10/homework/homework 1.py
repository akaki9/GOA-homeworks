# 1) შექმენით კალკულატორი, მომხარებელს შეეკითხეთ ორი რიცხვი, შემდეგ შეეკითხეთ რა მოქმედების შესრულება სურს ამ ორ რიცხვზე და მისი პასუხიდან გამომდინარე შეასრულეთ მოქმედება და დაბეჭდეთ.
# მაგალითად, თუ მომხარებელი შემოიტანს რიცხვებს 5 და 7, და შემოიტანს მოქმედებას მაგალთად დამატებას, თქვენ უნდა დაუბეჭდოთ 5 + 7 = 12

num1 = int(input ("number 1:"))
num2 = int(input ("number 2:"))

operator = input ("what do you want to do with numbers: (+ , - , / , *):")

if operator == "+":
    print(num1, "+", num2, "=", int(num1) + int(num2))

elif operator == "-":
 print(num1, "-", num2, "=", (int(num1) - int(num2)))

elif operator == "/":
 print(num1, "/", num2, "=", (int(num1) / int(num2)))

elif operator == "*":
 print(num1, "*", num2, "=", (int(num1) * int(num2)))
 
else: 
  print("something went wrong")


