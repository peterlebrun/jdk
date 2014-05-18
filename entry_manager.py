#! usr/bin/python

# Implement as a singleton class

import sqlite3
import sys
from sets import Set
import subprocess
import re
from entry import Entry
import math

def peel(onion):
### Take in space delimited string of tokens
### split off (peel) first token (layer) & rest of body (onion)
### return layer & onion
### anticipated to be used multiple times
### i.e. if you enter s k:home f:2013-10-01 t:2013-10-31
### it can be called four times to return each token as a new "layer"
  if ' ' in onion:
    layer, onion = onion.split(' ', 1)
  else:
    layer = onion
    onion = '' 

  return layer, onion

def run_main_loop():
  clear_and_print_notice_text()
  populate_home_screen_data()

  user_command = raw_input("#:>")

  while (user_command[0] != "q"):
    command, parameters = peel(user_command)  

    if (command == "n"):
      create_new_entry(parameters)

    elif (command == "r"):
      read_existing_entry(parameters)    

    elif (command == "s"):
      search_entries(parameters)

    elif (command == "t"):
      export_entry(parameters)

    elif (command == "h"):
      display_help_text()

    else:
      print "Command not recognized, try again.  Enter h for help."
    
    user_command = raw_input("#:>")

def clear_and_print_notice_text():
  subprocess.call(['clear'])

  notice_text = """jdk Text Entry Manager

Author\tPeter LeBrun
Contact\tpeterlebrun@gmail.com
Written\t2013

Feel free to modify and distribute for non-commercial purposes.
Contributions to project welcomed (and encouraged!)
_______________________________________________________________
  """

  print notice_text

  return None

def populate_home_screen_data():
  print "30 most recently edited entries:\n"
  titles = Entry.get_home_screen_data()
  print_titles(titles)

  return None

def create_new_entry(parameters):
  title = parameters
  
  e = Entry(title = title)
  e.edit_entry() 
  
  if (title == ""):
    print "\nEnter title:"
    e.update_title(raw_input("#: >> "))
    print "\nTitle set.\n"
  
  
  return None

def read_existing_entry(parameters): # some option to read last or read random
  entry_id, writeable_param = peel(parameters)
  writeable = False if not re.match('^w$', writeable_param) else True

  e = Entry(entry_id, writeable = writeable)
  e.edit_entry()

  return None

def search_entries(parameters):
  param1, rest = peel(parameters)
  param2, param3 = peel(rest)
   
  keyword, from_date, to_date = None, None, None

  for param in [param1, param2, param3]:
    if (param and param[0] == "k"):
      keyword = param[2:]

    elif(param and param[0] == "f"):
      from_date = param[2:]

    elif(param and param[0] == "t"):
      to_date = param[2:]
  
  clear_and_print_notice_text()

  titles = Entry.search_existing_entries(keyword, from_date, to_date)
  print_titles(titles)

  return None 

def print_titles(titles):
#  for i in range(int(math.floor(len(titles)/3))):
  for i in range(len(titles)):
    starting_space = " " if (len(str(titles[i][0])) == 1) else ""
    print " " + starting_space + str(titles[i][0]) + "  " + titles[i][1] 

  print

  return None

def export_entry(parameters):
  entry_id, location = peel(parameters)
  
  e = Entry(entry_id)
  e.export_entry(location)
  
def display_help_text():
  help_text = """
  Options:
  n {optional title}
    Create new entry with title "title"
    Opens a vim instance, using normal vim keybindings
    Example: n my_entry

  r id {optional writeable}
    Read existing entry with id "id"
    Example: r 15 w

  s {optional k:keyword f:fromdate t:todate}
    Search for existing entries
    Requires at least one of keyword, fromdate, or todate
    Note that date has to be in the form of yyyy-mm-dd
    i.e. Always 2 digit days and months (06, 04, 13, etc)
    Example: s k:keyword f:2013-10-21

  t id
    Export entry with id "id" to text file
    Example: t 15

  h
    Open help dialog

  q
    Quit the program
  """
  print help_text  
  
  return None

run_main_loop()

