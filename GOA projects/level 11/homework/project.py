#group project done solo
#simple chatbot


print("Hello! I'm Chatbot. What's your name?")
user_name = input("Enter your name: ")


print("Nice to meet you, " + user_name + "!")


print("How are you doing today?")
user_feeling = input("Enter 'good', 'bad', or 'okay': ")


if user_feeling == "good":
    print("That's great to hear, " + user_name + "!")
elif user_feeling == "bad":
    print("I'm sorry to hear that. I hope things get better soon.")
elif user_feeling == "okay":
    print("Thanks for sharing. I hope your day improves!")
else:
    print("I'm not sure how to respond to that, but I'm here to chat!")


print("What would you like to talk about? You can say 'weather', 'sports', or 'nothing'.")

user_topic = input("Enter a topic: ")


if user_topic == "weather":
    print("I can't actually check the weather, but I hope it's nice where you are!")
elif user_topic == "sports":
    print("Sports are good for the body!")
elif user_topic == "nothing":
    print("That's okay! I'm just here to chat if you change your mind.")
else:
    print("I don't know much about that topic, but I'm still learning!")

print("Do you play videogames?")
user_videogames = input("Enter'Yes' or 'No':")

if user_videogames == "Yes":
 print("Videogames are good escape from reality but they cant often become distractions to greater goals in life")
elif user_videogames == "No":
 print("You should try some, there's something for everyone but be careful not to get addicted")
else: 
 print("please give me valid answer")


print("It was nice chatting with you, " + user_name + "! Have a great day!")
