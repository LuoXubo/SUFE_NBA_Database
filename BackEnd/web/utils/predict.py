from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np


def predictAll(data):
    result = {
        'season': '22-23',
        'team': data[0].get('team')
    }
    time_list = []
    hit_percentage_list = []
    shot_number_list = []
    three_point_hit_percentage_list = []
    three_point_shot_number_list = []
    penalty_hit_percentage_list = []
    penalty_shot_number_list = []
    total_rebounds_list = []
    assists_list = []
    snatch_list = []
    blocks_list = []
    foul_list = []
    score_list = []
    all_list = [
        time_list,
        hit_percentage_list,
        shot_number_list,
        three_point_hit_percentage_list,
        three_point_shot_number_list,
        penalty_hit_percentage_list,
        penalty_shot_number_list,
        total_rebounds_list,
        assists_list,
        snatch_list,
        blocks_list,
        foul_list,
        score_list
    ]
    name_list = [
        'time',
        'hit_percentage',
        'shot_number',
        'three_point_hit_percentage',
        'three_point_shot_number',
        'penalty_hit_percentage',
        'penalty_shot_number',
        'total_rebounds',
        'assists',
        'snatch',
        'blocks',
        'foul',
        'score'
    ]
    x = []
    num = 0
    for player_data in data:
        num += 1
        x.append(num)
        time_list.append(player_data.get('time'))
        hit_percentage_list.append(player_data.get('hit_percentage'))
        shot_number_list.append(player_data.get('shot_number'))
        three_point_hit_percentage_list.append(player_data.get('three_point_hit_percentage'))
        three_point_shot_number_list.append(player_data.get('three_point_shot_number'))
        penalty_hit_percentage_list.append(player_data.get('penalty_hit_percentage'))
        penalty_shot_number_list.append(player_data.get('penalty_shot_number'))
        total_rebounds_list.append(player_data.get('total_rebounds'))
        assists_list.append(player_data.get('assists'))
        snatch_list.append(player_data.get('snatch'))
        blocks_list.append(player_data.get('blocks'))
        foul_list.append(player_data.get('foul'))
        score_list.append(player_data.get('score'))
    index = 0
    x = np.array(x)
    x = x.reshape(-1, 1)
    poly = PolynomialFeatures(degree=2)
    poly.fit(x)
    x_new = poly.transform(x)
    x_predict = [num + 1, ]
    x_predict = np.array(x_predict)
    x_predict = x_predict.reshape(-1, 1)
    x_predict_new = poly.transform(x_predict)
    for predictor in all_list:
        lr = LinearRegression()
        lr.fit(x_new, predictor)
        predict_result = lr.predict(x_predict_new)
        result[name_list[index]] = predict_result[0]
        index += 1
    return result
