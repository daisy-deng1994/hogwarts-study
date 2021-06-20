# editor:Daisy
# date:2021/6/19 4:28 下午
import logging
import allure
import pytest
import yaml
from homework.code.calculator import Calculator


# 获取测试数据
def get_calc_data(n : str):
    with open('../data/calc_data.yml', 'r', encoding='utf-8') as c:
        total = yaml.safe_load(c)
    return total.get(n).get('datas'),total.get(n).get('ids')


@allure.feature("计算器功能测试")
class TestCalculator:
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("结束计算")

    def setup(self):
        logging.info("开始计算啦！")

    def teardown(self):
        logging.info("结束计算啦！")

    @allure.story("加法功能")
    @allure.step("加法正向用例")
    @pytest.mark.parametrize('a,b,expect', get_calc_data("add_success")[0], ids=get_calc_data("add_success")[1])
    def test_add_success(self, a, b, expect):
        if type(self.calc.add(a,b))==float:
            aa=float(format(self.calc.add(a,b),'.2f'))
            assert expect == aa
        else:
            assert expect == self.calc.add(a, b)

    @allure.step("加法反向用例")
    @pytest.mark.parametrize('a,b,expect', get_calc_data("add_fail")[0], ids=get_calc_data("add_fail")[1])
    def test_add_fail(self, a, b, expect):
        with pytest.raises(TypeError) as s:
            self.calc.add(a, b)
            assert expect == str(s.value)

    @allure.story("除法功能")
    @allure.step("除法正向用例")
    @pytest.mark.parametrize('a,b,expect', get_calc_data("div_success")[0], ids=get_calc_data("div_success")[1])
    def test_div_success(self, a, b, expect):
        if type(self.calc.div(a,b))==float:
            aa=float(format(self.calc.div(a,b),'.3f'))
            assert expect == aa
        else:
            assert expect == self.calc.div(a, b)

    @allure.step("除法反向用例")
    @pytest.mark.parametrize('a,b,expect', get_calc_data("div_fail")[0], ids=get_calc_data("div_fail")[1])
    def test_div_fail(self,a,b,expect):
        with pytest.raises(ZeroDivisionError or TypeError) as s:
            self.calc.add(a, b)
            assert expect == str(s.value)


