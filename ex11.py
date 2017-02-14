print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "\nSo, you're %r years old, %r tall and %r lbs." % (age, height, weight)

print "\nWhat's your favorite colour?",
colour = raw_input()
print "What's your favorite movie?",
movie = raw_input()
print "What's your favorite season?",
season = raw_input()

print "\nYour favorite colour is %r, your favorite movie is %r, and your favorite season is %r." % (colour, movie, season)

#PEP 3111: raw_input() was renamed to input(). That is, the new input() function
#reads a line from sys.stdin and returns it with the trailing newline stripped.
#It raises EOFError if the input is terminated prematurely. To get the old behavior
#of input(), use eval(input()).

print "\nEnter a number!",
num1 = int(raw_input())
print "Enter a second number!",
num2 = int(raw_input())
print "Your numbers added equals", num1 + num2
