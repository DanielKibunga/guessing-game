# secret_number = 9 

# guess_count= 0

# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print('You won')




animal_type = "Dog"

guess_count = 0

guess_limit = 4

dog = "Bailey"

while guess_count < guess_limit:
    guess= input ('Guess: ')
    guess_count += 1
    if guess == animal_type:
         print(f" {dog} is very happy you guessed correctly")
         break
    else:
        print(f"{dog} is sad. Why you not like her.")
###when the guesses become more than 4 this else code will be executed
else: 
    print(f"{dog} is mad at you you failed")
    


   