total_seconds = int(input("Enter an integer for seconds: "))
minute = total_seconds // 60
second = total_seconds % 60
print("{0:d} seconds is {1:d} minutes and {2:d} seconds".format(total_seconds, minute, second))
