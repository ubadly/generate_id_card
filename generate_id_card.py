import random
from datetime import datetime


def calculate_id_checksum(id17):
    """计算身份证号码最后一位的校验码"""
    id17 = str(id17)
    if len(id17) != 17:
        return None
    factor = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    checksum = sum([int(id17[i]) * factor[i] for i in range(17)])
    remainder = checksum % 11
    return {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}[remainder]


def generate_id_number(year: int, month: int, day: int, gender: int):
    """
    生成随机身份证号码
    :param year: 出生年 1972
    :param month: 出生月 11
    :param day: 出生日 21
    :param gender: 性别 1 男      0 女
    :return: 18位身份证
    """
    # 随机生成一个合法的地区码，即前6位数字
    region_codes = ['410101', '410201', '410301']
    region_code = random.choice(region_codes)

    # 随机生成一个合法的出生日期，即第7到14位数字
    birth_date = datetime(year, month, day)
    birth_date_str = birth_date.strftime('%Y%m%d')

    # 随机生成一个合法的顺序码，即第15到17位数字
    if gender == 1:
        sequence_code = str(random.choice(range(1, 1000, 2))).zfill(3)
    else:
        sequence_code = str(random.choice(range(0, 1000, 2))).zfill(3)
    # 计算最后一位校验码
    id17 = region_code + birth_date_str + sequence_code
    checksum = calculate_id_checksum(id17)
    if checksum is None:
        return None

    # 拼接身份证号码并返回
    return id17 + checksum


if __name__ == '__main__':
    # 测试生成身份证号码
    id_number = generate_id_number(year=1972, month=11, day=21, gender=1)
    print(id_number)
