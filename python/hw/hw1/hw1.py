# Name:	alejandro chavez 
# Evergreen Login: chaveza chaale04
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###


a = 1.0
b = -5.86
c = 8.5408
answer1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
answer2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
print "\nProblem 1 solution follows:\n\n	%s\n	%s\n" % (answer1, answer2)


###
### Problem 2
###


import hw1_test
print "Problem 2 solution follows:\n\n	%s\n	%s\n	%s\n	%s\n	%s\n	%s\n" % (hw1_test.a,hw1_test.b,hw1_test.c,hw1_test.d,hw1_test.e,hw1_test.f)


###
### Problem 3
###


answer3 = ((hw1_test.a and hw1_test.b) or (not hw1_test.c) and not (hw1_test.d or hw1_test.e or hw1_test.f))
print "Problem 3 solution follows:\n\n	%s\n" %answer3



###
### Collaboration
###

