from database.models import Teams
from database.db_manager import base_manager

def get(Team_ID: int) -> dict:
    res = base_manager.execute(query="""SELECT * FROM Teams WHERE ID = ?""",
                             args=(Team_ID,))
    return res


def get_all() -> dict:
    res = base_manager.execute(query="""SELECT * FROM Teams""",
                             many=True)
    return res


def new(Team: Teams) -> dict:
    res = base_manager.execute(query="""INSERT INTO Teams(Team_Name, Team_Principal) 
                                       VALUES(?, ?)
                                       RETURNING ID""",
                             args=(Team.Team_Name, Team.Team_Principal))
    return res


def update_Team_Name(Team: Teams) -> dict:
    res = base_manager.execute(query="""UPDATE Teams
                                        SET Team_Name = ?
                                        WHERE ID = ?""",
                             args=(Team.Team_Name, Team.ID))
    return res


def delete(Team_ID: int) -> dict:
    res = base_manager.execute(query="""DELETE FROM Teams WHERE ID = ?""",
                             args=(Team_ID,))
    return res