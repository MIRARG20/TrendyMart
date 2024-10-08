from market import db

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=40), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=70), nullable=False, unique=True)
    items = db.relationship('Item', backref='owend_user', lazy=True)

# Define the Item model
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))


    # String representation of the Item instance
    def __repr__(self):
        return f'Item {self.name}'