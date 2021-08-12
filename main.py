from fraction import Fraction
from fraction_handler import FractionCalculator

# main.py는 건드리지 않아도 되지만, 읽어볼만 한 내용

def take_fraction_input(n):
    # 유효한 두 정수를 받는 함수
    while True:
        tmp = input(f'{n}: Enter the numerator and denominator of the fraction(both are integers): ').split()

        if len(tmp) != 2:
            print("[Error] You should enter two numbers")
        else:
            # num(numerator): 분자
            # denom(denominator): 분모
            num, denom = tmp[0], tmp[1]
            if not (num.isdigit() and denom.isdigit()):
                print("[Error] Both should be integers")
            elif int(denom) == 0:
                print('[Error] Denominator cannot be a zero')
            else:
                num, denom = int(num), int(denom)
                print(f'* Input success: {num}, {denom}')
                return num, denom


def take_operator_input():
    # 유효한 연산자를 받는 함수
    while True:
        op = input('Enter the operator[+ - * /]: ')
        if op not in ['+', '-', '*', '/']:
            print("[Error] Operator should be one of (+, -, *, /)")
        else:
            return op


if __name__ == '__main__':
    quit_process = False

    while not quit_process:
        command = input('Enter any key(\'q\' to quit): ')
        if command == 'q':
            quit_process = True
            continue

        tmp_num1, tmp_denom1 = take_fraction_input(1)
        fraction1 = Fraction(tmp_num1, tmp_denom1)

        tmp_num2, tmp_denom2 = take_fraction_input(2)
        fraction2 = Fraction(tmp_num2, tmp_denom2)

        op = take_operator_input()

        fraction_handler = FractionCalculator()
        if op == '+':
            result_fraction = fraction_handler.add_fraction(fraction1, fraction2)
        elif op == '-':
            result_fraction = fraction_handler.sub_fraction(fraction1, fraction2)
        elif op == '*':
            result_fraction = fraction_handler.mul_fraction(fraction1, fraction2)
        else:
            if fraction2.is_zero():
                print("[Error] The divisor cannot be zero\n")
                continue
            else:
                result_fraction = fraction_handler.div_fraction(fraction1, fraction2)

        print("-----Result-----")
        print(f"As fraction: {result_fraction.to_string()}")
        print(f"As decimals: {result_fraction.to_decimals()}")
        print()


