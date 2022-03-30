from ..api import ma
from ..models.battleship import Battleship


class BattleshipSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Battleship
