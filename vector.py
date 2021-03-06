#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       vector.py
#       
#       Copyright 2011 Stephen Ward <aukondk@aukondk.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import os

class fs_dir(object):
	def __init__(self, name):
		self.name = name
		self.exists = True

class fs_file(object):
	def __init__(self, name):
		self.name = name
		self.exists = True
		self.content = ""



def cmd_help():
	print "Recognised commands:"
	print "ls - List contents of current directory"
	print "exit - Leave Attack Vector"

def login():
	global loginname
	global cur_dir
	cur_dir = "/"
	print "NotUNIX v1.0"
	loginname = raw_input("Username: ")
	loginpass = raw_input("Password: ")

def prompt():
	global loginname
	global cur_dir
	command = raw_input(loginname + "@localhost:" + cur_dir + "# ")
	
	if command == "exit":
		print "End of Line"
		exit()
	
	elif command == "ls":
		cmd_ls()
	
	elif command == "help":
		cmd_help()
	
	else:
		print command + ": Command not found"
	prompt() #shouldn't have this nested inside itself :p while loop?

def cmd_ls():
	print "This will display files in the current directory"




os.system("clear")
print "ATTACK VECTOR - Computer Security Simulation"
print
login()
print
print "Welcome. Enter \"help\" for instructions"
prompt()
