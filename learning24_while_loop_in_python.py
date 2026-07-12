"""while loop"""
# while loop syntax:
# while condition:
#   code
#   increment or decrement

# in while loop starting point is written first outside of loop
# then condition is written by side and increment or decrement
# is written in the body
var = 1
while var <= 10:
    print(var)
    var += 1


"""continue in while loop"""
# skips iterations just like steps and does not send value to
# code if condition is True
var = 0
while var <= 10:
    var += 1
    if var < 6:
        continue
    print(var) # 6 to 11


"""break in while loop"""
var = 1
while var <= 10:
    if var == 6:
        break
    print(var) # 1 to 5
    var += 1


"""while True"""
# while loop runs infinitely and takes infinite inputs until
# break is written
# While True:
#   a = input()
# if condition is true loop breaks and stops
var = 1
while True:
    if var == 10:
        break
    var += 1
# useful for console based mini projects
