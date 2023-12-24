from database.models import Drivers
from database.db_manager import base_manager

def get(Driver_ID: int) -> dict:
    res = base_manager.execute(query="""SELECT * FROM Drivers WHERE ID = ?""",
                             args=(Driver_ID,))
    return res


def get_all() -> dict:
    res = base_manager.execute(query="""SELECT * FROM Drivers""",
                             many=True)
    return res


def new(Driver: Drivers) -> dict:
    res = base_manager.execute(query="""INSERT INTO Drivers(Team_ID, Driver_Name) 
                                       VALUES(?, ?)
                                       RETURNING ID""",
                             args=(Driver.Team_ID, Driver.Driver_Name))
    return res


def update(Driver: Drivers) -> dict:
    res = base_manager.execute(query="""UPDATE Drivers
                                        SET Driver_Name = ?
                                        WHERE ID = ?""",
                             args=(Driver.Driver_Name, Driver.ID))
    return res


def delete(Driver_ID: int) -> dict:
    res = base_manager.execute(query="""DELETE FROM Drivers WHERE ID = ?""",
                             args=(Driver_ID,))
    return res