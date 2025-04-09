#Pseudokod
#Start:
#fråga användarens <name> 
#hälsa <name>, fråga om <age>
#<beräkning vilket år <name> fyller 100 år>
#skriv ut resultatet: <year>
#Slut

name = input("Vad heter du? ")
age = int(input(f"Hej {name}, Hur gammal är du? "))
year = 2025 - age + 100
#line break or \n cause it looks and makes me feel cooler :D
print(f"Du kommer att fylla 100 år, {year}. \nHa en bra dag {name}!")
