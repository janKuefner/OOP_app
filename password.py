
import time #import a module to count time 
start = time.time() #start timer
n=0 #initialize the counter

while True:
    time.sleep(0.0000000001)
    n=n+1
    if n==9: #this will simulate a password with 4 digits
        end = time.time() #measure end time
        print(end - start) #display delta time aka time it took
        break

n=0 #initialize the counter
while True:
    time.sleep(0.0000000001)
    n=n+1
    if n==99: #this will simulate a password with 4 digits
        end = time.time() #measure end time
        print(end - start) #display delta time aka time it took
        break

n=0 #initialize the counter
while True:
    time.sleep(0.0000000001)
    n=n+1
    if n==999: #this will simulate a password with 4 digits
        end = time.time() #measure end time
        print(end - start) #display delta time aka time it took
        break

n=0 #initialize the counter
while True:
    time.sleep(0.0000000001)
    n=n+1
    if n==9999: #this will simulate a password with 4 digits
        end = time.time() #measure end time
        print(end - start) #display delta time aka time it took
        break


n=0 #initialize the counter
while True:
    time.sleep(0.0000000001)
    n=n+1
    if n==99999: #this will simulate a password with 4 digits
        end = time.time() #measure end time
        print(end - start) #display delta time aka time it took
        break
