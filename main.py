from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

ground = Entity(
    model='plane',
    texture="grass",
    collider="mesh",
    scale=(100, 1, 100)
)

player = FirstPersonController(jump_height=10)
Sky()

box = Entity(
    model='cube',
    color=color.black,
    collider='box',
    position=(5, 1, 5),
    scale=(10, 15, 8))

app.run()
