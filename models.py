# models.py
from app import db


class AIModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"AIModel('{self.name}', '{self.description}')"
