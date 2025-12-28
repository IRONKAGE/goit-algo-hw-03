import turtle

def koch_line(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_line(t, length, depth - 1)
        t.left(60)
        koch_line(t, length, depth - 1)
        t.right(120)
        koch_line(t, length, depth - 1)
        t.left(60)
        koch_line(t, length, depth - 1)

def draw_koch_snowflake(depth, length=300):
    window = turtle.Screen()
    window.setup(width=800, height=800)
    window.title(f"Сніжинка Коха (Рівень {depth})")
    
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-length / 2, length / 3)
    t.pendown()

    for _ in range(3):
        koch_line(t, length, depth)
        t.right(120)

    print("Малювання завершено. Закрийте вікно, щоб вийти.")
    window.mainloop()

if __name__ == "__main__":
    try:
        level = int(input(f"Рівень 0 — це звичайний трикутник.\n"
                          f"Рівень 3-4 — класична деталізована сніжинка.\n"
                          f"Рівень 6 і вище — малювання може зайняти тривалий час через експоненціальне зростання кількості сегментів.\n"
                          f"Введіть рівень рекурсії (рекомендовано 0-5):\n"))
        if level < 0:
            print("Рівень рекурсії не може бути від'ємним.")
        else:
            draw_koch_snowflake(level)
    except ValueError:
        print("Помилка: будь ласка, введіть ціле число.")
