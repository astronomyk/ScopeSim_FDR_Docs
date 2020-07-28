import matplotlib.pyplot as plt


def make_figs():
    figs = {}
    for i in range(5):
        f = plt.figure()
        f.add_subplot(111)
        f.axes[0].plot([0., 1.], [i, 1./(i+1.)])
        f.axes[0].set_ylim(-5, 5)
        figs[i] = f

    return figs


my_figs = make_figs()
for key in my_figs:
    my_figs[key].show()
    my_figs[key].savefig(f"{key}.png")
