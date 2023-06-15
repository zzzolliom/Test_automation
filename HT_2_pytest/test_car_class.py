import pytest
from HT_1_OOP.car_class import Car

class TestCarClass:
    @pytest.fixture
    def car_class_instanse(self):
        yield  Car()

    def test_set_yeahr (self , car_class_instanse):
        car_class_instanse.set_year(2020)
        assert car_class_instanse.year == 2020

    @pytest.mark.skip
    def test_start_car(self, car_class_instanse):
        result = car_class_instanse.start_car()
        assert result == "Автомобиль заведен"

    @pytest.mark.xfail
    def test_stop_car(self, car_class_instanse):
        result = car_class_instanse.stop_car()
        assert result == "Автомобиль заглушен"


    def test_set_type(self, car_class_instanse):
        car_class_instanse.set_type("Автобус")
        assert car_class_instanse.type == "Автобус"


    def test_set_type_error(self, car_class_instanse):
        with pytest.raises(TypeError):
            car_class_instanse.set_type()


    def test_set_color(self, car_class_instanse):
        car_class_instanse.set_color("blue")
        assert car_class_instanse.color == "blue"


    def test_errormessage_set_color(self, car_class_instanse):
        with pytest.raises(TypeError) as exinfo:
            car_class_instanse.set_color()
        assert "missing 1 required positional argument" in str(exinfo.value)

