from models.tables.event import Event
from models.tables.login import Login
from models.tables.match import Match
from models.tables.permission import Permission
from models.tables.player import Player
from models.tables.result import Result
from models.tables.tournament import Tournament
from models.tables.user_permission import UserPermission
from models.tables.users import Users
from models.tables.players_event_seed import PlayersEventSeed


from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
