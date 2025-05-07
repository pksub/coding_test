def solution(storage, usage, change):
    total_usage = 0
    for i in range(len(change)):
        usage = usage * (100 +  change[i])/100
        total_usage += usage
        if total_usage > storage:
            return i
    
    return -1

# storage	usage	change	    result
# 5141	    500	    [10, -10, 10, -10, 10, -10, 10, -10, 10, -10]	-1
# 1000	    2000	[-10, 25, -33]	1