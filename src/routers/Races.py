import fastapi

from database.models import Races
from resolvers import Races_res


Races_router = fastapi.APIRouter(prefix='/Races', tags=["Races"])


@Races_router.get(path='/get/{Races_ID}', response_model=dict)
def get_Race(Races_ID: int) -> dict:
    return Races_res.get(Race_ID = Races_ID)

@Races_router.get(path='/get', response_model=dict)
def get_Races() -> dict:
    return Races_res.get_all()

@Races_router.post(path='/new', response_model=dict)
def new_Race(Race: Races) -> dict:
    return Races_res.new(Race = Race)

@Races_router.put(path='/updateLocation/{Races_ID}', response_model=dict)
def update_Location(Race: Races) -> dict:
    return Races_res.update(Race = Race)

@Races_router.delete(path='/delete/{Races_ID}', response_model=dict)
def delete_Race(Race_ID: int) -> dict:
     return Races_res.delete(Race_ID = Race_ID)