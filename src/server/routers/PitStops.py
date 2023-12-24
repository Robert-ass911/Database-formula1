import fastapi

from database.models import PitStops
from resolvers import PitStops_res


PitStops_router = fastapi.APIRouter(prefix='/PitStops', tags=["PitStops"])


@PitStops_router.get(path='/get/{PitStops_ID}', response_model=dict)
def get_PitStop(PitStops_ID: int) -> dict:
    return PitStops_res.get(PitStop_ID = PitStops_ID)

@PitStops_router.get(path='/get', response_model=dict)
def get_PitStops() -> dict:
    return PitStops_res.get_all()

@PitStops_router.post(path='/new', response_model=dict)
def new_PitStop(PitStop: PitStops) -> dict:
    return PitStops_res.new(PitStop = PitStop)

@PitStops_router.put(path='/updatePitstop_Time/{PitStops_ID}', response_model=dict)
def update_Pitstop_Time(PitStop: PitStops) -> dict:
    return PitStops_res.update(PitStop = PitStop)

@PitStops_router.delete(path='/delete/{PitStops_ID}', response_model=dict)
def delete_PitStop(PitStop_ID: int) -> dict:
     return PitStops_res.delete(PitStop_ID = PitStop_ID)