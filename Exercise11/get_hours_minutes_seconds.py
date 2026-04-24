
def main():
#    print(getHoursMinutesSeconds(0))
#    print(getHoursMinutesSeconds(450))
#    print(getHoursMinutesSeconds(12884))
    assert getHoursMinutesSeconds(30) == '30s'
    assert getHoursMinutesSeconds(60) == '1m'
    assert getHoursMinutesSeconds(90) == '1m 30s'
    assert getHoursMinutesSeconds(3600) == '1h'
    assert getHoursMinutesSeconds(3601) == '1h 1s'
    assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
    assert getHoursMinutesSeconds(90042) == '25h 42s'
    assert getHoursMinutesSeconds(0) == '0s'


def getHoursMinutesSeconds(total_seconds: int):
    """Converts seconds to formatted hours, minutes and seconds."""

    # Return 0 seconds if total_seconds is zero
    if total_seconds == 0:
        return "0s"

    hours = 0
    """
    Here we keep incrementing hours as long as the total_seconds is greater than 3600
    """
    while total_seconds >= 3600:
        hours += 1
        total_seconds -= 3600

    minutes = 0
    """
    Here we keep incrementing minutes as long as the total_seconds is greater than 60
    """
    while total_seconds >= 60:
        minutes += 1
        total_seconds -= 60

    seconds = total_seconds

    # Formating the time
    hms = []

    if hours > 0:
        hms.append(str(hours) + "h")
    if minutes > 0:
        hms.append(str(minutes) + "m")
    if seconds > 0:
        hms.append(str(seconds) + "s")

    return ' '.join(hms)    
    


if __name__ == "__main__":
    main()
