from faker import Faker

faker = Faker()

gen_name = faker.name()
print(f"Testing out creating a fake name: {gen_name}")
