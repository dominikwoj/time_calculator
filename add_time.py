def add_time(start, duration, day = None):
    # "3:30 PM", "2:12", "Monday" -> 5:42 PM, Monday
    _days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    _start = [None] * 3
    _start[0], _start[1] = start.split(':')
    _start[1], _start[2] = _start[1].split(' ')
    _start[0:2] = list(map(int, _start[0:2]))

    _duration = duration.split(':')
    _duration = list(map(int, _duration))
    print(_start, _duration)
    h = _start[0] + _duration[0]
    m = _start[1] + _duration[1]
    print(h, m)

    day_out = ''
    #if day is None:
    #_min_total = _duration[0] * 60 + _duration[1] - (12 if _start[2] == 'AM' else 0)
    _min_total = _duration[0] * 60 + _duration[1]
    _day = _min_total // (24 * 60)
    _h = (_min_total - _day * (24 * 60)) // 60
    _min = _min_total - _day * (24 * 60) - _h * 60
    # _h = _min
    if start[2] == 'PM':
        if _h + _start[0] > 12:
            _day += 1
            _h += _start[0] - 12
            _part_of_day = 'AM'
        if _h + _start[0] > 12:
            _h -= 12
            _part_of_day = 'PM'


    print(f'{_min_total}|{_day}|{_h}|{_min}')
    day_out = f'{_day} days later'

    _part_of_day = _start[2]
    out = f'{h}:{m} {_part_of_day}'
    print(out)
    return out

if __name__ == '__main__':
    #import doctest
    #doctest.testfile('test.txt')
    #add_time("3:30 PM", "2:12", "Monday")
    add_time("8:16 PM", "466:02") # -> 6:18 AM (20 days later).