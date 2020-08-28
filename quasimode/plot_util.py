import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def make_grid_and_get_axes_dict(fig):
    d_axes = {'top': {'left': None, 'right': None}, 
              'bottom': {'left': None, 'right': None}}
    gs0 = gridspec.GridSpec(2, 2, hspace=0.2, wspace=0)
    # Bend Angle
    d_axes['top']['left'] = fig.add_subplot(gs0[0,0])
    d_axes['top']['right'] = fig.add_subplot(gs0[0,1], sharex=d_axes['top']['left'], sharey=d_axes['top']['left'])

    # Contour Length
    d_axes['bottom']['left'] = fig.add_subplot(gs0[1,0], sharex=d_axes['top']['left'])
    d_axes['bottom']['right'] = fig.add_subplot(gs0[1,1], sharex=d_axes['top']['left'], sharey=d_axes['bottom']['left'])

    d_axes['top']['right'].yaxis.tick_right()
    d_axes['bottom']['right'].yaxis.tick_right()
    return d_axes

def make_grid_and_get_axes_dict_twiststretch(fig):
    d_axes = {'left': None, 'right': None}
    gs0 = gridspec.GridSpec(1, 2, wspace=0)
    d_axes['left'] = fig.add_subplot(gs0[0,0])
    d_axes['right'] = fig.add_subplot(gs0[0,1], sharex=d_axes['left'], sharey=d_axes['left'])

    d_axes['right'].yaxis.tick_right()
    return d_axes