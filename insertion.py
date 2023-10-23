import time
def insertion_sort(data,drawData,timeTick):
    for _ in range(1,len(data)):
        key=data[_]
        j=_-1
        while j>=0 and  key < data[j]:
            data[j+1] = data[j]
            drawData(data, ['yellow' if x==j or x==j+1 else "#A90042" for x in range(len(data))])
            time.sleep(timeTick)
            j=j-1
        data[j+1] = key
    drawData(data, ['yellow' for x in range(len(data))])