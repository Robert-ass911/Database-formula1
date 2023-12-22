import fastapi

from database.models import Teams
from resolvers import Teams_res


Teams_router = fastapi.APIRouter(prefix='/Teams', tags=["Teams"])


@Teams_router.get(path='/get/{Teams_ID}', response_model=dict)
def get_Team(Teams_ID: int) -> dict:
    return Teams_res.get(Team_ID = Teams_ID)

@Teams_router.get(path='/get', response_model=dict)
def get_Teams() -> dict:
    return Teams_res.get_all()

@Teams_router.post(path='/new', response_model=dict)
def new_Team(Team: Teams) -> dict:
    return Teams_res.new(Team = Team)

@Teams_router.put(path='/updateTeam_Name/{Teams_ID}', response_model=dict)
def update_Team_Name(Team: Teams) -> dict:
    return Teams_res.update_Team_Name(Team = Team)

@Teams_router.delete(path='/delete/{Teams_ID}', response_model=dict)
def delete_Team(Team_ID: int) -> dict:
     return Teams_res.delete(Team_ID = Team_ID)