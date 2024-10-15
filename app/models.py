from . import db

class Herb(db.Model):
    __tablename__ = 'herbs'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    advantages = db.Column(db.ARRAY(db.String), nullable=False)
    image = db.Column(db.String(255))
    comments = db.Column(db.ARRAY(db.String), default=[])
