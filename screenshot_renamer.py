# from time import strftime, strptime
import time
import os

# define variables
picsdir = '/Users/james/Pictures'

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

def renamer(before_file_name, after_file_name):
    my_before_file = base_file_path + '/' + before_file_name
    os.rename(before_file_name,after_file_name)

# get user input
my_input = input('Enter a date in the format YYYYMMDD: ')

# make a list of png files in the base directory
my_png_files += [my_file for my_file in os.listdir(picsdir) if my_file[-4:] == '.png']

    
