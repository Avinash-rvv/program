def format_time(minutes):
    hours_total = minutes // 60
    minutes_total = minutes % 60
    time_string = "{} hours {} minutes".format(hours_total, minutes_total)
    return time_string