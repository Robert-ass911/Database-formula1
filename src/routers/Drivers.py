import fastapi

from database.models import Drivers
from resolvers import Drivers_res


Drivers_router = fastapi.APIRouter(prefix='/Drivers', tags=["Drivers"])


@Drivers_router.get(path='/get/{Drivers_ID}', response_model=dict)
def get_Driver(Drivers_ID: int) -> dict:
    return Drivers_res.get(Driver_ID = Drivers_ID)

@Drivers_router.get(path='/get', response_model=dict)
def get_Drivers() -> dict:
    return Drivers_res.get_all()

@Drivers_router.post(path='/new', response_model=dict)
def new_Driver(Driver: Drivers) -> dict:
    return Drivers_res.new(Driver = Driver)

@Drivers_router.put(path='/updateDriver_Name/{Drivers_ID}', response_model=dict)
def update_Driver_Name(Driver: Drivers) -> dict:
    return Drivers_res.update(Driver = Driver)

@Drivers_router.delete(path='/delete/{Drivers_ID}', response_model=dict)
def delete_Driver(Driver_ID: int) -> dict:
     return Drivers_res.delete(Driver_ID = Driver_ID)