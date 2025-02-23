from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Review, Customer

# Create an SQLite database (you can replace 'sqlite:///your_database.db' with your preferred database URL).
engine = create_engine('sqlite:///restaurants.db')

# Create the tables in the database.
Base.metadata.create_all(engine)

# Create a session to interact with the database.
Session = sessionmaker(bind=engine)
session = Session()
print("________________RESTAURANT______________")

# create restaurant instance
restaurant1 = session.query(Restaurant).first()

# Check if restaurant1 is not None before accessing its reviews
if restaurant1:
    print(restaurant1.reviews())
else:
    print("No restaurant found")

print("________________REVIEW______________")

# create Review instance
review1 = session.query(Review).first()

# Check if review1 is not None before accessing its attributes
if review1:
    print(review1.customer_id)
    res = review1.customer()
    print(res)
else:
    print("No review found")
