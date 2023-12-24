from pydantic import BaseModel
from datetime import datetime


class Races(BaseModel):
    ID : int
    Race_Name : str
    Date : datetime
    Location : str

class Teams(BaseModel):
    ID : int
    Team_Name : str
    Team_Principal : str

class Drivers(BaseModel):
    ID : int
    Team_ID : int
    Driver_Name : str

class PitStops(BaseModel):
    ID : int
    Race_ID : int
    Driver_ID : int
    Pitstop_Time : datetime

class Laps(BaseModel):
    ID : int
    Race_ID : int
    Driver_ID : int
    Lap_Time : datetime

class Standings(BaseModel):
    ID : int
    Race_ID : int
    Driver_ID : int
    Position : int
    Points : int

class Users (BaseModel):
    ID : int
    Position :str
    Login :str
    Password :str
    Power_level : int