from models.database import db
from models.models import Match
from models.tables.event import Event
from models.tables.player import Player
from models.tables.users import Users
from itertools import chain


def get_matches_details():
    db.session.expire_all()
    upcoming_matches = Match.query.filter_by(match_status='upcoming').all()
    in_progress_matches = Match.query.filter_by(match_status='in progress').all()
    finished_matches = Match.query.filter_by(match_status='finished').all()

    in_progress_match_details = []
    in_progress_and_upcoming_matches = chain(in_progress_matches, upcoming_matches)

    for match in in_progress_and_upcoming_matches:
        match_detail = {}
        match_detail['id'] = match.match_id
        match_detail['court_no'] = 0  # no court num in match
        event = Event.query.get(match.event_id)
        match_detail['event'] = event.event_name
        match_detail['event'] = match.event.event_name
        if match.result:
            match_detail['score'] = match.result.result_score
        else:
            match_detail['score'] = ''
        match_detail['status'] = 'In Progress'
        players_side_one = []
        for player_id in [match.side_one_player_1, match.side_one_player_2]:

            if player_id:
                player = Player.query.get(player_id)
                user = Users.query.get(player.player_id)
                player_name = f"{user.first_name} {user.last_name}"
                players_side_one.append(player_name)
                print(f"players_side_one - {players_side_one}")
        players_side_two = []
        for player_id in [match.side_two_player_1, match.side_two_player_2]:
            if player_id:
                player = Player.query.get(player_id)
                user = Users.query.get(player.player_id)
                player_name = f"{user.first_name} {user.last_name}"
                players_side_two.append(player_name)
                print(f"players_side_two - {players_side_two}")

        side_one_players = " , ".join(players_side_one[:2]) if len(players_side_one) == 2 else players_side_one[0]
        side_two_players = " , ".join(players_side_two[:2]) if len(players_side_two) == 2 else players_side_two[0]
        match_detail['match_up'] = f"{side_one_players} vs. {side_two_players}"
        in_progress_match_details.append(match_detail)

    finished_match_details = []
    for match in finished_matches:
        match_detail = {}
        match_detail['id'] = match.match_id
        match_detail['event'] = match.event.event_name
        match_detail['score'] = match.result.result_score
        match_detail['court_no'] = 0  # no court num in match
        match_detail['status'] = 'Finished'
        players_side_one = []
        for player_id in [match.side_one_player_1, match.side_one_player_2]:
            if player_id:
                player = Player.query.get(player_id)
                user = Users.query.get(player.player_id)
                player_name = f"{user.first_name} {user.last_name}"
                players_side_one.append(player_name)
                print(players_side_one)
        players_side_two = []
        for player_id in [match.side_two_player_1, match.side_two_player_2]:
            if player_id:
                player = Player.query.get(player_id)
                user = Users.query.get(player.player_id)
                player_name = f"{user.first_name} {user.last_name}"
                players_side_two.append(player_name)
                print(players_side_two)

        side_one_players = " , ".join(players_side_one[:2]) if len(players_side_one) == 2 else players_side_one[0]
        side_two_players = " , ".join(players_side_two[:2]) if len(players_side_two) == 2 else players_side_two[0]
        match_detail['match_up'] = f"{side_one_players} vs. {side_two_players}"

        winner_1 = Player.query.filter_by(player_id=match.result.winner_player_1).first()
        winner_1_user = Users.query.get(winner_1.player_id)
        winner_name = f"{winner_1_user.first_name} {winner_1_user.last_name}"

        if match.result.winner_player_2:
            winner_2 = Player.query.filter_by(player_id=match.result.winner_player_2).first()
            winner_2_user = Users.query.get(winner_2.player_id)
            winner_name += f" / {winner_2_user.first_name} {winner_2_user.last_name}"
        match_detail['winner'] = winner_name
        finished_match_details.append(match_detail)

    return {"in_progress_matches": in_progress_match_details, "finished_matches": finished_match_details}
'''
in_progress_matches = [
        {
            'id': 1,
            'court_no': '',
            'match_up': 'John-Rich',
            'event': 'MS',
            'score': '',
            'status': 'Not yet played'
        },
        {
            'id': 2,
            'court_no': '1',
            'match_up': 'Kimsila-Rossye',
            'event': 'WS',
            'score': '',
            'status': 'In-progress'
        },
        {
            'id': 3,
            'court_no': '2',
            'match_up': 'Jacob/John - Wrapel/Kimsila',
            'event': 'MD',
            'score': '',
            'status': 'In-progress'
        }
    ]
    finished_matches = [
        {
            'id': 1,
            'match_up': 'John-Derek',
            'event': 'MS',
            'score': '20-21',
            'winner': 'Derek'
        },
        {
            'id': 2,
            'match_up': 'Kimsila-Daisy',
            'event': 'WS',
            'score': '19-21',
            'winner': 'Daisy'
        },
        {
            'id': 3,
            'match_up': 'John - Jack',
            'event': 'MS',
            'score': '20-21',
            'winner': 'Jack'
        }
    ]
'''