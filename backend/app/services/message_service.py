from app.models import Message, db

def send_message(customer_id, agent_id, content):
    new_message = Message(
        customer_id=customer_id,
        agent_id=agent_id,
        content=content
        )
    db.session.add(new_message)
    try:
        db.session.commit()
        return new_message
    except Exception as e:
        db.session.rollback()
        print(f"Error sending message: {e}")
        return None

def respond_to_message(agent_id, message_id, content):
    message = Message.query.get(message_id)
    if message is None:
        return None
    agent_id = int(agent_id)
    if message.agent_id == agent_id:
        new_response = Message(
            customer_id=message.customer_id,
            agent_id=agent_id,
            content=content
            )
        db.session.add(new_response)
        try:
            db.session.commit()
            return new_response
        except Exception as e:
            db.session.rollback()
            print(f"Error responding to message: {e}")
            return None
    return None    

def get_messages(customer_id, agent_id):
    messages = Message.query.filter(
        (Message.customer_id == customer_id) & (Message.agent_id == agent_id) |
        (Message.customer_id == agent_id) & (Message.agent_id == customer_id)
    ).all()
    return messages

def delete_message(message_id):
    message = Message.query.get(message_id)
    if message:
        db.session.delete(message)
        try:
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting message: {e}")
            return False
    else:
        return False
    
def update_message(message_id, content):
    message = Message.query.get(message_id)
    if message:
        message.content = content
        try:
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error updating message: {e}")
            return False
    else:
        return False