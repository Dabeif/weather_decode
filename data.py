# 资料路径
BASE_DIR = '地面资料/'

# 错误码
FILE_NOT_FOUND = -1
STATION_NOT_FOUND = -2
NOT_GROUND_MSG = -3
TRANSLATE_ERROR = -4

# 云底高度
cloud_bottom_height = {
    '0': '<50m',
    '1': '50～100m',
    '2': '100～200m',
    '3': '200～300m',
    '4': '300～600m',
    '5': '600～1000m',
    '6': '1000～1500m',
    '7': '1500～2000m',
    '8': '2000～2500m',
    '9': '≥2500米或无云',
    'x': '云底高度不明，或者云底低于测站而云顶高于测站',
}

# 云量
cloud_amount = {
    '0': '无云',
    '1': '1或微量(可以判定为云状的微量云)',
    '2': '2-3',
    '3': '4',
    '4': '5',
    '5': '6',
    '6': '7-8',
    '7': '9或10',
    '8': '10',
    '9': '因有雾或其他视程障碍现象而使总云量无法估计',
    'x': '未观测(自动站未配有测云设备)',
}

# 风向
wind_direction = {
    '00': '静',
    '02': '北东北',
    '04': '东北',
    '07': '东东北',
    '09': '东',
    '11': '东东南',
    '14': '东南',
    '16': '南东南',
    '18': '南',
    '20': '南西南',
    '22': '西南',
    '25': '西西南',
    '27': '西',
    '29': '西西北',
    '32': '西北',
    '34': '北西北',
    '36': '北',
}

# 气压变化
pressure_change = {
    '2': '上升',
    '4': '无变化',
    '7': '下降',

    '0': '升后微降',
    '1': '升后平',
    '3': '微降后升',
    '5': '降后微升',
    '6': '降后平',
    '8': '微升后降'
}

# 天气现象
weather_phenomenon = {
    '00': '没有出现规定编报的天气现象',
    '04': '观测时水平能见度因烟（草原或森林着火而引起的烟，工厂排出的烟）或火山爆发的灰尘障碍而降低',
    '05': '观测时有霾',
    '06': '观测时有浮尘，广泛散布的浮在空中的尘土，不是在观测时由测站或测站附近的风所吹起来的。',
    '07': '观测时由测站或测站附近的风吹起来的扬沙或尘土，但还没有发展成完好的尘卷风或沙尘暴；或飞沫吹到观测船上',
    '08': '观测时或观测前一小时内在测站或测站附近看到发展完好的尘卷风，但没有沙尘暴',
    '09': '观测时视区内有沙尘暴，或者观测前一小时内测站有沙尘暴',
    "10": "轻雾",
    "11": "测站有浅雾，呈片状，在陆地上厚度不超过2米，在海上不超过10米",
    "12": "测站有浅雾，基本连续，在陆地上厚度不超过2米，在海上不超过10米",
    "13": "闪电",
    "14": "视区内有降水，没有到达地面或海面",
    "15": "视区内有降水，已经到达地面或海面，但估计距测站5千米以外",
    "16": "视区内有降水，已经到达地面或海面，在测站附近，但本站无降水",
    "17": "雷暴，但观测时测站没有降水",
    "18": "飑，观测时或观测前一小时内在测站或视区内出现",
    "19": "龙卷，观测时或观测前一小时内在测站或视区内出现",
    "20": "毛毛雨	非阵性的",
    "21": "雨",
    "22": "雪、米雪或冰粒",
    "23": "雨夹雪，或雨夹冰粒",
    "24": "毛毛雨或雨，并有雨凇结成",
    "25": "阵雨",
    "26": "阵雪，或阵性雨夹雪",
    "27": "冰雹或霰（伴有或不伴有雨）",
    "28": "雾",
    "29": "雷暴（伴有或不伴有降水）",
    "30": "轻的或中度的沙尘暴，过去一小时内减弱",
    "31": "轻的或中度的沙尘暴，过去一小时内没有显著的变化",
    "32": "轻的或中度的沙尘暴，过去一小时内开始或增强",
    "33": "强的沙尘暴，过去一小时内减弱",
    "34": "强的沙尘暴，过去一小时内没有显著的变化",
    "35": "强的沙尘暴，过去一小时内开始或增强",
    "36": "轻的或中度的低吹雪，吹雪所达高度一般低于观测员的眼睛（水平视线）",
    "37": "强的低吹雪，吹雪所达高度一般低于观测员的眼睛（水平视线）",
    "38": "轻的或中度的高吹雪，吹雪所达高度一般高于观测员的眼睛（水平视线）",
    "39": "强的高吹雪，吹雪所达高度一般高于观测员的眼睛（水平视线），或雪暴",
    "40": "观测时近处有雾，其高度高于观测员的眼睛（水平视线），但观测前一小时内测站没有雾",
    "41": "散片的雾",
    "42": "雾，过去一小时内已变薄，天空可辨明",
    "43": "雾，过去一小时内已变薄，天空不可辨",
    "44": "雾，过去一小时内强度没有显著的变化，天空可辨明",
    "45": "雾，过去一小时内强度没有显著的变化，天空不可辨",
    "46": "雾，过去一小时内开始出现或已变浓，天空可辨明",
    "47": "雾，过去一小时内开始出现或已变浓，天空不可辨",
    "48": "雾，有雾凇结成，天空可辨明",
    "49": "雾，有雾凇结成，天空不可辨",
    "50": "间歇性轻毛毛雨",
    "51": "连续性轻毛毛雨",
    "52": "间歇性中常毛毛雨",
    "53": "连续性中常毛毛雨",
    "54": "间歇性浓毛毛雨",
    "55": "连续性浓毛毛雨",
    "56": "轻的毛毛雨，并有雨凇结成",
    "57": "中常的或浓的毛毛雨，并有雨凇结成",
    "58": "轻的毛毛雨夹雨",
    "59": "中常的或浓的毛毛雨夹雨",
    "60": "间歇性小雨",
    "61": "连续性小雨",
    "62": "间歇性中雨",
    "63": "连续性中雨",
    "64": "间歇性大雨",
    "65": "连续性大雨",
    "66": "小雨，并有雨凇结成",
    "67": "中雨或大雨，并有雨凇结成",
    "68": "小的雨夹雪，或轻毛毛雨夹雪",
    "69": "中常的或大的雨夹雪，或中常的或浓的毛毛雨夹雪",
    "70": "间歇性小雪",
    "71": "连续性小雪",
    "72": "间歇性中雪",
    "73": "连续性中雪",
    "74": "间歇性大雪",
    "75": "连续性大雪",
    "76": "冰针（伴有或不伴有雾）",
    "77": "米雪（伴有或不伴有雾）",
    "78": "孤立的星状雪晶（伴有或不伴有雾）",
    "79": "冰粒",
    "80": "小的阵雨",
    "81": "中常的阵雨",
    "82": "大的阵雨",
    "83": "小的阵性雨夹雪",
    "84": "中常或大的阵性雨夹雪",
    "85": "小的阵雪",
    "86": "中常或大的阵雪",
    "87": "小的阵性霰，伴有或不伴有雨或雨夹雪",
    "88": "中常或大的阵性霰，伴有或不伴有雨或雨夹雪",
    "89": "轻的冰雹，伴有或不伴有雨或雨夹雪",
    "90": "中常或强的冰雹，伴有或不伴有雨或雨夹雪",
    "91": "观测前一小时内有雷暴，观测时有小雨",
    "92": "观测前一小时内有雷暴，观测时有中雨或大雨",
    "93": "观测前一小时内有雷暴，观测时有小（轻）的雪、或雨夹雪、或霰、或冰雹",
    "94": "观测前一小时内有雷暴，观测时有中常或大（强）的雪、或雨夹雪、或霰、或冰雹",
    "95": "小或中常的雷暴，观测时没有冰雹、或霰，但有雨、或雪、或雨夹雪",
    "96": "小或中常的雷暴，观测时伴有冰雹、或霰",
    "97": "大雷暴，观测时没有冰雹、或霰，但有雨、或雪、或雨夹雪",
    "98": "雷暴，观测时伴有沙尘暴和降水",
    "99": "大雷暴，观测时伴有冰雹、或霰",
}

# 过去天气现象
past_weather_phenomenon = {
    '0': '无',
    '3': '沙尘暴、吹雪或雪暴',
    '4': '雾',
    '5': '毛毛雨',
    '6': '非阵性的雨',
    '7': '非阵性的固体降水或混合降水',
    '8': '阵性降水',
    '9': '雷暴（伴有或不伴有降水'
}

# 低云
low_cloud = {
    '0': '没有低云',
    '1': '淡积云或碎积云',
    '2': '浓积云',
    '3': '秃积雨云',
    '4': '积云性层积云',
    '5': '层积云',
    '6': '层云和（或）碎层云',
    '7': '碎雨云',
    '8': '积云和不是积云性的层积云',
    '9': '鬃积雨云',
    'x': '由于黑暗、或雾、或沙尘暴、或其他类似现象以致看不到属于CL的各属云',
}

# 中云
middle_cloud = {
    '0': '没有中云',
    '1': '透光高层云',
    '2': '蔽光高层云或雨层云',
    '3': '透光高积云',
    '4': '荚状层积云',
    '5': '成带的或成层的透光高积云',
    '6': '积云性高积云',
    '7': '复高积云或蔽光高积云',
    '8': '积云状高积云',
    '9': '混乱天空的高积云',
    'x': '由于黑暗、或雾、或沙尘暴、或其他类似现象，或者完整的较低云层存在，以致看不到属于CM的各属云',
}

# 高云
high_cloud = {
    '0': '没有高云',
    '1': '毛卷云',
    '2': '密卷云',
    '3': '伪卷云',
    '4': '卷云',
    '5': '辐辏状卷云和卷层云',
    '6': '辐辏状卷云和卷层云',
    '7': '卷层云布满全天',
    '8': '卷层云',
    '9': '卷积云',
    'x': '由于黑暗、或雾、或沙尘暴、或其他类似现象，或者完整的较低云层存在，以致看不到属于CH的各属云',
}

# 缺测
not_recorded = {
    '1': '温度组',
    '2': '露点组',
    '3': '气压组',
    '4': '海平面气压组',
    '5': '气压变化量组',
    '6': '降水组',
    '7': '天气现象组',
    '8': '云量组'
}