from faker import Faker

fake= Faker()

class Payloads:
    create_user= {
        "email": fake.email(),
        "password": fake.password(length=10),
        "name": fake.name(),
        "nickname": fake.user_name()
    }



