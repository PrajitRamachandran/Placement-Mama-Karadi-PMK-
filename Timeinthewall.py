def clock_angle(hour: int, minute: int) -> float:
    # Checking for valid input
    if hour < 0 or minute < 0 or hour > 12 or minute > 60:
        return "Invalid input"

    # Reset hour to 0 if it is 12
    if hour == 12:
        hour = 0
    # Reset minute to 0 if it is 60
    if minute == 60:
        minute = 0
    
    # Calculating the angles
    hour_angle = 0.5 * (hour * 60 + minute)
    minute_angle = 6 * minute

    # Calculating the angle between hour and minute hands
    angle = abs(hour_angle - minute_angle)
    angle = min(360 - angle, angle)  # Get the smallest angle

    return angle

# Input
hour = 9
minute = 15

# Output
print(f"The angle between the hour and minute hands at {hour}:{minute} is {clock_angle(hour, minute)} degrees.")
