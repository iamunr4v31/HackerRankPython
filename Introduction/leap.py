def divisibility(a,b):
    return a % b == 0

def is_leap(year):
    return divisibility(year, 400) or (divisibility(year, 4) and not divisibility(year, 100))

print(is_leap(2100))