def battery_is_ok(temperature, soc, charge_rate, language): 
  if language == "EN":    
    status_list = [temperature_in_range_EN(temperature), soc_in_range_EN(soc), charge_rate_in_range_EN(charge_rate)]
  if language == "DE":    
    status_list = [temperature_in_range_DE(temperature), soc_in_range_DE(soc), charge_rate_in_range_DE(charge_rate)]
  for statuses in status_list:
    if statuses == False:
      return False
  return True


def temperature_in_range_EN(temperature):
  check_warning_EN(0, 45, temperature)
  if temperature < 0 or temperature > 45:
    print_statements('Temperature is out of range!')
    return False
  return True


def temperature_in_range_DE(temperature):
  check_warning_DE(0, 45, temperature)
  if temperature < 0 or temperature > 45:
    print_statements('Die Temperatur liegt außerhalb des zulässigen Bereichs!')
    return False
  return True

def soc_in_range_EN(soc):
  check_warning_EN(20, 80, soc)
  if soc < 20 or soc > 80:
    print_statements('State of Charge is out of range!')
    return False
  return True


def soc_in_range_DE(soc):
  check_warning_DE(20, 80, soc)
  if soc < 20 or soc > 80:
    print_statements('Ladezustand außerhalb des Bereichs!')
    return False
  return True


def charge_rate_in_range_EN(charge_rate):
  check_warning_EN(0, 0.8, charge_rate)
  if charge_rate > 0.8:
    print_statements('Charge rate is out of range!')
    return False
  return True


def charge_rate_in_range_DE(charge_rate):
  check_warning_DE(0, 0.8, charge_rate)
  if charge_rate > 0.8:
    print_statements('Der Ladestrom liegt außerhalb des zulässigen Bereichs!')
    return False
  return True


def check_warning_EN(min_value, max_value, value):
  threshold = 0.5 * max_value
  if value >= min_value + threshold:
    print_statements('Warning: Approaching discharge')
  if value <= max_value - threshold:
    print_statements('Warning: Approaching charge-peak')


def check_warning_DE(min_value, max_value, value):
  threshold = 0.5 * max_value
  if value >= min_value + threshold:
    print_statements('Warnung: Naht Entladung')
  if value <= max_value - threshold:
    print_statements('Warnung: Ladespitze nähert sich')


def print_statements(message):
  print(message)


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7, "EN") is True)
  assert(battery_is_ok(50, 85, 0, "EN") is False)
  assert(battery_is_ok(-1, 79, 0, "EN") is False)
  assert(battery_is_ok(0, 75, 0, "EN") is True)
  assert(battery_is_ok(45, 75, 0, "EN") is True)
  assert(battery_is_ok(46, 75, 0, "EN") is False)
  assert(battery_is_ok(30, 20, 0, "EN") is True)
  assert(battery_is_ok(30, 80, 0, "EN") is True)
  assert(battery_is_ok(30, 10, 0, "EN") is False)
  assert(battery_is_ok(30, 90, 0, "EN") is False)
  assert(battery_is_ok(30, 50, 0.8, "DE") is True)
  assert(battery_is_ok(30, 50, 0.9, "DE") is False)
