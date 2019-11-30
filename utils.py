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
    ans = ''
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
    return ans


def IIiii(item: str):
    df = pd.read_excel("地面资料/station_number.xlsx", header=None)
    ans = df[df[0] == int(item)]
    if ans.empty:
        ans = "未知"
    else:
        ans = f"{'城市':　<6}: " + ans.iloc[0][1] + ans.iloc[0][2]
    return ans


def ir_ix_h_vv(item: str):
    ans = ""
    if int(item[1]) <= 3:
        ans += f"{'人工站':　<6}: "
    else:
        ans += f"{'自动站':　<6}: "
    # ir:是否编报降水组
    if item[0] != '/':
        ans += ('不' if item[0] != '1' else '') + '编报降水组, '
    # 是否编报天气现象组
    if item[1] != '/':
        ans += ('不' if item[1] != '1' else '') + '编报天气现象组\n'
    # h: 云底高度
    ans += f"{'云底高度':　<6}: "
    if item[2] != '/':
        ans += f'{data.cloud_bottom_height[item[2]]}\n'
    else:
        ans += '缺测'
    # vv: 有效能见度
    ans += f"{'有效能见度':　<6}: "
    if item[3:] != '//':
        ans += f'{effective_visibility(int(item[3:]))}千米'
    else:
        ans += '缺测'
    return ans


def N_dd_ff(item: str):
    ans = ''
    # N: 总云量
    ans += f"{'总云量':　<6}: "
    if item[0] != '/':
        ans += f'{data.cloud_amount[item[0]]}\n'
    else:
        ans += '缺测\n'
    # dd: 风向
    ans += f"{'风向':　<6}: "
    if item[1:3] != '//':
        ans += f'{data.wind_direction[item[1:3]]}风\n'
    else:
        ans += '缺测\n'
    # ff: 风速
    ans += f"{'风速':　<6}: "
    if item[3:] != '//':
        ans += f'{int(item[3:])}米/秒'
    else:
        ans += '缺测'
    return ans


def _1Sn_TTT(item: str):
    ans = f"{'温度':　<6}: "
    if item[1] == '1':
        ans += '-'
    else:
        ans += '+'
    if item[2:] != '///':
        ans += f'{int(item[2:]) / 10}摄氏度'
    else:
        ans += '缺测'
    return ans


def _2Sn_TdTdTd(item: str):
    ans = f"{'露点':　<6}: "
    if item[1] == '1':
        ans += '-'
    else:
        ans += '+'
    if item[2:] != '///':
        ans += f'{int(item[2:]) / 10}摄氏度'
    else:
        ans += '缺测'
    return ans


def _3PoPoPoPo(item: str):
    ans = f"{'气压':　<6}: "
    if item[1:] != '////':
        ans += f'{int(item[1:]) / 10}hPa'
    else:
        ans += '缺测'
    return ans


def _4PPPP(item: str):
    ans = f"{'海平面气压':　<6}: "
    if item[1:] != '////':
        ans += f'{1000 + int(item[1:]) / 10}hPa'
    else:
        ans += '缺测'
    return ans


def _5aPPP(item: str):
    ans = f"{'过去三小时内':　<6}: " + f'气压{data.pressure_change[item[1]]}'
    if item[1] == '2':
        ans += f', 气压变量为+{int(item[2:]) / 10}hPa'
    elif item[1] == '7':
        ans += f', 气压变量为-{int(item[2:]) / 10}hPa'
    return ans


def _6RRR1(item: str):
    ans = f"{'过去六小时内':　<6}: " + '本站降水量'
    t = int(item[1:-1])
    if t != '///':
        if 1 <= t <= 988:
            ans += f'{t}mm'
        elif t == 990:
            ans += f'微量'
        elif 991 <= t <= 999:
            ans += f'{(t - 990) / 10}mm'
    else:
        ans += '缺测'
    return ans


def _7wwW1W2(item: str):
    ww = item[1:3]
    W1 = item[3]
    W2 = item[4]
    ans = f"{'现在天气现象':　<6}: "
    if ww != "//":
        ans += f'{data.weather_phenomenon[ww]}\n'
    else:
        ans += '缺测\n'
    ans += f"{'过去天气现象':　<6}: "
    if W1 != '/':
        ans += f'{data.past_weather_phenomenon[W1]}'
    if W2 != '/':
        ans += f'和{data.past_weather_phenomenon[W2]}'
    return ans


def _8Nh_CCC(item: str):
    ans = ''
    if item[1] != '/':
        if item[2] != '0':
            ans += f"{'低云量':　<6}: " + f'{data.cloud_amount[item[1]]}\n'
        else:
            ans += f"{'中云量':　<6}: " + f'{data.cloud_amount[item[1]]}\n'
    if item[2] != '/':
        ans += f"{'低云状':　<6}: " + f'{data.low_cloud[item[2]]}\n'
    else:
        ans += f"{'低云状':　<6}: 缺测\n"
    if item[3] != '/':
        ans += f"{'中云状':　<6}: " + f'{data.middle_cloud[item[3]]}\n'
    else:
        ans += f"{'中云状':　<6}: 缺测\n"
    if item[4] != '/':
        ans += f"{'高云状':　<6}:" + f'{data.high_cloud[item[4]]}'
    else:
        ans += f"{'高云状':　<6}: 缺测"
    return ans


def translate(msg: list):
    ans = {msg[0]: IIiii(msg[0]), msg[1]: ir_ix_h_vv(msg[1]), msg[2]: N_dd_ff(msg[2])}
    func_list = [_1Sn_TTT, _2Sn_TdTdTd, _3PoPoPoPo, _4PPPP, _5aPPP, _6RRR1, _7wwW1W2, _8Nh_CCC]
    not_recorded = list(range(1, 9))
    for item in msg[3:]:
        # 第3段不编报
        if item.startswith('333'):
            break
        # 编报第2段
        if item[0].isdigit():
            n = int(item[0])
            not_recorded.remove(n)
            ans[item] = func_list[n-1](item)
    if not not_recorded:
        ans['缺测'] = '\n缺测:无\n'
    else:
        ans['缺测'] = '\n缺测:\n'
        for i in not_recorded:
            ans['缺测'] += f'{data.not_recorded[str(i)]}\n'
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
                    print(f"\n报文是: {msg}")
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
