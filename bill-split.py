# Libraries
import src.functions as f
import click
import colorama
from colorama import Style

# Output formatting
colorama.init(autoreset=True)
f.dollar_sign()

# Click call
@click.command()
@click.option('-f','--filename', prompt=f.logo+'Bill split open file', help='Name of the legder')
@click.option('-s','--show', is_flag=True, show_default=True, help='Show previous entries at the beginning')
def start(filename, show):
    #Search file and initialize accordingly the users dictionary
    name = f.get_name(filename)
    users = f.search_file(filename, show)

    # Program start
    command = input(f.logo)
    command_dict = f.method_info_dict(command)

    while list(command_dict.keys())[0] not in f.quit_list:
        for key_arg, val in command_dict.items():
            if key_arg in f.help_me_list:
                f.help_me()

            elif key_arg in f.print_dict_list:
                f.print_dict(users)

            elif key_arg in f.wipe_all_list:
                users = f.wipe_all(users)
            
            elif key_arg in f.users_input_list:
                users = f.users_input(users, list(val))
            
            elif key_arg in f.delete_user_list:
                users = f.delete_user(users, list(val))

            elif key_arg in f.add_amount_list:
                try:
                    users = f.add_amount(users, val[0], val[1], val[2])
                except IndexError:
                    print(f.logo_error+'Invalid number of arguments. Check help[-h] for [{}] syntax'.format(key_arg))
                except ValueError:
                    print(f.logo_error+'Invalid type of argument. Amount needs to be a number. Check help[-h] for [{}] syntax'.format(key_arg))
            
            elif key_arg in f.update_amount_amount_list:
                try:
                    users = f.update_amount(users, val[0], val[1], val[2])
                except IndexError:
                    print(f.logo_error+'Invalid number of arguments. Check help[-h] for [{}] syntax'.format(key_arg))
                except ValueError:
                    print(f.logo_error+'Invalid type of argument. Amount needs to be a number. Check help[-h] for [{}] syntax'.format(key_arg))

            elif key_arg in f.remove_expense_list:
                try:
                    users = f.remove_expense(users, val[0], val[1])
                except IndexError:
                    print(f.logo_error+'Invalid number of arguments. Check help[-h] for [{}] syntax'.format(key_arg))
                except ValueError:
                    print(f.logo_error+'Invalid type of argument. Amount needs to be a number. Check help[-h] for [{}] syntax'.format(key_arg))
            
            elif key_arg in f.each_total_list:
                each = f.each_total(users)
                u = list(users.keys())
                if len(users.keys()) == 0:
                    print(f.info_logo+'There are no inputs')
                for i in range(len(users.keys())):
                    print(f.info_logo+Style.BRIGHT+'{}'.format(u[i])+Style.RESET_ALL+': '+'{}'.format(each[i]))
            
            elif key_arg in f.total_list:
                print(f.info_logo+'Total amount: '+str(f.total(users)))
            
            elif key_arg in f.calculate_list:
                try:
                    f.calculate(users, f.total(users), f.each_total(users))
                except ZeroDivisionError:
                    print(f.logo_error+'There are no inputs')
            
            else:
                print(f.logo_error+key_arg+' invalid command')

            f.save(users, name)
        command = input(f.logo)
        command_dict = f.method_info_dict(command)
 
 
if __name__ == '__main__':
    start()
