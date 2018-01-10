from datetime import datetime

seed= datetime.now().microsecond
rand_max=int(raw_input("Enter the maximum random number you want to generate(less than 32749)"))
count=int(raw_input("Enter count of random number you want to generate"))
for i in range(count):
    seed = (seed * 32719 + 3) % 32749
    print seed%rand_max

