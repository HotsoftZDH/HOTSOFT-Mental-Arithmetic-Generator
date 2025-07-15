import random
from fractions import Fraction
def question(max_num, min_num, sign, num_type=1):
    """生成数学题目（支持整数、小数、分数）"""
    operators = {1: '+', 2: '-', 3: '×', 4: '÷', 5: '²' if num_type == 3 else '^2'}

    questions = []
    for _ in range(10):
        # 生成数字（根据不同类型）
        if num_type == 1:  # 整数
            num1 = random.randint(int(min_num), int(max_num))
            num2 = random.randint(int(min_num), int(max_num))
        elif num_type == 2:  # 小数
            num1 = round(random.uniform(min_num, max_num), 2)
            num2 = round(random.uniform(min_num, max_num), 2)
        else:  # 分数
            num1 = Fraction(
                random.randint(1, int(max_num)),
                random.randint(1, int(max_num))
            )
            num2 = Fraction(
                random.randint(1, int(max_num)),
                random.randint(1, int(max_num))
            )

        # 构建题目表达式
        if sign == 5:  # 平方
            expr = f"({num1})²" if num_type == 3 else f"{num1}^2"
        elif sign == 4:  # 除法
            if num_type == 3 and num2.numerator == 0:
                num2 = Fraction(1, 1)  # 避免分数除数为0
            elif num_type != 3 and num2 == 0:
                num2 = 1  # 避免整数/小数除数为0
            expr = f"{num1} ÷ {num2}"
        else:  # 加减乘
            if sign == 2 and num1 < num2:  # 减法确保非负
                num1, num2 = num2, num1
            expr = f"{num1} {operators[sign]} {num2}"

        questions.append(expr)

    return questions