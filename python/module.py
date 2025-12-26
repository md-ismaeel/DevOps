import datetime
from basic import xyz
from faker import Faker

faker = Faker()

# print(datetime.datetime.now())

# print(xyz.arr)


print(faker.email())
print(faker.address())
print(faker.text())
print(faker.company())
