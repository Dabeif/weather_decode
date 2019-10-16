import sys
import data
import utils

if __name__ == '__main__':
    while True:
        print('-'*20 + '欢迎来到地面报文译码系统' + '-'*20)
        print('1. 译码')
        print('2. 退出')
        res = input('请选择：')
        if res == '2':
            sys.exit(0)
        while True:
            if res == '1':
                try:
                    year, month, day, hour, station = map(int, input("请输入年、月、日、时次、台站号(以空格隔开)：").split())
                    filepath = utils.get_path(month, day, hour)
                    ans = utils.search(filepath, str(station))
                    if ans == data.FILE_NOT_FOUND:
                        print('文件未找到!')
                    elif ans == data.STATION_NOT_FOUND:
                        print('无此台站号!')
                    elif ans == data.NOT_GROUND_MSG:
                        print('不是地面报文资料!')
                    elif ans == data.TRANSLATE_ERROR:
                        print('译码出错！')
                    else:
                        print(ans)
                    break
                except Exception:
                    print('请按指定格式输入！')
            elif res == '2':
                sys.exit(0)
            else:
                print('输入有误，请重新输入！')
                res = input('请选择：')
