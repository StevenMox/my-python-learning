# -*- coding: utf-8 -*-

name = 'Steven J. Moxley'
age = 28
height = 72 #inches
weight = 185 #lbs
eyes = 'Hazel'
teeth = 'White'
hair = 'Dirty Blonde'

#conversion for inches to centimeters
inches = 72
centimeters = inches * 2.54

#conversion for lbs to kg
pounds = 180
kilos = pounds / 2.2046226218

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "%r inches equals %r centimeters." % (inches, centimeters)
print "%s pounds equals %.5s kilos" % (pounds, kilos)
#.(any number to round to certain decimal place in python)
