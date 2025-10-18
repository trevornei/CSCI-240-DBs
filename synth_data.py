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
      first_name = faker.first_name()
      last_name = faker.last_name()
      username = faker.user_name()
      print(f"""
          First_Name = {first_name}
          Last_Name = {last_name}
          username = {username}
      """)

generate_users()
