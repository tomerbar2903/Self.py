number_of_things_per_pig = int(input("Enter A 3-digit Number: "))
pig1 = number_of_things_per_pig % 10  # isolates right-most digit
pig2 = int(number_of_things_per_pig / 100)  # isolates left-most digit
pig3 = int(number_of_things_per_pig / 10) % 10  # isolates middle digit


sum_of_things = pig1 + pig2 + pig3

print(f"Total Amount Of Things: {sum_of_things}")
print(f"Average Per Pig: {int(sum_of_things / 3)}")
print(f"Remainder: {sum_of_things % 3}")
print(f"Can Be Fully Divided By The 3 Pigs? {sum_of_things % 3 == 0}")