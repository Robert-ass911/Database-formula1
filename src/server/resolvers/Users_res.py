from database.models import Users
from database.db_manager import base_manager

def get(User_ID: int) -> dict:
    res = base_manager.execute(query="""SELECT * FROM Users WHERE ID = ?""",
                             args=(User_ID,))
    return res


def get_all() -> dict:
    res = base_manager.execute(query="""SELECT * FROM Users""",
                             many=True)
    return res


def new(User: Users) -> dict:
    res = base_manager.execute(query="""INSERT INTO Users(Position, Login, Password, Power_level) 
                                       VALUES(?, ?, ?, ?)
                                       RETURNING ID""",
                             args=(User.Position, User.Login, User.Password, User.Power_level))
    return res


def update_Password(User: Users) -> dict:
    res = base_manager.execute(query="""UPDATE Users
                                        SET Password = ?
                                        WHERE ID = ?""",
                             args=(User.Password, User.ID))
    return res


def delete(User_ID: int) -> dict:
    res = base_manager.execute(query="""DELETE FROM Users WHERE ID = ?""",
                             args=(User_ID,))
    return res