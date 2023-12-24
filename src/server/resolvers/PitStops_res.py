from database.models import PitStops
from database.db_manager import base_manager

def get(PitStop_ID: int) -> dict:
    res = base_manager.execute(query="""SELECT * FROM PitStops WHERE ID = ?""",
                             args=(PitStop_ID,))
    return res


def get_all() -> dict:
    res = base_manager.execute(query="""SELECT * FROM PitStops""",
                             many=True)
    return res


def new(PitStop: PitStops) -> dict:
    res = base_manager.execute(query="""INSERT INTO PitStops(Race_ID, Driver_ID, Pitstop_Time) 
                                       VALUES(?, ?, ?)
                                       RETURNING ID""",
                             args=(PitStop.Race_ID, PitStop.Driver_ID, PitStop.Pitstop_Time))
    return res


def update(PitStop: PitStops) -> dict:
    res = base_manager.execute(query="""UPDATE PitStops
                                        SET Pitstop_Time = ?
                                        WHERE ID = ?""",
                             args=(PitStop.Pitstop_Time, PitStop.ID))
    return res


def delete(PitStop_ID: int) -> dict:
    res = base_manager.execute(query="""DELETE FROM PitStops WHERE ID = ?""",
                             args=(PitStop_ID,))
    return res