#!/usr/bin/env python3

# module imports
from time import strftime, strptime
import time
import os
import webbrowser

# define variables
picsdir = '/Users/james/Pictures'
# not working?
# picsdir = os.environ.get('PICSDIR')
user_choice = ''
my_png_files = []
today_files = []
all_ss = os.listdir(picsdir)

helptext = "\n 'h' - help."
helptext += "\n 's' - skip"
helptext += "\n 'c' - cancel rename"
helptext += "\n 'f' - confirm rename"
helptext += "\n 'a' - change file date"
helptext += "\n 'g' - change incident date"
helptext += "\n 'r' - reinitialize"
helptext += "\n 't' = change ticket number"
helptext += "\n 'd' = change defaults"
helptext += "\n 'q' = quit"

# define functions
def convert_time(base_file_path, file_name):
    my_time_stamp = strftime("%Y%m%d", strptime(time.ctime(os.path.getmtime(base_file_path + '/' + file_name))))
    return my_time_stamp

def new_namer(base_file_path,before_file_name,ss_date,ticket_num,ss_desc):
    if ticket_num:
       my_ticket_num = ticket_num + '_'
    my_before_file = base_file_path + '/' + before_file_name
    file_ext = before_file_name[-4:]
    my_after_file = base_file_path + '/' + my_ticket_num  + ss_date + '_' +  ss_desc + file_ext
    return my_after_file

def open_file(base_file_path,current_file):
  webbrowser.open('file://' + (os.path.join(base_file_path, current_file)))

def renamer(base_file_path,before_file_name,after_file_name):
    my_before_file = os.path.join(base_file_path,before_file_name)
    os.rename(my_before_file,after_file_name)

def rename_ui(files_to_rename,base_file_path,my_ticket_num,ss_date):
 for current_file in files_to_rename:
    print("Current file is: {}".format(current_file))
    open_file(picsdir,current_file)
    webbrowser.open('file://' + (os.path.join(picsdir,current_file)))
    print("Enter d to set a description or s to skip...")
    get_user_input()
    if user_choice == 's':
        continue
    elif user_choice == 'd':
       ss_desc = input('Enter a description for the screenshot: ')
       file_ext = current_file[-4:]
       my_after_file = new_namer(base_file_path,current_file,ss_date,my_ticket_num,ss_desc)
       print("Rename to {}?".format(my_after_file))
       print("Enter f to confirm or c to cancel")
       get_user_input()
       if user_choice == 'c':
         continue
       elif user_choice == 'f':
         renamer(picsdir,current_file,my_after_file)

# main body         

def get_user_input():
    global user_choice
    user_choice = input('Enter an option or h for help: ')
    return user_choice

# get initial input
def initialize_values():
    global ss_date
    global my_ticket_num
    ss_date  = input('Enter a date in the format YYYYMMDD: ')
    my_ticket_num = input('Enter a JIRA ticket number: ')
    return ss_date, my_ticket_num

initialize_values()
   
for my_file in all_ss:
    current_stamp = convert_time(picsdir, my_file)
    if current_stamp == ss_date and my_file[-4:] == '.png':
      today_files.append(my_file)

rename_ui(today_files,picsdir,my_ticket_num,ss_date)



