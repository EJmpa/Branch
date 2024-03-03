from app.models import Customer, db

def update_customer_username(customer_id, new_username):
    customer = Customer.query.get(customer_id)
    if customer:
        customer.username = new_username
        db.session.commit()
        return True
    else:
        return False