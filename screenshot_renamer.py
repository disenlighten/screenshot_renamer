# from time import strftime, strptime
import time

# define variables
picsdir = '/Users/james/Pictures'

# define functions
def convert_time(base_file_path, file_name):
    my_time_stamp = strftime("%Y%m%d", strptime(time.ctime(os.path.getmtime(base_file_path + '/' + file_name))))
    return my_time_stamp

# get user input
my_input = input('Enter a date in the format YYYYMMDD: ')

for my_file in os.listdir(picsdir):
    if my_file[-4:] == '.png':
        current_stamp = convert_time(picsdir, my_file)
        if current_stamp == my_input:
            print('{} {}'.format(my_file, time.ctime(os.path.getmtime('{}/{}'.format(picsdir, my_file)))))

    
