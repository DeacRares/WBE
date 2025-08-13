import json

class WeaponBall:
    def __init__(self,name):
        self.name = name
        self.elo = 1000
        self.wins = 0
        self.loses = 0

    def display(self):
        print(f'{self.name} - elo : {self.elo} - record : {self.wins}{self.loses}')
        return f'{self.name} - elo : {self.elo} - record : {self.wins}{self.loses}\n\n'

competitors = {}
data = {}
final_list = []

def elo_change(winner_rating, loser_rating, k=64):
    expected_winner = 1 / (1 + 10 ** ((loser_rating - winner_rating) / 400))
    change = k * (1 - expected_winner)
    return int(round(change))


def init_competitors():
    for value in data.values():
        for ball in value.values():
            if ball not in competitors:
                competitors[ball] = WeaponBall(ball)

def elo_determination():
    for value in data.values():
        change = elo_change(competitors[value['winner']].elo,competitors[value['loser']].elo)
        competitors[value['winner']].elo +=change
        competitors[value['winner']].wins += 1
        competitors[value['loser']].elo =max(competitors[value['loser']].elo-change, 100)
        competitors[value['loser']].loses -= 1

def sort_the_list():
    lst = []
    for value in competitors.values():
        lst.append(value)
    lst.sort(key=lambda x: x.elo)
    return lst

def display():
    idx = 1
    text = ''
    for ball in reversed(final_list):  # reverse the order
        print(f'nr {idx} : ', end='')
        text += f'           nr {idx} : ' + ball.display()
        idx += 1

    file_path = 'rank.txt'

    with open(file_path, 'w') as file:
        file.write(text)

if __name__=='__main__':

    with open('data.json', 'r') as file:
        data = json.load(file)

    init_competitors()
    elo_determination()
    final_list = sort_the_list()
    display()

