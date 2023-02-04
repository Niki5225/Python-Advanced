from collections import deque

food_supplies = [int(x) for x in input().split(", ")]
daily_stamina = deque([int(x) for x in input().split(", ")])
peaks = {80: "Vihren",
         90: "Kutelo",
         100: "Banski Suhodol",
         60: "Polezhan",
         70: "Kamenitza"}
day = 1
peak_values = [80, 90, 100, 60, 70]
conquered_peaks = []
while food_supplies and daily_stamina and peak_values and day <= 7:
    stamina = daily_stamina.popleft()
    food = food_supplies.pop()
    result = stamina + food
    current_peak = peak_values[0]

    if result >= current_peak:
        conquered_peaks.append(peaks[current_peak])
        peak_values.remove(current_peak)
    day += 1
if peak_values:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
else:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
if conquered_peaks:
    print("Conquered peaks:")
    for el in conquered_peaks:
        print(el)
