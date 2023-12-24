import fastapi

from database.models import Users
from resolvers import Users_res


Users_router = fastapi.APIRouter(prefix='/Users', tags=["Users"])


@Users_router.get(path='/get/{Users_ID}', response_model=dict)
def get_User(Users_ID: int) -> dict:
    return Users_res.get(User_ID = Users_ID)

@Users_router.get(path='/get', response_model=dict)
def get_Users() -> dict:
    return Users_res.get_all()

@Users_router.post(path='/new', response_model=dict)
def new_User(User: Users) -> dict:
    return Users_res.new(User = User)

@Users_router.put(path='/updatePassword/{Users_ID}', response_model=dict)
def update_Password(User: Users) -> dict:
    return Users_res.update_Password(User = User)

@Users_router.delete(path='/delete/{Users_ID}', response_model=dict)
def delete_User(User_ID: int) -> dict:
     return Users_res.delete(User_ID = User_ID)