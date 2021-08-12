class Fraction:
    '''
    이 class는 분자(numerator)와 분모(denominator)로 구성된 분수를 표현합니다.
    항상 기약분수 상태로 존재합니다.

    멤버 변수: num, denom
    메소드: reduce(), is_zero(), to_string(), to_decimals(), get_gcd()
    '''

    num, denom = 0, 0

    def __init__(self, num, denom):
        # input: 정수 타입의 num, denom
        # return: x (void 함수)

        # 생성자
        # TODO 분자, 분모를 받아서 멤버 변수에 저장. 기약분수로도 만들어 줘야겠지??
        pass

    def reduce(self):
        # input: x
        # return: x (void 함수) -> but, 굳이 바꾸겠다면 return 값 수정 가능

        # 분수를 기약분수로 만들어주는 함수
        # TODO 기약분수를 어떻게 만들까요? Hint: 기약분수 = 분자 분모가 서로소인 분수
        pass

    def is_zero(self):
        # input: x
        # return: True or False

        # 분수의 값이 0인지 return (boolean type)
        # TODO 적절히 바꿔서 True or False를 return 하도록
        return False

    def to_string(self):
        # input: x
        # return: str

        # 분수의 값을 분수 형태의 문자열로 표현
        return f"{self.num} / {self.denom}"

    def to_decimals(self):
        # input: x
        # return: float

        # 분수의 값을 소수로 표현
        return self.num / self.denom

    def get_gcd(self, a, b):
        # input: 정수 타입의 a, b
        # return: 정수 타입의 최대공약수

        # 최대 공약수를 구하는 함수. (왜 이 함수가 최대 공약수를 리턴하는지 궁금하다면, 유클리드 호제법 검색)
        # TODO (함수 바꿀 필요는 x) Hint: 이건 왜 필요할까?
        while b != 0:
            tmp = a % b
            a = b
            b = tmp
        return a
