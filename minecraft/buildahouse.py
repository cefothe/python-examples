from mcpi.minecraft import *
from mcpi.block import *


def make_house(mc, x, y, z, width, height, length):
    mc.setBlocks(x, y, z, x + width, y + height, z + length, STONE)

    # What happens if we make AIR inside the cube?
    mc.setBlocks(x + 1, y + 1, z + 1,
                 x + width - 2, y + height - 2, z + length - 2, AIR)

mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

width = 10
height = 10
length = 10

# Use the function from the other program
make_house(mc, x, y, z, width, height, length)