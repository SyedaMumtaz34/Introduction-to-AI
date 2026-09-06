print("hello i'm a AI bot what is your name? ")
name=input()
print(f"Nice to meet you {name}")
print("How are you feeling today? good/bad.")
mood=input().lower()
if mood=="good":
    print("I'm glad to hear that.")
elif mood=="bad":
    print("I'm sorry to hear that.hope things get better soon.")
else:
    print("i see sometimes it's hard to put feelings into words.")
print(f"it was nice chating with you {name}.Good bye!")
