def func():
    global count
    if count==4:
        return
    else:
        print(count)
        count+=1
        func()

count=0
func()