
def battery_is_ok(temperature, soc, charge_rate, language):     
  status_list = [temperature_in_range(temperature, language), soc_in_range(soc, language), charge_rate_in_range(charge_rate, language)]
  for statuses in status_list:
    if statuses == False:
      return False
  return True


def temperature_in_range(temperature, language):
  check_warning(0, 45, temperature, language)
  if temperature < 0 or temperature > 45:
    if language == "EN":
      EN_print_statements('Temperature is out of range!')
    elif language == "DE":
      DE_print_statements('Temperature is out of range!')
    return False
  return True


def soc_in_range(soc, language):
  check_warning(20, 80, soc, language)
  if soc < 20 or soc > 80:
    if language == "EN":
      EN_print_statements('State of Charge is out of range!')
    elif language == "DE":
      DE_print_statements('State of Charge is out of range!')
    return False
  return True


def charge_rate_in_range(charge_rate, language):
  check_warning(0, 0.8, charge_rate, language)
  if charge_rate > 0.8:
    if language == "EN":
      EN_print_statements('Charge rate is out of range!')
    elif language == "DE":
      DE_print_statements('Charge rate is out of range!')
    return False
  return True


def check_warning(min_value, max_value, value, language):
  threshold = 0.5 * max_value
  if value >= min_value + threshold:
    if language == "EN":
      EN_print_statements('Warning: Approaching discharge')
  elif value <= max_value - threshold:
    if language == "EN":
      EN_print_statements('Warning: Approaching charge-peak')


def EN_print_statements(sentence):
  if sentence == "Temperature is out of range!":
    print("Temperature is out of range!")
  elif sentence == "State of Charge is out of range!":
    print("State of Charge is out of range!")
  elif sentence == "Charge rate is out of range!":
    print("Charge rate is out of range!")
  elif sentence == "Warning: Approaching discharge":
    print("Warning: Approaching discharge")
  elif sentence == "Warning: Approaching charge-peak":
    print("Warning: Approaching charge-peak")

def DE_print_statements(sentence):
  if sentence == "Temperature is out of range!":
    print("Die Temperatur liegt außerhalb des zulässigen Bereichs!")
  elif sentence == "State of Charge is out of range!":
    print("Ladezustand außerhalb des Bereichs!")
  elif sentence == "Charge rate is out of range!":
    print("Der Ladestrom liegt außerhalb des zulässigen Bereichs!")
  elif sentence == "Warning: Approaching discharge":
    print("Warnung: Naht Entladung")
  elif sentence == "Warning: Approaching charge-peak":
    print("Warnung: Ladespitze nähert sich")

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
  assert(battery_is_ok(30, 50, 0.8, "EN") is True)
  assert(battery_is_ok(30, 50, 0.9, "EN") is False)
