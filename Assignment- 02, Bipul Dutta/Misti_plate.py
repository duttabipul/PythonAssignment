
# Assignment No: 02,       Date: 19.05.2022
# Misti Plate => Height and Width
# Output => Total number of Misti

misti_plate_height = int(input("Enter the height of Misti Plate: "))
misti_plate_width = int(input("Enter the width of Misti Plate: "))

total_area = misti_plate_height * misti_plate_width
total_number_of_misti = (misti_plate_height + misti_plate_width) + (total_area/2+1) # It works incremental way
sumIsNotZero = True

while sumIsNotZero:
    print("Total area of the Misti Plate is: ", total_area)
    sumIsNotZero = False

print("Total number of Misti is: ", total_number_of_misti)

# Output:
# Enter the height of Misti Plate: 4
# Enter the width of Misti Plate: 2
# Total area of the Misti Plate is: 8.00
# Capacity of the total Misti is: 11.00