#  შექმენით ახალი სია მხოლოდ ლუწი რიცხვების ერთი დიდი სიიდან 

big_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

small_list = [num for num in big_list if num % 2 == 0]

print(small_list)

