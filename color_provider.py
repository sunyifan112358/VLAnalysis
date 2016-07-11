class ColorProvider:
    r = ['#f21840', '#f23054', '#f24968', '#f2817c', '#f2798f',
            '#f291a3', '#f2aab7', '#f2c2cb', '#f2dade']
    g = ['#46d615', '#56d62b', '#66d640', '#76d656', '#86d66b',
            '#96d681', '#a6d696', '#b6d6ab', '#c6d6c1']
    b = ['#1860f2', '#3071f2', '#4981f2', '#6191f2', '#79a1f2',
            '#91b2f2', '#aac2f2', '#c2d2f2', '#dae2f2']

    def __getitem__(self, index):
        colors = [
            '#cc0000',
            '#ff9933',
            '#ccff33',
            '#009933',
            '#555555',
            '#859eef'
        ]

        return colors[index % len(colors)]

    def get_color_list(self, index):
        if index % 3 == 0:
            return ColorProvider.r
        elif index % 3 == 1:
            return ColorProvider.g
        else:
            return ColorProvider.b
