def get_minuts_value():
    while True:
        try:
            value = int(input('Please enter number of minutes to calculate: \n'))  
            if value > 0:
                return value
            print('Try agian! This value is incorrect! Only positive numbers grater than 0 are allowed.') 
        except ValueError:
            print('Try agian! This value is incorrect! Only positive numbers grater than 0 are allowed.')

def calculations(minutes_total):
    days, rem_minutes = divmod(minutes_total, 1440) 
    hours, minutes = divmod(rem_minutes, 60) 
    return days, hours, minutes

def ask_to_continiue():    
    while True:
        user_input = input('Calculate again - Y/N: \n').strip().lower()
        if user_input in ('y', 'n'):
            return user_input == 'n'
        print('Please enter (Y)es or (N)o.')

def main():
    while True:
        D, H, M = calculations(get_minuts_value())
        print(f"<{60 * '-'}>")
        print(f'Days: {D}, Hours:{H}, Minutes:{M}')
        if ask_to_continiue(): break

main()