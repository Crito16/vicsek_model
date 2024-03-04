import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

v_0 = 0.001
r_i = 2
noise = 0.01
x = np.random.uniform(1, 6, 10)
y = np.random.uniform(1, 6, 10)
theta = np.random.uniform(0, 2 * (np.pi), 10)

fig, ax = plt.subplots(layout='constrained')
scat = ax.scatter([],[])
ax.set(xlim=[-0.5,6.5], ylim=[- 0.5,6.5])
#print(neighbours(0))
#print(x[0])



# The next function returns an array with the values of the theta parameter
# of the neightbours of the element i considering a radious of r_i
def neighbours(i):
    theta_n=np.empty(0)
    cnum=np.empty(0)
    for j in range(len(x)):
        if j!=i:
            d_x = x[i]-x[j]
            d_y = y[i]-y[j]
            r = np.sqrt((d_x)**2 + (d_y)**2)
            if r < r_i:
                theta_n = np.append(theta_n, theta[j])

    for j in range (len(theta_n)):
        cnum = np.append(cnum,np.cos(theta_n[j]) + complex(0,np.sin(theta_n[j])))
    return np.angle(np.sum(cnum))

def update(dt):
    for i in range(len(x)):
        theta[i] = neighbours(i) + noise
        x[i] = (x[i] + v_0*np.cos(theta[i])*dt) % 6
        y[i] = (y[i] + v_0*np.sin(theta[i])*dt) % 6
    data = np.stack([x,y]).T
    scat.set_offsets(data)
    return scat


ani = anim.FuncAnimation(fig=fig, func=update, interval=80)
plt.show()