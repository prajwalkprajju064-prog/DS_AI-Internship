cities =["karnataka","chennai","bengaluru","noida","mumbai"]
heros =["rdhil","yah","darshan"]

def print_len(list):
    print(len(list))
    
def print_list(list):
        for item in list:
            print(item, end="    ")


print_len(heros)
print_list(cities)