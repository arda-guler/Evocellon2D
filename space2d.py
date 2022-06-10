class space2d:
    def __init__(self, autorule=None, cells=[], time=0):
        self.autorule = autorule
        self.cells = cells
        self.size = [len(cells[0]), len(cells)]
        self.time = time

    def set_autorule(self, autorule):
        self.autorule = autorule

    def get_cell(self, x, y):
        try:
            return self.cells[y][x]
        except IndexError:
            return None

    def update(self):
        new_states = []
        
        self.time += 1
        
        sx = self.size[0]
        sy = self.size[1]
        
        for yi in range(sy):
            new_states.append([])
            for xi in range(sx):
                # get cells
                cell = self.get_cell(xi, yi)

                nc1 = self.get_cell(xi-1, yi-1)
                nc2 = self.get_cell(xi,   yi-1)
                nc3 = self.get_cell(xi+1, yi-1)
                nc4 = self.get_cell(xi-1, yi)
                nc5 = self.get_cell(xi+1, yi)
                nc6 = self.get_cell(xi-1, yi+1)
                nc7 = self.get_cell(xi,   yi+1)
                nc8 = self.get_cell(xi+1, yi+1)

                new_state = self.autorule(self.time, cell, nc1, nc2, nc3, nc4, nc5, nc6, nc7, nc8)
                new_states[yi].append(new_state)

        for yi in range(sy):
            for xi in range(sx):
                cell = self.get_cell(xi, yi)
                cell.set_state(new_states[yi][xi])
