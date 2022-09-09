
ItemsInCart = 0

if ItemsInCart != 2:
    # raise Exception("Less Items in cart")
    pass

assert(ItemsInCart == 0)

# Try and Catch

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except:
    print("Another Operation")
    print("New operation")

try:
    with open('file.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("Cleaning Records - Performing Git Operation")