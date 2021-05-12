import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

time = input("Time (HH.MM.): ")

def time_conversion(time):
    # converts input string time to int minutes
    try:
        hour, minutes = time.strip('.').split('.')
        hour, minutes = int(hour), int(minutes)
    except ValueError:
        return None
    if hour < 0 or hour > 24:
        return None
    if hour == 0:
        hour = 24
    if minutes < 0 or minutes > 59:
        return None
    minutes += hour*60
    return minutes

def lights(time):
    # checkin if day/night time
    # and light conditions with respective hours converted to mins:
    if time_conversion(time):
        mins = time_conversion(time)
        #    time between 2AM and 5.30AM
        if mins >= (120) and mins < (330):
            return 'Night_off'
        #    time between 5.30AM till 8PM
        elif mins >= 330 and mins < 1200:
            return 'Day'
        else:
        #   remaining time from 8PM till 5.30AM when lights are on
            return 'Night_on'
    else:
        #    in case invalid time input
        print('Invalid input. Accepted time format: (HH.MM.)')
        return None
def chance(time):
    #   defines chance for individual lights to be switched on
    #   from 95% chance at 8PM gradually decreasing to 0% at 2AM
    if time_conversion(time) is not None:
        hrs = time_conversion(time)/60
        if hrs < 20:
            hrs += 24
        hrs -= 20
        return 95 - (hrs*15.8)

def windows():
    #   creating the array representing the windows
    #   applying chance of switched on if applicable
    mode = lights(time)
    a = np.zeros(20)
    if mode == 'Night_on':
        for i in range(20):
            if np.random.randint(1, 101) <= chance(time):
                a[i] = 1
    a = a.reshape(5, 4)
    return a
def clrs():
    #   setting 'glass' and 'wall' colors in relation to day/night
    #   plus title
    mode = lights(time)
    if mode:
        if mode == 'Day':
            glass_clr = ['#add8e6', 'y']
            wall_clr = '#e7ccab'
            title = 'Daytime (5.30-19.59)'
        else:
            glass_clr = ['#161616', '#fff59c']
            wall_clr = '#453a2c'
            title = 'Night time (20.00-5.29)'
    return glass_clr, wall_clr, title


try:
    #   color parameters for windows and wall
    #   setting the boundaries for on/off lights
    glass, wall, title = clrs()
    cmap = mpl.colors.ListedColormap(glass)
    bounds = [0., 0.5, 1.]
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

    wd = windows()
    im = plt.imshow(wd, interpolation='none', cmap=cmap, norm=norm)
    #   creating 'walls' with minor ticks and step correction, removing ticklables
    ax = plt.gca()
    ax.set_xticks(np.arange(-.5, 4, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 5, 1), minor=True)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(which='minor', color=wall, linestyle='-', linewidth=20)
    ax.set(title=title)

    plt.show()
except UnboundLocalError:
    #   in case invalid input exception handling
    pass