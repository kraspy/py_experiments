import matplotlib.pyplot as plt


def show_simple_plot(
    x: tuple[int, ...],
    y: tuple[int, ...],
    title: str = 'Default Title',
    xlabel: str = 'Label X',
    ylabel: str = 'Label Y',
    legend: bool = True,
    grid: bool = True,
) -> None:
    plt.plot(
        x,
        y,
        # 'o',
        marker='x',  # s, *, D, ^, v, <, >
    )
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if legend:
        plt.legend()
    plt.grid(grid)
    plt.xlim(xmin=0, xmax=50)
    plt.ylim(ymin=0, ymax=20)
    plt.xticks((0, 10, 20), ('tick1', 'tick2', 'tick3'))
    plt.yticks((0, 5, 10), ('Y1', 'Y2', 'Y3'))

    plt.show()


show_simple_plot(
    (0, 1, 2, 3, 4, 5),
    (0, 4, 3, 2, 5, 1),
)
