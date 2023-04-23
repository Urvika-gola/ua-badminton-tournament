from app import db

"""
Class Result, stores the result corresponding to a Match
"""


class Result(db.Model):
    __tablename__ = "result"
    result_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    result_name = db.Column(db.String(20), nullable=True)  # result obtained, results awaiting etc.
    result_score = db.Column(db.String(30), nullable=True)
    winner_player_1 = db.Column(db.Integer, db.ForeignKey('player.player_id'), nullable=False)
    winner_player_2 = db.Column(db.Integer, db.ForeignKey('player.player_id'), nullable=True)
    players = db.relationship("Player", backref="results", lazy=True)
    matches = db.relationship("Match", backref="result", lazy=True)

    def __init__(self, result_name: str = None, result_score: str = None, winner_player_1: int = None,
                 winner_player_2: int = None) -> None:
        """
        Initialize a Result object with the given attributes.
        result_name: The name of the result (optional).
        result_score: The score of the result (optional).
        """
        self.result_name = result_name
        self.result_score = result_score
        self.winner_player_1 = winner_player_1
        self.winner_player_2 = winner_player_2

    def __repr__(self) -> str:
        """Return a string representation of the Result object."""
        return f"<Result {self.result_name}, Result score {self.result_score}, Winner player 1 {self.winner_player_1}," \
               f"Winner player 2 {self.winner_player_2}>"
