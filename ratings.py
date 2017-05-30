"""Restaurant rating lister."""


# put your code here


# for i in range(0, len(line_list)):
#     line_list[i] = line_list[i].strip()

def print_rest_rate(file_name):
    """Separates restuarant and ratings from the input file into a dictionary.
       Sorts the restaurants in alphabetical order.
    """
    ratings = {}
    file_content = open(file_name)

    for line in file_content:

        rest, rate = line.strip().split(":")

        ratings[rest] = rate

    while True:
        is_user_choice = raw_input('''Do you want to 
        1. see all the resturant ratings 
        2. add a new Restaurant. 
        3. quit \nChoose 1, 2 or 3: ''')
        if is_user_choice == '1':
            sort_rest_rate(ratings)
        elif is_user_choice == '2':
            input_rest_rate(ratings)
        elif is_user_choice == '3':
            break
        else:
            print "Please enter 1, 2 or 3"


def input_rest_rate(ratings):
    while True:
        rest_name = raw_input("Please input Restaurant name: \n")
        rest_rate = raw_input("Please input Restaurant rate between 1 and 5 \n")
        if not rest_rate.isdigit():
            print "Please input a number between 1 and 5 as a rate!"
        elif int(rest_rate) > 5 or int(rest_rate) < 1:
            print "Please input a number between 1 and 5 as a rate!"        
        else:
            break

    ratings[rest_name] = rest_rate


def sort_rest_rate(ratings):
    for rest, rate in sorted(ratings.items()):
        print rest, rate
    

print_rest_rate("scores.txt")



