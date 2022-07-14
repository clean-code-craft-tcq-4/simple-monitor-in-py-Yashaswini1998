from check_limits import *

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