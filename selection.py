import time
def selection_sort(data,drawData,timeTick):
    for step in range(len(data)-1):
        min_idx=step
        for i in range(step+1,len(data)):
            if data[i] < data[min_idx]:
                min_idx=i
                drawData(data, ['yellow' if x==i or x==i+1 else "#A90042" for x in range(len(data))])
                time.sleep(timeTick)
        (data[step],data[min_idx])=(data[min_idx],data[step])
    drawData(data, ['yellow' for x in range(len(data))])