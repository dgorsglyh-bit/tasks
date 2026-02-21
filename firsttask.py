import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
while True:
        try:    
            month_number = int(input())
            if month_number == 12 or month_number == 1 or month_number == 2:
                print("Winter")
            elif month_number == 3 or month_number == 4 or month_number == 5:
                print("Spring")
            elif month_number == 6 or month_number == 7 or month_number == 8:
                print("Summer")
            elif month_number == 9 or month_number == 10 or month_number == 11:
                print("Autumn")
            else:
                print("Error")  
        except EOFError:
            break