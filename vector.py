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

def login():
	global loginname
	print "NotUNIX v1.0"
	loginname = raw_input("username: ")
	loginpass = raw_input("password: ")



def prompt():
	global loginname
	command = raw_input(loginname + "@localhost:/# ")
	if command == "exit":
		print "End of Line"
		exit()
	else:
		print command + ": Command not found"
	prompt() #shouldn't have this nested inside itself :p while loop?

login()
print "Welcome. Enter \"exit\" to leave"
prompt()
