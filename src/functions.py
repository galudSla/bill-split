# Libraries
import re 
import os
import colorama
from colorama import Fore, Style, Back

# Output formatting
colorama.init(autoreset=True)
logo = '['+Fore.CYAN+'+'+Style.RESET_ALL+'] '
info_logo = '['+Fore.YELLOW+'*'+Style.RESET_ALL+'] '
logo_error = '['+Fore.RED+'-'+Style.RESET_ALL+'] '
calculate_logo = '['+Fore.MAGENTA+'$'+Style.RESET_ALL+'] '
arrow_sign = Fore.MAGENTA+' -> '+Style.RESET_ALL

# Dollar sign logo
def dollar_sign():
    print('                     '+Back.CYAN+Style.BRIGHT+'Bill Split')
    print('''                                   
    @@@@@@@@@@@@@@@@@@@@@&&&@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@&BJ~:.........:~JG&@@@@@@@@@@@@@
    @@@@@@@@@@@@#   ?B##&&&&&##B?   #@@@@@@@@@@@@
    @@@@@@@@@@@@@#! .Y&@@@@@@@&Y. !#@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@&? :@@@@@@@: ?&@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@BG5J?J5GB@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@&J. .^!7!^. .5@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@J  ?&@@@@@@@&! .G@@@@@@@@@@@@@@
    @@@@@@@@@@@@Y  ?&@@@@@@@@@@@#^ :#@@@@@@@@@@@@
    @@@@@@@@@@G. !&@@@@@@#J#@@@@@@G. 7@@@@@@@@@@@
    @@@@@@@@&^ :#@@@@@@@@~ ~@@@@@@@@?  G@@@@@@@@@
    @@@@@@@P  5@@@@@@@5^.   .:J&@@@@@#: ~@@@@@@@@
    @@@@@@7 .&@@@@@@@^ ~#&@&#?^#@@@@@@@? .#@@@@@@
    @@@@@! ^@@@@@@@@@: !BB##&@@@@@@@@@@@G  G@@@@@
    @@@@J :@@@@@@@@@@@5~::....~&@@@@@@@@@#  G@@@@
    @@@&  B@@@@@@@@@@@@@@@@@@Y .@@@@@@@@@@P .@@@@
    @@@#  &@@@@@@@@@@!:5#&@&B^ ~@@@@@@@@@@&  #@@@
    @@@@. P@@@@@@@@@@#!..   .~G@@@@@@@@@@@P .@@@@
    @@@@G  #@@@@@@@@@@@@@~ ~@@@@@@@@@@@@@#  G@@@@
    @@@@@G  ?&@@@@@@@@@@@#?#@@@@@@@@@@@&?  G@@@@@
    @@@@@@&?  ~G&@@@@@@@@@@@@@@@@@@@&G~  ?&@@@@@@
    @@@@@@@@@P~. .~JPB#&&&&&&&#BPJ~. .~P@@@@@@@@@
    @@@@@@@@@@@@&GJ!^:.........:^!JG&@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@&&&&&@@@@@@@@@@@@@@@@@@@@                            
    ''')

# Arguments lists
help_me_list = ['-h', '--help']
print_dict_list = ['-p', '--print']
wipe_all_list = ['-w', '--wipe']
users_input_list = ['-i', '--input']
delete_user_list = ['-d', '--delete']
add_amount_list = ['-a', '--add']
update_amount_amount_list = ['-u', '--update']
remove_expense_list = ['-r', '--remove']
each_total_list = ['-e', '--each']
total_list = ['-t', '--total']
calculate_list = ['-c', '--calculate']
quit_list = ['-q', '--quit']

#Create the name with extension .txt
def get_name(to_join):
    temp_list = [to_join, '.txt']
    name_and_extension = "".join(temp_list)
    return name_and_extension

# Search if the name of the splitter exists in the same directory as .txt, 
# if not, create empty .txt with the same name
def search_file(argument, flag):
    name = get_name(argument)
    path = os.getcwd()
    file_path = path+'\\'+name
    if os.path.isfile(file_path):
        with open(file_path) as file:
            users = file.read()
            if len(users) != 0:
                users = eval(users)
            else:
                users = dict()
        if flag:
            print_dict(users)
    else:
        help_me()
        with open(file_path, 'w'):
            users = dict()
    return users

# Extracts the arguments from the user input as well as the
# information and stores them in a dictionary form, with arguments 
# as keys and everything else that follows the argument as a value of 
# that key in the form of a list
# i.e {argument:['name','expense','amount']}
def method_info_dict(user_input):
    input_dict = {}
    user_input = re.split(' ', user_input)
    args_idx = [idx for idx, arg in enumerate(user_input) if arg.startswith('-') == True]
    if len(args_idx) > 1:
        for idx, val in enumerate(user_input):
            if idx in args_idx:
                input_dict[val] = []
                temp = val
            else:
                input_dict[temp].append(val)
    else:
        input_dict[user_input[0]] = []
        for val in user_input[1:]:
            input_dict[user_input[0]].append(val)
        
    return input_dict

# Help 
def help_me():
    print(Style.BRIGHT+'\n                  IMPORTANT NOTE\n             ALWAYS SEPERATE WITH SPACES \n')
    print('-h  --help         Help')
    print('-p  --print        Print your inputs so far')
    print('-w  --wipe         Delete everything')
    print('-i  --input        Add users [user1 user2 ...]')
    print('-d  --delete       Remove user completely')
    print('-a  --add          Add expense for one user at a time [user expense-name amount]')
    print('-u  --update       Update the expense of a user [user expense-name new-amount]')
    print('-r  --remove       Remove the expense for a specific user [user expense-name]')
    print('-e  --each         How much each one paid')
    print('-t  --total        Total amount paid')
    print('-c  --calculate    Calculate')
    print('-q  --quit         Quit\n')

# Prints the user dictionary for validation purposes
def print_dict(users):
    if len(list(users.keys())) == 0:
        print(info_logo+'There are no inputs')
    for key,val in users.items():
        if val == dict():
                print(info_logo+Style.BRIGHT+('{}: No inputs'.format(key)))
                continue
        for i in val:
            print(info_logo+Style.BRIGHT+('{}: {} -> {}'.format(key, i, val[i])))

# Deletes all the information
def wipe_all(users):
    confirmation = input(logo_error+Fore.RED+Style.BRIGHT+'WARNING '+Style.RESET_ALL+"You're about to delete everything. Confirm [y]: ")
    yes_list = ['yes', 'y']
    if confirmation.lower() in yes_list:
        users = dict()
        print(logo_error+'Succesfully wiped all out')
    return users
    
# Adds usernames to the dictionary
def users_input(users, names):
    for i in names:
        if len(list(users.keys())) !=0 and i in list(users.keys()):
            print(logo_error+i+' already exists')
        else:
            users[i] = dict()
    return users

# Deletes user with all its expenses
def delete_user(users, names):
    for user in names:
        if user not in list(users.keys()):
            print(logo_error+'Username not found')
        else:
            del users[user]
    return users

# Adds the expense name and value to the dictionary
def add_amount(users, name, exp, amount):
    if name not in list(users.keys()):
        print(logo_error+'Username not found')
    else:
        users[name].update({exp: int(amount)})
    return users

# Updates the amount for an expense for a specific user
def update_amount(users, name, exp, amount):
    if (name not in list(users.keys())) or (exp not in list(users[name].keys())):
        print(logo_error+'Incorrect name or expense name')
    else:
        users[name][exp] = int(amount)
    return users
 
# Removes expense name and value
def remove_expense(users, name, exp):
    if (name not in list(users.keys())) or (exp not in list(users[name].keys())):
        print(logo_error+'Incorrect name or expense name')
    else:
        del users[name][exp]
    return users

# How much did each one pay in total
def each_total(users):    
    each_total = [0 for i in range(len(users.keys()))]
    counter = 0
    for id,val in users.items():
        for k in val:
            each_total[counter] += val[k]
        counter += 1
    return each_total

# Calculates the total amount spent
def total(users):
    total = 0
    for key,val in users.items():
        for k in val: 
            total += val[k]
    return total

# Final calculation
def calculate(users, total, each_total):    
    each = total/(len(users.keys()))
    take = [0 for i in range(len(users.keys()))]
    give = [0 for i in range(len(users.keys()))]
    for i in range(len(users.keys())):
        if each_total[i]-each > 0:
            take[i] = abs(each_total[i]-each)
        elif each_total[i]-each < 0:
            give[i] = abs(each_total[i]-each)
        else:
            take[i] = 0
            give[i] = 0
  
    usernames = list(users.keys())
    resolved = {key: {} for key in usernames}
    for k in range(len(users.keys())):
        for j in range(len(users.keys())):
            if j != k and give[j] != 0 and take[k] != 0 and take[k] > give[j]:
                resolved[usernames[j]].update({usernames[k]: give[j]})
                take[k] = take[k] - give[j]
                give[j] = 0
            if j != k and give[j] != 0 and take[k] != 0 and take[k] < give[j]:
                resolved[usernames[j]].update({usernames[k]: take[k]})
                give[j] = give[j] - take[k]
                take[k] = 0
                break
            if j != k and give[j] != 0 and take[k] != 0 and take[k] == give[j]:
                resolved[usernames[j]].update({usernames[k]: give[j]})
                take[k] = take[k] - give[j]
                give[j] = take[k] - give[j]
                break
    for key,val in resolved.items():
        for i in val:
            if val[i] != 0:
                print(calculate_logo+Style.BRIGHT+'{}'.format(key)+Style.NORMAL+arrow_sign+Style.BRIGHT+'{} {}'.format(i, round(val[i], 1)))

# Saves the dictionary to .txt
def save(users, name):
    with open(name, 'w') as file:
        file.write(str(users))


if __name__ == '__main__':
    pass 