# მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი მომხარებლის შემოტანილ რიცხვამდე დაბეჭდეთ ყველა რიცხვის საშუალო არითმეტიკული 

sum = int(input("enter your number:"))
sum2 = 0
for i in range(1, sum):
 sum2 = sum2 + i

print(sum2 / sum)