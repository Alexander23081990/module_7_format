team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
team1_time = 1552.512
team2_time = 2153.31451
score_1 = 40
score_2 = 42


def num():
    print('В команде %s, %s участников' % (team1, team1_num))
    print('Итого в командах сегодня участников: %s и %s' % (team1_num, team2_num))


def task():
    print('Команда {} решила задач: {}'.format(team2, score_2))


def time():
    print('{} решили задачи за {}c'.format(team2, team2_time))


def score():
    print(f'Команды решили {score_1} и {score_2} задач.')
    if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
        result = f'Результат битвы: победа команды {team1}!'
    elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
        result = f'Результат битвы: победа команды {team2}!'
    else:
        result = 'Ничья!'
    return print(result)


def total():
    total_score = score_1 + score_2
    time_avg = (team1_time + team2_time) / 2
    print(f'Сегодня было решено {total_score} задач, в среднем по {time_avg} секунды на задачу!')


num()
task()
time()
score()
total()
