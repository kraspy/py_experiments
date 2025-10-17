import random
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


def show_simple_bar():
    x_values = list(range(1, 11))
    y_values = [random.randint(1, 100) for _ in range(10)]

    plt.bar(
        x_values,
        y_values,
        width=0.2,
        color=('r', 'g', 'b', 'm', 'y', 'k', 'b'),
    )

    plt.show()


def show_pie():
    values = [10, 20, 30, 40]

    labels = 'food', 'entertainments', 'travels', 'sport'

    plt.pie(values, labels=labels, colors=('r', 'g', 'y', 'm'))

    plt.show()


# show_simple_plot(
#     (0, 1, 2, 3, 4, 5),
#     (0, 4, 3, 2, 5, 1),
# )

# show_simple_bar()

show_pie()
