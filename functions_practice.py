def hello():
    print("Greetings User")
hello()

def pack(first_name, middle_name, last_name):
    return[first_name, middle_name, last_name]
print(pack("Lukas", "Allen", "Linares"))

def eat_lunch(my_list):
  if len(my_list) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_list)):
      if i == 0:
        print(f"First I eat {my_list[0]}")
      else:
        print(f"Next I eat {my_list[i]}")
eat_lunch([])
eat_lunch(["Sandwich","Chips","Yogurt","Pie"])