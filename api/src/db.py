from sqlmodel import Session, SQLModel, create_engine, select
from models import User, Game, UserUpdate, Transaction
from datetime import date
from typing import Optional, List
from datetime import date

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


def create_user(session: Session, user: User) -> int | None:
    """
    Create a new user in the database

    Parameters:
        session: Session - the active database session
        user: UserCreate - Data to create a new user

    Returns:
        id: int - Newly created user's id
    """
    user.id = None

    session.add(user)  #asks session to add user to database
    session.commit()

    return user.id

def user_exists(session: Session, username: str) -> bool:
    """
    Checks if a given username has been used by any user in 
    the database

    parameters: 
        session: Session - the active database session
        username: str - username to be checked

    returns:
        bool
    """

    statement = select(User).where(User.username == username)
    result = session.exec(statement)

    return result.first() is not None


def get_user_by_id(session: Session, user_id: int) -> Optional[User]:
    """
    fetch the user identified by user_id from the database

    parameters:
        session: Session - the active database session
        user_id: int - primary key identifying the user

    returns:
        Optional[User] - User object if found, None otherwise
    """ 
    ...
    statement = select(User).where(User.id == user_id)
    result = session.exec(statement).first()

    if result:
        return result
    return None

def get_user_by_username(session: Session, username: str) -> Optional[User]:
    """
    fetch the user identified by username from the database

    parameters:
        session: Session - the active database session
        username: str - username identifying the user

    returns:
        Optional[User] - User object if found, None otherwise
    """ 
    statement = select(User).where(User.username == username)
    result = session.exec(statement).first()
    return result 

def update_user(session: Session, user_id: int, user_update: UserUpdate, game: str="") -> Optional[User]:
    """
    Update an existing user in the database.

    Parameters:
        session: Session - the active database session
        user_id: int - ID of the user to update
        user_update: UserUpdate - Data to update the user

    Returns:
        Optional[User] - Updated user object if found and updated, None otherwise
    """
    ...
    user = get_user_by_id(session, user_id)

    if not user:
        return None

    if user_update.username:
        user.username = user_update.username
        
    if user_update.password:
        user.password = user_update.password
        
    if user_update.credits:
        transaction = Transaction(
            user_id=user_id,
            game=game,
            amount=user_update.credits,
            date=date.today()
        )
        store_transaction(session, transaction) 
        
        user.credits += user_update.credits
    
    session.add(user)
    session.commit()
    session.refresh(user)

def delete_user(session: Session, user_id: int) -> Optional[User]:
    """
    delete a user from the database

    Parameters:
        session: Session - the active database session
        user_id: int - ID of the user to delete

    Returns:
        Optional[User] - Deleted user object if found and deleted, None otherwise
    """
    ...
    statement = select(User).where(User.id == user_id)
    result = session.exec(statement)
    user = result.one()

    session.delete(user)
    session.commit()

def get_transaction_by_id(session: Session, trans_id: int) ->Optional[Transaction]:
    """
    fetch the transaction by its id number from the database

    Parameters:
        session: Session - the active database session
        trans_id: int - ID of the sought transaction

    Returns:
        Optional[Transaction] - Transaction object if found, None otherwise
    """
    ...
    statement = select(Transaction).where(Transaction.transaction_id == trans_id)
    result = session.exec(statement).first()

    if result:
        return result
    return None

def store_transaction(session: Session, transaction: Transaction) -> int | None:
    """
    Create a new transaction in the database

    Parameters:
        session: Session - the active database session
        transaction: TransactionCreate - Data to create a new Transaction

    Returns:
        id: int - Newly created transaction id
    """
    transaction.id = None

    session.add(transaction)
    session.commit()

    return transaction.id

def get_transactions_query(session: Session, date: date, player_id: int, game: str) -> List[Transaction]:
    """
    Fetch transactions by a specific date and player from the database

    Parameters:
        session: Session - the active database session
        date: date - the date to filter transactions
        player_id: int - ID of the player

    Returns:
        List[Transaction] - List of transactions matching the date and player
    """
    
    # statement = select(Transaction).where(
    #     Transaction.date == date & Transaction.user_id == player_id & Transaction.game == game
    # )
    statement = select(Transaction).where(
        (Transaction.date == date) & (Transaction.user_id == player_id) & (Transaction.game == game)
    )
    result = session.exec(statement).all()
    print(result)
    return result

# def get_game(session: Session=None, game_id: int) -> Game:
#     """
#     fetch the game identified by game_id from the database
#
#     parameters:
#         session: Session - the active database session
#         game_id: int - primary key identifying the game 
#
#     returns:
#         Game 
#     """ 
#     ...
#
