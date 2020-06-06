
# 各種入力
base_tile_cost = float(input('Tile Cost? (M) '))
surveyors_cost = int(input('Surveyors Cost? (M) '))
russia_empire = input('Russia Empire? [y/n] ')
while russia_empire not in ['y', 'n']:
    print(f'Russia Empire Value is Invalid {russia_empire}')
    russia_empire = input('Try Again: Russia Empire? [y/n] ')

# タイルのコスト倍率を数値で保存
tile_cost_ratio = 9 if russia_empire == 'y' else 10

# surveyorsの回数を計算
surveyors_times = None
for x in range(1, 11):
    n = (x**2 - 2 * x + 2) * (2**((x - 1) // 10))
    if surveyors_cost == n:
        surveyors_times = x
        break

    if surveyors_cost < n:
        print(f'Maybe Not Right Surveyors Cost Value ({surveyors_cost})')
        exit()

