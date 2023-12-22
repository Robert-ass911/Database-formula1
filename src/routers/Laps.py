import fastapi

from database.models import Laps
from resolvers import Laps_res


Laps_router = fastapi.APIRouter(prefix='/Laps', tags=["Laps"])


@Laps_router.get(path='/get/{Laps_ID}', response_model=dict)
def get_Lap(Laps_ID: int) -> dict:
    return Laps_res.get(Lap_ID = Laps_ID)

@Laps_router.get(path='/get', response_model=dict)
def get_Laps() -> dict:
    return Laps_res.get_all()

@Laps_router.post(path='/new', response_model=dict)
def new_Lap(Lap: Laps) -> dict:
    return Laps_res.new(Lap = Lap)

@Laps_router.put(path='/updateLap_Time/{Laps_ID}', response_model=dict)
def update_Lap_Time(Lap: Laps) -> dict:
    return Laps_res.update(Lap = Lap)

@Laps_router.delete(path='/delete/{Laps_ID}', response_model=dict)
def delete_Lap(Lap_ID: int) -> dict:
     return Laps_res.delete(Lap_ID = Lap_ID)