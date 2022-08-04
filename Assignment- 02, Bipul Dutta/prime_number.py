
# Assignment No: 02,      Date: 19.05.2022
# Find out the prime numbers and add the numbers.

lower_number = int(input("Enter the lower number: "))
upper_number = int(input("Enter the upper number: "))
total = 0

for num in range(lower_number, upper_number + 1):
    count = 0
    for i in range(2, (num // 2 + 1)):      #In Python, the double-backslash operator (//) is the floor division operator.
        if num %i ==0:                      # Floor division means dividing and rounding down to the nearest integer.
            count = count + 1
            break                           # 0 will print form the start in the program, but it won't affect the program.

    if (count == 0 and num != 1):
        print(" %d" %num, end= " ")
        total = total + num
print("\n Total Sum of the Prime Numbers:", total )

# Output:
# Enter the lower number: 1
# Enter the upper number: 99
#  2  3  5  7  11  13  17  19  23  29  31  37  41  43  47  53  59  61  67  71  73  79  83  89  97
#  Total Sum of the Prime Numbers: 1060