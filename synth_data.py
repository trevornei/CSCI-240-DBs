from faker import Faker

faker = Faker()

# gen_name = faker.name()
# print(f"Testing out creating a fake name: {gen_name}")

"""
For Users & Feeds
1 Create for loop that iterates to 10
2 for each iterate call faker.methods() to generate synthetic data.
3 sequentially append the data so that it conforms to the data model. 
"""

# Create a list of dictionaries for user and key value pairs that map to the data model. 

users = []

def generate_users():
  for i in range(10):
      fn = faker.first_name()
      ln = faker.last_name()
      un = faker.user_name()
      user_dict = {
        "first_name": fn, 
        "last_name":  ln,
        "username":  un
      }

      users.append(user_dict)

'''
      print(f"""
          First_Name = {fn}
          Last_Name = {ln}
          username = {un}
      """)
'''
generate_users()
print(users)

