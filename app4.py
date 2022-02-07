guess_count = 1
while guess_count <= 5:
    print('*' * guess_count)
    guess_count = guess_count + 1
print('Done')

'Program 2'

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("you won")
        break
else:
    print("you lose")

"Program 3"

car_value = ""
started = False
while True:
    car_value = input('> ').lower()
    if car_value == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("start - to exit")
    elif car_value == "start":
        if started:
            print('car already started')
        else:
            started = True
            print("Car started...Ready to go")
    elif car_value == "stop":
        if not started:
            started = False
            print("Car stopped")
        else:
            print('car already stopped')
    elif car_value == "quit":
        break
    else:
        print("I don't understand that...")

