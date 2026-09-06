#!/usr/bin/env python3
import random
import tkinter as tk


class LinuxPrank:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("sysRender")
        self.root.overrideredirect(True)
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)
        self.root.configure(bg="#000000")
        self.root.bind("<Escape>", lambda event: self.root.destroy())
        self.root.bind("<q>", lambda event: self.root.destroy())
        self.root.bind("<Q>", lambda event: self.root.destroy())
        self.root.bind("<Button-1>", lambda event: self.root.destroy())
        self.root.bind("<KeyPress>", self.handle_keys)

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.canvas = tk.Canvas(
            self.root,
            width=self.width,
            height=self.height,
            bg="#000000",
            highlightthickness=0,
            cursor="none",
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.root.update_idletasks()
        self.root.attributes("-alpha", 0.95)
        self.animate()

    def handle_keys(self, event):
        if event.keysym in {"Escape", "q", "Q"}:
            self.root.destroy()

    def random_color(self):
        return random.choice(["#ff00ff", "#b000ff", "#7a00ff", "#400080", "#000000", "#200020"])

    def draw_vertical_lines(self):
        step = random.randint(8, 18)
        for x in range(0, self.width + step, step):
            line_color = random.choice(["#000000", "#50007a", "#ff00ff", "#7a00ff"])
            width = random.randint(3, 15)
            self.canvas.create_line(
                x, 0, x, self.height,
                fill=line_color,
                width=width,
            )

    def draw_squares(self):
        for _ in range(random.randint(40, 140)):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(20, 320)
            self.canvas.create_rectangle(
                x, y, x + size, y + size,
                fill=self.random_color(),
                outline="",
            )

    def render_frame(self):
        self.canvas.delete("all")

        for _ in range(random.randint(2, 6)):
            self.draw_vertical_lines()

        self.draw_squares()

        if random.randint(0, 2) == 0:
            overlay = random.choice(["#000000", "#180018", "#250028", "#ff00ff", "#050005"])
            self.canvas.create_rectangle(
                0, 0, self.width, self.height,
                fill=overlay,
                outline="",
            )

    def animate(self):
        self.render_frame()
        self.root.after(random.randint(20, 60), self.animate)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    try:
        app = LinuxPrank()
        app.run()
    except tk.TclError as exc:
        print("Erro ao abrir a janela do prank no Linux:")
        print(str(exc))
        print("Verifique se o Tkinter está instalado: sudo pacman -S python-tk")
        raise
