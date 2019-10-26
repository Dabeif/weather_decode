import os
import traceback
import data
import re
import pandas as pd

# 判断是否以“=”结尾
pattern = re.compile('^(.*)=\n?$')


# 有效能见度
def effective_visibility(x: int):
    tmp = ['>70', '<0.05', '0.05', '0.2', '0.5', '1', '2', '4', '10', '20', '>=50']
    ans = f"能见度为"
    if x == 0:
        ans += "<0.1"
    elif 1 <= x <= 50:
        ans += f'{x/10}'
    elif 56 <= x <= 79:
        ans += f'{x - 50}'
    elif x == 80:
        ans += f'≥30'
    elif 81 <= x <= 88:
        ans += f'{(x-80)*5+30}'
    elif x >= 89:
        ans += tmp[x-89]
    return ans + '千米'


def IIiii(item: str):
    df = pd.read_excel("station_number.xlsx", header=None)
    ans = df[df[0] == int(item)]
    if ans.empty:
        ans = "未知"
    else:
        ans = ans.iloc[0][1] + ans.iloc[0][2]
    return ans


def ir_ix_h_vv(item: str):
    ans = ""
    if int(item[1]) <= 3:
        ans += '人工站：'
    else:
        ans += '自动站'
    # ir:是否编报降水组
    if item[0] != '/':
        ans += ('不' if item[0] != '1' else '') + '编报降水组, '
    # 是否编报天气现象组
    if item[1] != '/':
        ans += ('不' if item[1] != '1' else '') + '编报天气现象组, '
    # h: 云底高度
    if item[2] != '/':
        ans += f'云底高度为{data.cloud_bottom_height[item[2]]}, '
    else:
        ans += '云底高度缺测'
    # vv: 有效能见度
    if item[3:] != '//':
        ans += effective_visibility(int(item[3:]))
    else:
        ans += '有效能见度缺测'
    return ans


def N_dd_ff(item: str):
    ans = ''
    # N: 总云量
    if item[0] != '/':
        ans += f'总云量为{data.cloud_amount[item[0]]}, '
    else:
        ans += '总云量缺测'
    # dd: 风向
    if item[1:3] != '//':
        ans += f'{data.wind_direction[item[1:3]]}风, '
    else:
        ans += '风向缺测，'
    # ff: 风速
    if item[3:] != '//':
        ans += f'风速{int(item[3:])}米/秒'
    else:
        ans += '风速缺测'
    return ans


def _1Sn_TTT(item: str):
    ans = '温度：'
    if item[1] == '1':
        ans += '零下'
    if item[2:] != '///':
        ans += f'{int(item[2:]) / 10}摄氏度'
    else:
        ans += '缺测'
    return ans


def _2Sn_TdTdTd(item: str):
    return f'露点：' + ('零下' if item[1] == '1' else '') + f'{int(item[2:]) / 10}摄氏度'


def _3PoPoPoPo(item: str):
    ans = '气压：'
    if item[1:] != '////':
        ans += f'{int(item[1:]) / 10}hPa'
    else:
        ans += '缺测'
    return ans


def _4PPPP(item: str):
    ans = '海平面气压：'
    if item[1:] != '////':
        ans += f'{1000 + int(item[1:]) / 10}hPa'
    else:
        ans += '缺测'
    return ans


def _5aPPP(item: str):
    ans = f'过去三小时内气压{data.pressure_change[item[1]]}'
    if item[1] == '2':
        ans += f', 气压变量为+{int(item[2:]) / 10}hPa'
    elif item[1] == '7':
        ans += f', 气压变量为-{int(item[2:]) / 10}hPa'
    return ans


def _6RRR1(item: str):
    ans = ''
    t = int(item[1:-1])
    if 1 <= t <= 988:
        ans += f'过去六小时内本站降水量为{t}mm'
    elif t == 990:
        ans += f'过去六小时内本站降水微量'
    elif 991 <= t <= 999:
        ans += f'过去六小时内本站降水量为{(t - 990) / 10}mm'
    return ans


def _7wwW1W2(item: str):
    return f'现在天气现象是{data.weather_phenomenon[item[1:3]]}, ' \
        f'过去六小时出现的天气现象是{data.past_weather_phenomenon[item[3]]}和{data.past_weather_phenomenon[item[4]]}'


def _8Nh_CCC(item: str):
    ans = ''
    if item[1] != '/':
        if item[2] != '0':
            ans += f'低云量为{data.cloud_amount[item[1]]}, '
        else:
            ans += f'中云量为{data.cloud_amount[item[1]]}, '
    if item[2] != '/':
        ans += f'低云状：{data.low_cloud[item[2]]}, '
    else:
        ans += f'低云状：缺测，'
    if item[3] != '/':
        ans += f'中云状：{data.middle_cloud[item[3]]}, '
    else:
        ans += f'中云状：缺测，'
    if item[4] != '/':
        ans += f'高云状：{data.high_cloud[item[4]]}'
    else:
        ans += f'高云状：缺测'
    return ans


def translate(msg: list):
    ans = {msg[0]: IIiii(msg[0]), msg[1]: ir_ix_h_vv(msg[1]), msg[2]: N_dd_ff(msg[2])}
    func_list = [_1Sn_TTT, _2Sn_TdTdTd, _3PoPoPoPo, _4PPPP, _5aPPP, _6RRR1, _7wwW1W2, _8Nh_CCC]
    for item in msg[3:]:
        # 第3段不编报
        if item.startswith('333'):
            break
        # 编报第2段
        if item[0].isdigit():
            n = int(item[0])
            ans[item] = func_list[n-1](item)
    return ans


def get_path(month: int, day: int, hour: int):
    return data.BASE_DIR + f'AAXX{month:02}{day:02}.T{hour:02}'


def search(filepath: str, station: str):
    if not os.path.exists(filepath):
        return data.FILE_NOT_FOUND
    with open(filepath, 'r') as f:
        next(f)
        next(f)
        line = next(f)
        if not line.startswith('AAXX'):
            return data.NOT_GROUND_MSG
        for line in f:
            if line.startswith(station):
                # 获取目标报文
                ans = pattern.match(line)
                if ans:
                    msg = ans.group(1).split()
                else:
                    msg = line.split()
                    line = next(f)
                    ans = pattern.match(line)
                    while not ans:
                        msg.extend(line.split())
                        line = next(f)
                        ans = pattern.match(line)
                    msg.extend(ans.group(1).split())
                # 翻译目标报文
                try:
                    print(msg)
                    result = translate(msg)
                    return '\n'.join(list(result.values()))
                except Exception:
                    traceback.print_exc()
                    return data.TRANSLATE_ERROR
                break
            else:
                while not pattern.match(line):
                    line = next(f)
        return data.STATION_NOT_FOUND
