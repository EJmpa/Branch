from datetime import datetime
from app import db

class Customer(db.Model):
    __tablename__ = 'customers'

    customer_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    customer_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Agent(db.Model):
    __tablename__ = 'agents'
    agent_id = db.Column(db.Integer, primary_key=True)
    agent_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Message(db.Model):
    __tablename__ = 'messages'
    message_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'))
    agent_id = db.Column(db.Integer, db.ForeignKey('agents.agent_id'))
    content = db.Column(db.Text, nullable=False)
    sent_at = db.Column(db.DateTime, default=datetime.utcnow)

    customers = db.relationship('Customer', backref='messages', foreign_keys=[customer_id])
    agents = db.relationship('Agent', backref='messages', foreign_keys=[agent_id])

    def to_dict(self):
        return {
            'message_id': self.message_id,
            'customer_id': self.customer_id,
            'agent_id': self.agent_id,
            'content': self.content,
            'sent_at': self.sent_at.isoformat() if self.sent_at else None,
        }
