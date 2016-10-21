print(1 == 2) # Expected output: False

print(1 > 2) # Expected output: False

print(2 > 1) # Expected output: True

print(1 >= 1) # Expected output: True

print(2 == 2) # Expected output:True

print(2 != 2) # Expected output: False

age = 30

print(age > 10) # Expected outcome: True

print(10 < age) # Expected outcome: True

print(age > 10 + 20) # Expected outcome: False

print(age + 20 > 10) # Expected outcome: True
age = 1
print(age > 12 and age < 19) # Expected outcome:

age = 14
print(age > 12 and age < 19) # Expected outcome: True

age = 19
print(age > 12 and age < 19) # Expected outcome: False

age = 18
print(age > 12 and age < 19 and age != 5) # Expected outcome: True

age = 5
print(age > 12 and age < 19 and age != 5) # Expected outcome: False

age = -1
print(age > 12 and age < 19) # Expected outcome: False

age = 10
print(age > 25 and age < 15) # Expected outcome:    False
# Could the above expression ever be True?
