# შექმენით სია სადაც გექნებათ  ყველა მონაცემთა ტიპის მქონე ელემენტები  შემდეგ for loop ით შეუმოწმებთ მონაცემთა ტიპებს და გამოიტანთ მხოლოდ სტრინგ ტიპის ელემენტებს

big_list = ["words", 5, 10, "blabla", True, False, 10.5]

for items in big_list:
    if type(items) == str: 
        print(items)

