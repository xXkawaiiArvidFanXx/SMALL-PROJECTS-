import matplotlib.pyplot as plt
import numpy as np


def cirklar():
    plt.style.use('_mpl-gallery-nogrid')

    # make data
    X, Y = np.meshgrid(np.linspace(-3, 3, 256), np.linspace(-3, 3, 256))
    Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)
    levels = np.linspace(Z.min(), Z.max(), 7)

    # plot
    fig, ax = plt.subplots()

    ax.contourf(X, Y, Z, levels=levels)

    plt.show()


def chipset():
    from matplotlib import cm

    plt.style.use('_mpl-gallery')
    try:
        
        n_radii =int(input("vad vill du ha för radii"))
        n_angles =int(input("vad vill du ha för vinklar :)"))
    except (SyntaxError, ValueError, TypeError) as e:
                print(f"FEL!!!!!!!!!: {e}")
                

    
    radii = np.linspace(0.125, 1.0, n_radii)
    angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)[..., np.newaxis]

    # Convert polar (radii, angles) coords to cartesian (x, y) coords.
    x = np.append(0, (radii*np.cos(angles)).flatten())
    y = np.append(0, (radii*np.sin(angles)).flatten())
    z = np.sin(-x*y)

    # Plot
    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    ax.plot_trisurf(x, y, z, vmin=z.min() * 2, cmap=cm.Blues)

    ax.set(xticklabels=[],
        yticklabels=[],
        zticklabels=[])

    plt.show()

