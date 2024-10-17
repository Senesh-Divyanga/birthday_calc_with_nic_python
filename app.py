# get nic number as a user input

nic_number = input("Enter your NIC number: ")

# validate user input

def validate_nic(nic : str) -> bool:
    nic_length = len(nic)
    if nic_length == 12 and nic.isnumeric() == True:
        print("Valid NIC number")
    else:
        print("Invalid NIC number")

# identify the born year

def get_born_year():
    born_year = int(nic_number[0:4])
    return born_year

# find the date of birth


# display output

validate_nic(nic_number)