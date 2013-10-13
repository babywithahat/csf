# Name: ...
# Evergreen Login: ...
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###

import hw2_test
a = 0;
b = 0;
while a != hw2_test.n+1:
  b += a
  a += 1
print "\nProblem 1 solution follows:\n\n  %s" % b

###
### Problem 2
###

print "\nProblem 2 solution follows:\n"
for x in range (2,11):
  print " %s" % (1.0/x)

###
### Problem 3
###

print "\nProblem 3 solution follows:\n"
n = 10
triangular = 0
for i in range (1,n+1):
  triangular += i;
  i +=1;
print " Triangular number:",n, "via loop:", triangular
print " Triangular number:",n, "via formula:", n*(n+1)/2


###
### Problem 4
###


n = 10
a = 1
for i in range (1,n+1):
  a = a * i 
print "\nProblem 4 solution follows:\n  %s" % a

###
### Problem 5
###

print "\nProblem 5 solution follows:\n"
n = 10
b = n
a = 1 
while b != 0:
  for i in range (1,b+1):
    a = a * i
  print " %s" % a
  a = 1
  b -= 1

###
### Problem 6
###

print "\nProblem 6 solution follows:"
n = 10
a = 1.0
for i in range (1, n+1):
  a = (1.0/i)*a
print " %s" % a

###
### Collaboration
###
##just me

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").

###
### Reflection
###

#I google how to use for loops and while loops
