def get_total_days(month):
    if month == 2:
        return 28
    if month == 7 or month == 8:
        return 31
    if month % 2 == 0:
        if month <= 7:
            return 30
        return 31
    else:
        if month <= 7:
            return 31
        return 30


def solve(month, weekday):
    """
    How many weeks are needed?

    Month
    1 = January
    ...
    12 = December

    Weekday
    1 = Monday
    ...
    7 = Sunday

    January has 31 days.
    The number of days alternate between 31 and 30 until December.
    Two exceptions:
        1. February has 28 days(29 in a leap year)
        2. August skips alternation(July and August has 31 days)

    Algorithm
    1. Get days of the given month.
    2. Days / 7 => minimum weeks
    3. Days % 7 => remainder days
    4. Compute additional weeks => Weekday + > 8 ? 2 : 1
    """
    days = get_total_days(month)
    weeks = days // 7
    remainder_days = days % 7
    if remainder_days == 0:
        return weeks
    additional_weeks = 2 if weekday + remainder_days > 8 else 1
    return weeks + additional_weeks


def main():
    month, weekday = input().split()
    answer = solve(int(month), int(weekday))
    print(answer)
    return answer


if __name__ == '__main__':
    main()