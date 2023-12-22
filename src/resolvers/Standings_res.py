from database.models import Standings
from database.db_manager import base_manager

def get(Standing_ID: int) -> dict:
    res = base_manager.execute(query="""SELECT * FROM Standings WHERE ID = ?""",
                             args=(Standing_ID,))
    return res


def get_all() -> dict:
    res = base_manager.execute(query="""SELECT * FROM Standings""",
                             many=True)
    return res


def new(Standing: Standings) -> dict:
    res = base_manager.execute(query="""INSERT INTO Standings(Race_ID, Driver_ID, Position, Points) 
                                       VALUES(?, ?, ?, ?)
                                       RETURNING ID""",
                             args=(Standing.Race_ID, Standing.Driver_ID, Standing.Position, Standing.Points))
    return res


def update(Standing: Standings) -> dict:
    res = base_manager.execute(query="""UPDATE Standings
                                        SET Position = ?
                                        WHERE ID = ?""",
                             args=(Standing.Position, Standing.ID))
    return res


def delete(Standing_ID: int) -> dict:
    res = base_manager.execute(query="""DELETE FROM Standings WHERE ID = ?""",
                             args=(Standing_ID,))
    return res