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

  user_command = raw_input("#:>") # add in "if sys.argv[1] then that else raw_input
#(i.e. any command should be available as a first input

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
  
  # autonaming option - a, q, etc (i.e. one letter titles bring up autonaming conventions)
  
  return None

def read_existing_entry(parameters): # some option to read last or read random
  entry_id, writeable_param = peel(parameters)
  writeable = False if not re.match('^w$', writeable_param) else True

  e = Entry(entry_id, writeable = writeable)
  e.edit_entry()
  # create entry object
  # call entry_object.open_file()
  # include read/write parameters
  # if file saved (check for file update) call update_date_modified method

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
  
  #keyword   = "" if (keyword is None) else keyword
  #from_date = "" if (from_date is None) else from_date
  #to_date   = "" if (to_date is None) else to_date

  clear_and_print_notice_text()

  #print keyword, from_date, to_date
  #print param1, param2, param3 
  #print "Results of searching for " + keyword + ":\n"
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

#def create_new_entry_old(title = None):
### create new entry object
### run entry.open_file 
### runs when the user enters n
### followed by optional title
### creates file in the /entries/ folder
### creates entry in entries table, consisting of file location, date created, date modified (= date created at first), key, and optional title
### call vim with appropriate parameters
### upon closing vim, prompt user for a title if one not supplied
### update db entry with appropriate data (date modified, title) 

# create new entry in entries table
# # include the title, the entry location, the date created, date modified = date created
# return the key of the new entry
# create new file in entries directory (named with the key of the file)
#  return None

#def open_vim(filename = None, write = True):
### abstract away vim interactions
#  subprocess.call(['vim', filename])
#  return None

# def read_existing_entry(entry_id, write = False):
### runs when the user enters r {entry_id} [w(rite)]
### hits the database, gets the file location
### opens the file in vim, sets to readonly but not if write is true
### if not readonly, & file saves, update date_modified after file closes
#  return None

#def quit_program():
### implement as part of the main loop
#  return None

run_main_loop()

#for row in cursor.fetchall():
#  print row[0], '\t', row[1]

# test for too many params entered
# test for too much whitespace entered
# Split user command on " " (spaces)
# item 1 = action (one of {n, e, s, q})
# item 2 = modifier (see below)
# need some way to validate these modifiers

"""
options [] = optional, {} = required
n [title] = new item (also jdk n "titlename") (doesn't need a title initially, but if no title, prompt on exit)
  create new entry. [title] is optional, but otherwise will be prompted for a title when quitting
e {action} {key} read existing entry
  open existing entry.  {action} = r for read-only, w to edit.  {key} = numeric id of entry.
s {[keyword] [from_date] [to_date]}
  search for one of these items
q quit

How it works

* Get user input
* Take action based on user input
* One of
** Create new file (func)
** Edit existing file (func)
** Search for existing file (func)
** Export file (later) - who even knows if I'll use this
** Quit

"""
