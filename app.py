# get nic number as a user input

nic_number = input("Enter your NIC number: ")

# validate user input

if len(nic_number) != 12 and nic_number.is_integer() == False:
    print("Invalid NIC number")
else:
    print("Valid NIC number")

# identify the born year

def get_born_year():
    born_year = int(nic_number[0:4])
    return born_year

# find the date of birth


# display output

