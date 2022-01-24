def bytes_to(bytes_value, to_unit, bytes_size=1024):
    units = {'k': 1, 'm': 2, 'g': 3, 't': 4, 'p': 5, 'e': 6}
    return round(float(bytes_value) / (bytes_size ** units[to_unit]), 2)


def convert_to_human(value):
    if value < 1024:
        return str(value) + 'b'
    if value < 1048576:
        return str(bytes_to(value, 'k')) + 'k'
    if value < 1073741824:
        return str(bytes_to(value, 'm')) + 'm'

    return str(bytes_to(value, 'g')) + 'g'


def convert_to_human_with_limits(value, limit):
    if value < limit:
        return convert_to_human(value)

    return "[bold magenta]" + convert_to_human(value) + "[/]"
