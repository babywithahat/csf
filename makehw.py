#!/usr/bin/python2
print "This program creates a pdf of dicrete mathematics homework"
assign_num = raw_input("What assignment number is this?: ")
class_thread = raw_input("Which thread in class does this assignment pertain to?: ")
title_name = raw_input("What is the title of your assignment?: ")
file_name = "Assignment" + assign_num + "_chaveza.tex"



print "Creating and opening file " + file_name + " ..."
fo = open(file_name, "w")
fo.close()
fo = open(file_name, "w")
fo.write("\documentclass{article}\n")
fo.write("\usepackage{graphicx}\n")
fo.write("\\begin{document}\n")
fo.write("\hfill Alejandro Chavez\n\n")
fo.write("\hfill Assignment " + assign_num + " - " + class_thread + "\n\n")
fo.write("\hfill \\today\\\\\n\n")
fo.write("\\begin{center}")
fo.write("\\begin{large}")
fo.write(title_name)
fo.write("\end{large}")
fo.write("\end{center}")

def remove_last_line_from_string(s):
  return s[:s.rfind('\n')]
last_line_deleted = 0

itemize_nests = 0
exit_code = 0
status = ""
process = ""
tab_stack = list()
while (exit_code == 0):
  print "##########"
  print process
  print "##########" + status
  print "---"
  print "itemize nests: ",itemize_nests
  print "---"
  print "b: \\begin{itemize}"
  print "e: \\begin{end}"
  print "i: \\item"
  print "t: make a table"
  print "x: Enter text"
  print "u: undo last line"
  print "!: finish"
  prompt = raw_input(">> ")
  if prompt in ['b', 'B']:
    tabs = "\t"*itemize_nests
    tab_stack.append(itemize_nests)
    fo.write(tabs + "\\begin{itemize}\n")
    process += tabs + "\\begin{itemize}\n"
    itemize_nests += 1
    status = "///nest begun. %s nests open." % itemize_nests

  elif prompt in ['e', 'E']:
    if itemize_nests == 0:
      status =  "///There are no itemize nests to end."
    else:
      itemize_nests -= 1
      tabs = "\t"*itemize_nests
      tab_stack.append(itemize_nests)
      fo.write(tabs + "\\end{itemize}\n")
      process += tabs + "\\end{itemize}\n"
      status = "///nest ended. %s nests open." % itemize_nests

  elif prompt in ['i', 'I']:
    if itemize_nests == 0:
      status =  "///There are no itemize nests to create an item under."
    else:
      tabs = "\t"*itemize_nests
      tab_stack.append(itemize_nests)
      fo.write(tabs + "\item\n")
      process += tabs + "\item\n"
      status = "//item created"

  elif prompt in ['x', 'X']:
    tabs = "\t"*itemize_nests
    texttabs = "\t"*(itemize_nests+1)
    tab_stack.append(itemize_nests)
    text = raw_input("Enter text>> ")
    fo.write(texttabs + text + "\n")
    process += texttabs + text + "\n"
    status = "///text entered"

  elif prompt in ['u', 'U']:
    process = remove_last_line_from_string(process)
    process = remove_last_line_from_string(process)
    process += "\n"  
    fo.close()
    rf = open(file_name)
    lines = rf.readlines()
    rf.close
    fo = open(file_name, "w")
    fo.writelines(lines[:-1])
    itemize_nests = tab_stack.pop() 
  elif prompt in ['!']:
    if itemize_nests != 0:
      status =  "There are still itemize nests that need to be ended."
    else:
      exit_code = 1

  else:
    status = ""

fo.write("\\end{document}\n")
fo.close()
