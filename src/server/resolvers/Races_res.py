from database.models import Races
from database.db_manager import base_manager

def get(Race_ID: int) -> dict:
    res = base_manager.execute(query="""SELECT * FROM Races WHERE ID = ?""",
                             args=(Race_ID,))
    return res


def get_all() -> dict:
    res = base_manager.execute(query="""SELECT * FROM Races""",
                             many=True)
    return res


def new(Race: Races) -> dict:
    res = base_manager.execute(query="""INSERT INTO Races(Race_Name, Date, Location) 
                                       VALUES(?, ?, ?)
                                       RETURNING ID""",
                             args=(Race.Race_Name, Race.Date, Race.Location))
    return res


def update(Race: Races) -> dict:
    res = base_manager.execute(query="""UPDATE Races
                                        SET Location = ?
                                        WHERE ID = ?""",
                             args=(Race.Location, Race.ID))
    return res


def delete(Race_ID: int) -> dict:
    res = base_manager.execute(query="""DELETE FROM Races WHERE ID = ?""",
                             args=(Race_ID,))
    return res