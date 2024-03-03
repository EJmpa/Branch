from app.models import Customer, Agent
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


def authenticate_customer(username, password):
    customer = Customer.query.filter_by(username=username).first()
    if customer and check_password_hash(customer.password_hash, password):
        return customer
    return None

def authenticate_agent(username, password):
    agent = Agent.query.filter_by(username=username).first()
    if agent and check_password_hash(agent.password_hash, password):
        return agent
    return None

def create_customer(name, email, phone, username, password):
    password_hash = generate_password_hash(password)
    new_customer = Customer(customer_name=name, email=email, phone=phone, username=username, password_hash=password_hash)
    db.session.add(new_customer)
    try:
        db.session.commit()
        return new_customer
    except Exception as e:
        db.session.rollback()
        print(f"Error creating customer: {e}")
        return None

def create_agent(name, username, password):
    password_hash = generate_password_hash(password)
    new_agent = Agent(agent_name=name, username=username, password_hash=password_hash)
    db.session.add(new_agent)
    try:
        db.session.commit()
        return new_agent
    except Exception as e:
        db.session.rollback()
        print(f"Error creating agent: {e}")
        return None