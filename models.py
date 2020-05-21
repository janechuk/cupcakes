"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
DEFAULT_IMAGE_URL = "https://tinyurl.com/demo-cupcake"


def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):

    """Models for Blogly."""
    __tablename__ = 'cupcakes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    def __repr__(self):
        """Show info about user"""

        c = self
        return f"<User {c.id} {c.flavor } {c.size} {c.image} {c.rating}>"