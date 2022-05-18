W = 'W'
MP = 'MP'
D = 'D'
L = 'L'
P = 'P'
WIN_SCORE = 3
DRAW_SCORE = 1
LOSS_SCORE = 0
HEADER = f'Team                           | {MP} |  {W} |  {D} |  {L} |  {P}'


def format_result(team, team_dict):
    return (f'{team: <31}| '
            f'{team_dict[team][MP]:>2} | '
            f'{team_dict[team][W]: >2} | '
            f'{team_dict[team][D]: >2} | '
            f'{team_dict[team][L]: >2} | '
            f'{team_dict[team][P]: >2}')


def tally(rows: list):
    teams_dict = dict()
    for row in rows:
        first_team, second_team, situation = row.split(';')
        if first_team not in teams_dict:
            teams_dict[first_team] = {W: 0, L: 0, MP: 0, D: 0, P: 0}
        if second_team not in teams_dict:
            teams_dict[second_team] = {W: 0, L: 0, MP: 0, D: 0, P: 0}
        if situation == 'win':
            teams_dict[first_team][W] += 1
            teams_dict[second_team][L] += 1
            teams_dict[first_team][P] += WIN_SCORE
            teams_dict[second_team][P] += LOSS_SCORE
        elif situation == 'loss':
            teams_dict[second_team][W] += 1
            teams_dict[first_team][L] += 1
            teams_dict[second_team][P] += WIN_SCORE
            teams_dict[first_team][P] += LOSS_SCORE
        elif situation == 'draw':
            teams_dict[first_team][D] += 1
            teams_dict[second_team][D] += 1
            teams_dict[first_team][P] += DRAW_SCORE
            teams_dict[second_team][P] += DRAW_SCORE
        teams_dict[first_team][MP] += 1
        teams_dict[second_team][MP] += 1
    results = [format_result(team, teams_dict) for team in teams_dict]
    # To sort the results by score REVERSED
    #  and then break ties, you sort a list by alphabet,
    # Then, since it has partially the order you need
    # you apply the score sort.
    results.sort(key=lambda x: x.split('|')[0])
    results.sort(key=lambda x: x.split('|')[-1], reverse=True)
    return [HEADER] + results
