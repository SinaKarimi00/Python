start = False
want2 = ''
up = '|'
down = '_'

while True:
    print('''
        Enter What do you want to do?
        1-Start a car => start
        2-Turn off => off
    ''')
    want = input()
    if want.upper() == "START":
        if not start:
            start = True
            print('''
            Car Start
            Now what should I do?
            1-For up => +
            2-For down => -
            ''')
            want2 = input()
            if want2 == '+':
                print(f"Window go up {up}")

            elif want2 == '-':
                print(f"Window go Down {down}")

        else:
            print('''
            Car was starting
            Now what should I do?
            1-Up => +
            2-Down => -
            ''')
            want2 = input()
            if want2 == '+':
                print(f"Window go up {up}")

            elif want2 == '-':
                print(f"Window go Down {down}")            
    elif want.upper() == "OFF":
        if start:
            print("The car turned off")
            break
        else:
            print("The car was off")
            break