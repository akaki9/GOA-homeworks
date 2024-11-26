# შემოატანინეთ მომხმარებელს რიცხვი და დაადგინეთ არის თუ არა დადებითი უარყოფითი ან ნულის ტოლი 

num1 = int(input("enter your number:"))
if num1 == 0:
    print("number is 0")
elif num1 < 0:
    print("number is negative")
elif num1 > 0:
    print("number is positive")