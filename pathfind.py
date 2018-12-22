import tkinter as tk


class PathfinderApp:

    def __init__(self, _root):
        self.root = _root
        self.width = 800
        self.height = 800
        self.refreshing_rate = 50
        self.root.geometry("{}x{}".format(self.width, self.height))
        self.canva_scene = CanvaScene(self)

        self.start_point, self.end_point = self.canva_scene.get_objectives()

    def update(self):
        self.calc_direction(self.start_point, self.end_point)

    def calc_direction(self, _start_point, _end_point):
        pass
    

class CanvaScene:

    def __init__(self, _app):
        self.cell_size = 10
        self.width = 600
        self.height = 600
        self.rows = self.height // self.cell_size
        self.cols = self.width // self.cell_size
        self.cells = []
        self.canva = tk.Canvas(_app.root, bg="white")
        self.canva.config(width=self.width, height=self.height)
        self.canva.pack(side=tk.TOP)

        self.draw_grid()
        self.populate_grid(self.canva)

        self.start_point = self.place_point(10, 24, "start")
        self.end_point = self.place_point(50, 35, "end")
        self.place_point(35, 41, "obstacle")

    def draw_grid(self):
        for i in range(self.rows+1):
            self.canva.create_line(10, (i * self.cell_size), self.width, (i * self.cell_size))
        for j in range(self.cols+1):
            self.canva.create_line((j * self.cell_size), 10, (j * self.cell_size), self.height)

    def populate_grid(self, _canva):
        self.cells = [
            Cell(x, y, self.cell_size, _canva, ((x * self.cols)+y))
            for x in range(self.rows)
            for y in range(self.cols)
        ]

    def place_point(self, _x, _y, _nature):
        cell_index = (_x * self.cols)+_y

        if _nature == "start":
            self.cells[cell_index].fill_color(self.canva, "green")
        elif _nature == "end":
            self.cells[cell_index].fill_color(self.canva, "red")
        elif _nature == "obstacle":
            self.cells[cell_index].fill_color(self.canva, "black")

        return _x, _y

    def get_objectives(self):
        return self.start_point, self.end_point


class Cell:

    def __init__(self, _x, _y, _size, _canva, _id):
        self.coords = (_x, _y)
        self.size = _size
        self.id = _id

        self.rect = _canva.create_rectangle((_x * self.size),
                                            (_y * self.size),
                                            ((_x * self.size) + self.size),
                                            ((_y * self.size) + self.size),
                                            fill='white', tags=self.id)

    def fill_color(self, _canva, _color):
        _canva.itemconfigure(self.rect, fill=_color)


root = tk.Tk()
app = PathfinderApp(root)


# App start point

root.mainloop()



