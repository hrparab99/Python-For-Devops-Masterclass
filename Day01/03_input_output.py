# String Formatting
name = input("Enter your name : ")
city = input("Enter your city : ")
about = f"\nHello Friends, Myself {name} and I am from {city}"

print(about)

name2 = input("\nEnter another name : ")
print("\nAfter using replace function",about.replace("Friends",name2))

print(dir(about))   # Which other fuction we can use