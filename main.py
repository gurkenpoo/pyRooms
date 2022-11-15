from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

# create a window

app = Ursina()

player = FirstPersonController(
    position=(0, 0, 1), model='cube', collider='mesh'
)
ground = Entity(model='plane', texture='grass', collider='mesh', scale=(100, 1, 100), shader=lit_with_shadows_shader)
rectangulo = Entity(model='cube', texture='brick', scale_y=2, collider='mesh', position=(1, 3, 2),
                    shader=lit_with_shadows_shader)
pivot = Entity()

DirectionalLight(parent=pivot, y=2, z=3, shadows=True, rotation=(45, -45, 45))

Sky(texture='sky_sunset')

tooltip_test = Tooltip(
    '<scale:1.5><pink>' + 'Rainstorm' + '<scale:1> \n \n' +
    '''Summon a <blue>rain  
    storm <red>to deal 5 .'''.replace('\n', ' '),
    background_color=color.white
)

tooltip_test.enabled = True

app.run()
