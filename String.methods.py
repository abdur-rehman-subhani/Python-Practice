name=input("What's your name ? ").strip().title()
print(f"Hello, {name}")
#Remove whitespace from user's input(Str)
#name=name.strip()
#Capatalize First letter of user's name 
#name=name.capitalize()
#Capatalize First letter of each word of User's input(Str)
#name=name.title()
#Split user's name into first name and last name
first, last=name.split(" ")
print(f"Hello, {first}")
#We can use these methods together and even in First line of this program
#name=name.strip().title()