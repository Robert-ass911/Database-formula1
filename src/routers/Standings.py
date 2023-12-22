import fastapi

from database.models import Standings
from resolvers import Standings_res


Standings_router = fastapi.APIRouter(prefix='/Standings', tags=["Standings"])


@Standings_router.get(path='/get/{Standings_ID}', response_model=dict)
def get_Standing(Standings_ID: int) -> dict:
    return Standings_res.get(Standing_ID = Standings_ID)

@Standings_router.get(path='/get', response_model=dict)
def get_Standings() -> dict:
    return Standings_res.get_all()

@Standings_router.post(path='/new', response_model=dict)
def new_Standing(Standing: Standings) -> dict:
    return Standings_res.new(Standing = Standing)

@Standings_router.put(path='/updatePosition/{Standings_ID}', response_model=dict)
def update_Position(Standing: Standings) -> dict:
    return Standings_res.update(Standing = Standing)

@Standings_router.delete(path='/delete/{Standings_ID}', response_model=dict)
def delete_Standing(Standing_ID: int) -> dict:
     return Standings_res.delete(Standing_ID = Standing_ID)