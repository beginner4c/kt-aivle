N = int(input())
tod = input()
day = {"MON":1, "TUE":2, "WED":3, "THU":4, "FRI":5, "SAT":6, "SUN":7, 1:"MON", 2:"TUE", 3:"WED", 4:"THU", 5:"FRI", 6:"SAT", 7:"SUN"}
check = day[tod]
N += check

if N > 7 :
    N = N % 7

print(day[N])
