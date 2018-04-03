time = 0
timeStep = 0.001 #maa vere liten nok slik at ikke Fd blir crazy stort
timeEnd = 20

J = 2
drumRadius = 40
pRadius = 0.8#i m
theta = 0
thetaDot = 0

y = 200
yDot = 0
m = 100
k = 10**6
b = 10**3
g = 9.81

def calculation(y_pos, yDot, theta, thetaDot, time):
    y = y_pos
    if y < 0:
        Fd = abs(y)*k + (-yDot*b)
    else:
        Fd = 0

    thetaDotDot = (-m*g+Fd)*pRadius/J

    thetaDot += thetaDotDot*timeStep
    theta += thetaDot*timeStep
    yDot = thetaDot*pRadius
    y = y + yDot*timeStep
    time = time + timeStep
    print("thetaDot: %d Time: %d Fd: %d" % (thetaDot, time, Fd))
    return y, yDot, theta, thetaDot, time
