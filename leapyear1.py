def isYearLeap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def daysInMonth(year, month):
    if isYearLeap(year)== False and month==2:
        return 28
    elif isYearLeap(year)== True and month==2:
        return 29
    elif year == any and month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        return 31
    else:
        return 30


testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	print(result)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
