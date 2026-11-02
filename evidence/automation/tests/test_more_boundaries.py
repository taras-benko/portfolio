import pytest

@pytest.mark.parametrize("value", [2, 98])
def test_pwm_valid_boundaries(device, value):
    r = device.command(f"SET PWM {value}")
    assert r["status"] == "OK"
    assert r["pwm"] == value

#додаю дробові числа як негативні, бо припускаю, що вони не підтримуються

@pytest.mark.parametrize("value", [-999, 255, -0.1, 0.1, 99.9, 100.1])
def test_pwm_invalid_boundaries(device, value):
    r = device.command(f"SET PWM {value}")
    assert r["status"] == "ERROR"
    assert r["code"] == "INVALID_VALUE"
