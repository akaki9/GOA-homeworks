# შემოატანინეთ მომხმარებელს მისი ასაკი თუ მისი ასაკი 18 წელზე მეტია დაუპრინტეთ “you are adult” თუ 18 წელზე ნაკლები “you are virgin”

num1 = int(input("enter your age:"))

if num1 >= 18:
    print("you are adult")
elif num1 < 18:
    print("you are virgin")