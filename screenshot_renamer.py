#!/usr/bin/env python3

# module imports
from time import strftime, strptime
import time
import os
import webbrowser
import sys
import argparse
# for a future feature
# import readline

# define variables
picsdir = '/Users/james/Pictures'
default_date = time.strftime("%Y%m%d")
# not working?
# picsdir = os.environ.get('PICSDIR')
user_choice = ''
my_png_files = []
today_files = []
all_ss = os.listdir(picsdir)

parser = argparse.ArgumentParser()
parser.add_argument("-f", dest="file_to_modify", help="A picture that you want to rename")
parser.add_argument("-d", dest="ss_date", default=default_date, help="Date in the format YYYYMMDD")
parser.add_argument("-t", dest="my_ticket_num", help="Ticket number")

args = parser.parse_args()

helptext = "\n 'h' - help."
helptext += "\n 's' - skip"
helptext += "\n 'c' - cancel rename"
helptext += "\n 'f' - confirm rename"
helptext += "\n 'g' - change incident date"
helptext += "\n 'r' - reinitialize"
helptext += "\n 't' - change ticket number"
helptext += "\n 'd' - change defaults"
helptext += "\n 'b' - back to previous file"
helptext += "\n 'q' - quit"

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

def file_navigator(user_choice,current_file,files_to_rename):
    current_index = files_to_rename.index(current_file)
    if 'b' in user_choice:
        new_current_file = files_to_rename[current_index-1]
    print(new_current_file) 
    return new_current_file

def rename_ui(files_to_rename,base_file_path,my_ticket_num,ss_date):
    for current_file in files_to_rename:
        print("Current file is: {}".format(current_file))
        open_file(picsdir,current_file)
        # webbrowser.open('file://' + (os.path.join(picsdir,current_file)))
        print("Enter d to set a description or s to skip...")
        user_choice = get_user_input()
        if 's' in user_choice:
            continue
        elif 'd' in user_choice:
            ss_desc = input('Enter a description for the screenshot: ')
            file_ext = current_file[-4:]
            my_after_file = new_namer(base_file_path,current_file,ss_date,my_ticket_num,ss_desc)
            print("Rename to {}?".format(my_after_file))
            print("Enter f to confirm or c to cancel")
            user_choice = get_user_input()
            if 'c' in user_choice:
                continue
            elif 'f' in user_choice:
                renamer(picsdir,current_file,my_after_file)
            elif 'b' in user_choice:
                current_file = file_navigator(user_choice,current_file,today_files)
                continue

def rename_ui_onefile(base_file_path,file_to_modify,my_ticket_num,ss_date):
    print("Current file is: {}".format(file_to_modify))
    open_file(base_file_path,file_to_modify)
    # webbrowser.open('file://' + (os.path.join(picsdir,current_file)))
    print("Enter d to set a description or s to skip...")
    user_choice = get_user_input()
    if 's' in user_choice:
        return False
    elif 'd' in user_choice:
       ss_desc = input('Enter a description for the screenshot: ')
       file_ext = file_to_modify[-4:]
       my_after_file = new_namer(base_file_path,file_to_modify,ss_date,my_ticket_num,ss_desc)
       print("Rename to {}?".format(my_after_file))
       print("Enter f to confirm or c to cancel")
       user_choice = get_user_input()
       if 'c' in user_choice:
           return False
       elif 'f' in user_choice:
         renamer(picsdir,file_to_modify,my_after_file)

def get_user_input():
    user_choice = input('Enter an option or h for help: ')
    return user_choice

# get initial input
def initialize_values():
    ss_date  = input('Enter a date in the format YYYYMMDD: ')
    my_ticket_num = input('Enter a JIRA ticket number: ')
    return ss_date, my_ticket_num

# main body  

# handle command line use if there a file is called from the command line
if args.file_to_modify is not None:
    file_to_modify = args.file_to_modify
    dir_path = os.path.dirname(os.path.realpath(file_to_modify))
    ss_date = args.ss_date
    if args.my_ticket_num is not None:
        my_ticket_num = args.my_ticket_num
    else:
        my_ticket_num = ""
    rename_ui_onefile(dir_path,file_to_modify,ss_date,my_ticket_num)
else:
    user_values = initialize_values()
    ss_date = user_values[0]
    my_ticket_num = user_values[1]
   
    for my_file in all_ss:
        current_stamp = convert_time(picsdir, my_file)
        if current_stamp == ss_date and my_file[-4:] == '.png':
            today_files.append(my_file)

    rename_ui(today_files,picsdir,my_ticket_num,ss_date)
