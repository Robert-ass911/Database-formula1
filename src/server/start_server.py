from database.db_manager import base_manager
import settings
import uvicorn
from fastapi import FastAPI
from routers import Races, Teams, Drivers, PitStops, Laps, Standings, Users
from fastapi.responses import RedirectResponse

app = FastAPI(title='formula')

app.include_router(Races.Races_router)
app.include_router(Teams.Teams_router)
app.include_router(Drivers.Drivers_router)
app.include_router(PitStops.PitStops_router)
app.include_router(Laps.Laps_router)
app.include_router(Standings.Standings_router)
app.include_router(Users.Users_router)

@app.router.get('/')
def start_page() -> RedirectResponse:
    return RedirectResponse('/docs')

if __name__ == "__main__":
    uvicorn.run(app='start_server:app', reload=True, host=settings.HOST, port=settings.PORT)