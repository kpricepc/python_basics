def hp():
    return "HP is an approved vendor."
def dell():
    return "Dell is an approved vendor."
def supermicro():
    return "Supermicro is not an approved vendor."
def inspur():
    return "Inspur is not an approved vendor."
def default():
    return user_input + " vendor is not found, and therefore is not an approved vendor."

vendor_dictionary = {
    "hp" : hp,
    "dell" : dell,
    "supermicro" : supermicro,
    "inspur": inspur
}

user_input = input("Enter Vendor: ")
user_input_formated = user_input.lower()

def vendor_lookup(vendor):
    assert vendor != "", "Please enter a vendor name"
    return vendor_dictionary.get(vendor, default)()

print(vendor_lookup(user_input_formated))