import os   # importing new library into the code

print(os.system("df -h"))   # Linux or mac
print(os.system('uptime'))  # uptime and load
print(os.system("free -m"))  # memory RAM

command ="date" 
command = "uptime"

def check_cpu(command): #defining function
    print(os.system(command))

check_cpu("date") # calling function


def time(command):
    print(os.system(command))

time("uptime")