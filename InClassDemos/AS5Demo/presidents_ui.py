
from presidents import Presidents

a_presidents = None

def main():
    print("Presidents Program")
    get_data()

def get_data():
    try:
        with open('presidents.txt', 'r') as infile:
            lines = infile.readlines()
        # list comprehension -- for item in the list, strip - remove white space
        presidents = [item.strip() for item in lines]
    # exceptions starting with most specific and getting more general
    except FileNotFoundError as e:
        print(e)
    except ValueError as e: 
        print(e)
    except Exception as e:
        print(e)

    create_object(presidents)

def create_object(presidents):
    global a_presidents

    a_presidents = Presidents(presidents)

    # quick test
    print(a_presidents.num_times_back_to_back_presidents())
    print(a_presidents.num_times_president("Abraham Lincoln"))

main()