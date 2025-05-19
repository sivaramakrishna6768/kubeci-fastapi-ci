from app.models import User

fake_user_db = []

def get_users():
    return fake_user_db

def add_user(user: User):
    fake_user_db.append(user)
    return user
