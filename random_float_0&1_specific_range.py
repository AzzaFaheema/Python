import random

random_float_0_to_1 = random.random()
print("Random float betwen 0 and 1 is", random_float_0_to_1)
start_range=int(input("Enter starting range"))
end_range=int(input("Enter ending range"))
random_float_in_range = random.uniform(start_range, end_range)
print("Random float between", start_range, "and", end_range, ":", random_float_in_range)

OUTPUT

Random float betwen 0 and 1 is 0.3067250428590902
Enter starting range5
Enter ending range10
Random float between 5 and 10 : 7.733029447682052
