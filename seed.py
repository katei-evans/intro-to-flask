from models import User, db, Post
from app import app

with app.app_context():
    print("Seeding users...")

    Katei = User(first_name ="Katei", middle_name='Kaji', last_name='Caleb', username='katei')
    Abigael = User(first_name ="Nelly", middle_name='sherlyn', last_name='Abigael', username='Aby')

    db.session.add_all([Katei, Abigael])
    db.session.commit()

    print('sending posts...')
    p1 = Post(post_title='adventure', post_content='hiking mountains', user='Katei')
    p2 = Post(post_title='reading', post_content='novels to read', user='Abigael')

    db.session.add_all([p1, p2])
    db.session.commit()



