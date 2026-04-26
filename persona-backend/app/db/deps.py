from app.db.database import get_session


def get_db():
    """
    Function to get db session
    """
    session = get_session()
    db = session()
    try:
        yield db
    finally:
        db.close()
