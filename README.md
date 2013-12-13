jdk
===

A text entry management system inspired by vim

Background
When I used windows, I was a big fan of Q10.  Removed all the distractions.

But, I was stuck managing all the files I created by myself.  Even worse, I couldn't easily search everything!

Enter the idea for jdk: a lightweight, database-backed file management system.

To begin:

simply run python entry_manager.py from the command line.

press h to read jdk's help syntax.

Overview
jdk is made to be simple.

Set up an alias in your system so that jdk='python entry_manager.py'.  A new text entry is now only a few keystrokes away.
"jdk" to enter the project, "n" to create a new entry.  After you finish writing, you will be prompted for a title.

If you want to read an existing entry, just type "r {id}" where id is the primary key of the entry in the database.

Don't know the primary key?  just type "s k:'keyword'" to see the relevant results, including their primary keys.

And when you're done, "q" to quit.

For more information, type "h" to view the jdk help page.

Why jdk?

jdk doesn't stand for anything in particular, it's just simple to type.  Right pointer, left middle, right middle, <CR>.
