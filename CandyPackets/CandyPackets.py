T = input()

val_list = []
for i in range(int(T)):
    val_list.append(int(input()))


for val in val_list:
    x = 0
    bag_no = 0
    while(x < val):
        x += (2**(bag_no))
        bag_no += 1
    print(bag_no)

