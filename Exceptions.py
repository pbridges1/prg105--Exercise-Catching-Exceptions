# Open a file
try:
    with open("Testing.txt", 'r+') as f:
        line = f.readlines()
except IOError as e:
    print "File not found({0}) : {1}".format(e.errno, e.strerror)
print "\n\n"
# Check for correct input
while True:
    try:
        t = int(raw_input("Enter a number: \n"))
        break
    except ValueError:
        print "That is not a valid number. Try again \n"
