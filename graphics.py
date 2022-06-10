def render_space(c, s, cs, t):
    c.delete("all")
    cell_size = cs
    
    sx = s.size[0]
    sy = s.size[1]
    
    for y in range(sy):
        for x in range(sx):
            if s.get_cell(x, y).state:
                gx1 = x * cell_size
                gy1 = y * cell_size
                gx2 = gx1 + cell_size
                gy2 = gy1 + cell_size

                c.create_rectangle(gx1, gy1, gx2, gy2, fill="white")

            else:
                pass

    c.create_text(10, 10, anchor="nw", text=str(t), fill="red")

