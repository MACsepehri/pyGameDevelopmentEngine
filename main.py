import GDE

app = GDE.Window((500, 600))

my_obj = GDE.Object(100, 100, app)
my_obj.draw_rect(24, 24, "blue")
my_obj.add_move_condition(GDE.keyboard["a"], "left", 0.5, lambda: print("Moving left"))
my_obj.add_move_condition(GDE.keyboard["d"], "right", 0.5, lambda: print("Moving right"))
my_obj.add_move_condition(GDE.keyboard["w"], "up", 0.5, lambda: print("Moving up"))
my_obj.add_move_condition(GDE.keyboard["s"], "down", 0.5, lambda: print("Moving down"))

def update():
    app.fill_color("white")
    my_obj.callback_keyboard_action()

app.update_window(update)
app.run()