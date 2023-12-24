from database.models import Laps
from database.db_manager import base_manager

def get(Lap_ID: int) -> dict:
    res = base_manager.execute(query="""SELECT * FROM Laps WHERE ID = ?""",
                             args=(Lap_ID,))
    return res


def get_all() -> dict:
    res = base_manager.execute(query="""SELECT * FROM Laps""",
                             many=True)
    return res


def new(Lap: Laps) -> dict:
    res = base_manager.execute(query="""INSERT INTO Laps(Race_ID, Driver_ID, Lap_Time) 
                                       VALUES(?, ?, ?)
                                       RETURNING ID""",
                             args=(Lap.Race_ID, Lap.Driver_ID, Lap.Lap_Time))
    return res


def update(Lap: Laps) -> dict:
    res = base_manager.execute(query="""UPDATE Laps
                                        SET Lap_Time = ?
                                        WHERE ID = ?""",
                             args=(Lap.Lap_Time, Lap.ID))
    return res


def delete(Lap_ID: int) -> dict:
    res = base_manager.execute(query="""DELETE FROM Laps WHERE ID = ?""",
                             args=(Lap_ID,))
    return res