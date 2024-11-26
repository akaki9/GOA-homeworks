# 1 დან 100 მდე დაბეჭდეთ მხოლოდ ის რიცხვები რომლებიც 3 ჯერადიც არის და 5 ჯერადიც

num = 1

while num >= 1 and num <= 100:
    if num % 3 == 0 and num % 5 == 0:
        print(num)
    num = num + 1