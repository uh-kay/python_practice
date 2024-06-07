from employee import Employee


def test_give_default_raise():
    jonah = Employee('Jonah', 'Sylvian', 60000)
    jonah.give_raise()
    assert jonah.annual_salary == 65000


def test_give_custom_raise():
    jonah = Employee('Jonah', 'Sylvian', 60000)
    jonah.give_raise(10000)
    assert jonah.annual_salary == 70000
