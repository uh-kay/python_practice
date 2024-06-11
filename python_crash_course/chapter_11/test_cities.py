from city_functions import city_country


def test_city_country():
    output = city_country('Santiago', 'Chile')
    assert output == 'Santiago, Chile'


def test_city_country_population():
    output = city_country('santiago', 'chile', population=5000000)
