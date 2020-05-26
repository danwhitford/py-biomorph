import turtle
import random

def reset():
    turtle.clearscreen()


def random_angle():
    return random.randrange(180)


def random_line():
    return random.randrange(50)


def print_genes(genes, offset=0):
    t = turtle.Turtle()
    t.speed(0)
    t.seth(90)
    t.penup()
    t.setx(offset)
    t.sety(-100)
    t.pendown()
    t.fd(100)
    turtle_group = [t]
    for angle, line in genes:
        # Copy list before looping or it will never end
        for t1 in list(turtle_group):
            t2 = t1.clone()
            t2.left(angle)
            t1.right(angle)
            turtle_group.append(t2)
        for t1 in turtle_group:
            t1.fd(line)


def make_genes():
    return [
        [(random_angle(), random_line())],
        [(random_angle(), random_line())],
        [(random_angle(), random_line())],
    ]


def mutate_genes(genes):
    for angle, line in genes:
        angle *= random.uniform(0.9, 1.1)
        line *= random.uniform(0.9, 1.1)
    if random.randrange(3):
        genes.append((random_angle(), random_line()))


turtle.fd(50)
turtle.speed(0)

genes = make_genes()

screen = turtle.Screen()
screen.screensize(1200, 600)
screen.setup(1200, 600)
OFFSET_SIZE = screen.window_width() / 4
print(OFFSET_SIZE)

while True:
    reset()
    for i, gene in enumerate(genes):   
        offset = -OFFSET_SIZE + (i * OFFSET_SIZE)     
        print_genes(gene, offset)
    cont = screen.numinput("Picker", "Enter 1 to or 3")
    cont = int(cont)
    cont = cont % 3
    cont = cont - 1
    picked = genes[cont]
    genes = [list(picked), list(picked), list(picked)]
    for gene in genes:
        mutate_genes(gene)

print("Finished")
turtle.done()
