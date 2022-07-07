
def battery_is_ok(temperature, soc, charge_rate):     
  status_list = [temperature_in_range(temperature), soc_in_range(soc), charge_rate_in_range(charge_rate)]
  for statuses in status_list:
    if statuses == False:
      return False
  return True


def temperature_in_range(temperature):
  if temperature < 0 or temperature > 45:
    print('Temperature is out of range!')
    return False
  return True


def soc_in_range(soc):
  if soc < 20 or soc > 80:
    print('State of Charge is out of range!')
    return False
  return True


def charge_rate_in_range(charge_rate):
  if charge_rate > 0.8:
    print('Charge rate is out of range!')
    return False
  return True


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
  assert(battery_is_ok(-1, 79, 0) is False)
  assert(battery_is_ok(0, 75, 0) is True)
  assert(battery_is_ok(45, 75, 0) is True)
  assert(battery_is_ok(46, 75, 0) is False)
  assert(battery_is_ok(30, 20, 0) is True)
  assert(battery_is_ok(30, 80, 0) is True)
  assert(battery_is_ok(30, 10, 0) is False)
  assert(battery_is_ok(30, 90, 0) is False)
  assert(battery_is_ok(30, 50, 0.8) is True)
  assert(battery_is_ok(30, 50, 0.9) is False)
