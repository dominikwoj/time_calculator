def add_time(start, duration, day=None):
    _days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    _start = [None] * 3
    _start[0], _start[1] = start.split(':')
    _start[1], _start[2] = _start[1].split(' ')
    _start[0:2] = list(map(int, _start[0:2]))

    _duration = duration.split(':')
    _duration = list(map(int, _duration))

    _part_of_day = _start[2]
    _init = 0

    if _start[2] == 'AM':
        _init = -12 if _start[0] == 12 else 0
    else:
        _init = 0 if _start[0] == 12 else 12

    _min_total = (_init + _start[0] + _duration[0]) * 60 + _start[1] + _duration[1]
    _day = _min_total // (24 * 60)
    _h = (_min_total - _day * (24 * 60)) // 60
    _min = _min_total - _day * (24 * 60) - _h * 60

    # print(f'_d={_day}|_h={_h}|_min={_min}|_init={_init}|_min_total={_min_total}')
    if _h >= 12:
        _part_of_day = 'PM'
        if _h != 12:
            _h -= 12
    else:
        _part_of_day = 'AM'

    if _h == 0:
        _h = 12  # 0:00 AM not exists -> 12:00 AM
        _part_of_day = 'AM'

    _day_later = ''
    match _day:
        case 1:
            _day_later = f' (next day)'
        case _day if _day > 1:
            _day_later = f' ({_day} days later)'

    _day_name = ''
    if day is not None:
        _i = _days.index(day.upper())
        _name = _days[(_i + _day) % 7]
        _day_name = f', {_name[0]}{_name[1:].lower()}'

    return f'{_h}:{_min:02d} {_part_of_day}{_day_name}{_day_later}'


if __name__ == '__main__':
    import doctest

    doctest.testfile('test.txt')
