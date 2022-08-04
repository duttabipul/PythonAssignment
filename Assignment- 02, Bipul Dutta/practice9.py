"""
dict1 = {
    'name' : 'Bipul',
    'dist' : 'Khulna'
}
print(dict1)
dict2 = {
    'mobile' : '0184563'
}
print(dict1,dict2)
adding = dict1['name'] + 'and' + dict2['mobile']
print(adding)

num = int(input("Enter number: "))
if num %2 ==0:
    print("Its a even number")
else:
    print("Its a odd number")

print("Enter a number: ")
num = int(input())
if num > 10:
    print("The number is greater than ten")
else:
    print("The number is less than ten")
"""
num = int(input("Enter num: "))
if num > 10:
    print("Number is greater than ten")
if num == 10:
    print("Number is equal to ten")
if num < 10:
    print("Number is less than ten")