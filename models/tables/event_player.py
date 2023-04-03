from app import db

"""
Class representing the user-event interest table, with a many-to-many relationship between event & players.
An event can be played by many players, A player can play many events.
"""


class EventPlayer(db.Model):
    __tablename__ = 'event_player'
    event_id = db.Column(db.Integer, db.ForeignKey('match.match_id'), primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.player_id'), primary_key=True)

    def __repr__(self) -> str:
        """
        Returns a string representation of the EventPlayer object.
        """
        return f'<EventPlayer Event ID={self.event_id} - PlayerID={self.player_id}>'