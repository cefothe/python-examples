from mcpi.minecraft import Minecraft
import time

# Connect to Minecraft Pi
mc = Minecraft.create()

def getPlayerPosition(name):
    presentId = mc.getPlayerEntityId("cefothe")
    return mc.entity.getPos(presentId)


# Get a list of all connected players
players = mc.getPlayerEntityIds()


# This should get the Id of user "Present"
PresentId = mc.getPlayerEntityId("cefothe")

pos = getPlayerPosition("cefothe")
x = pos.x
y = pos.y
z = pos.z
blocktype = 1
mc.setBlock(x, y, z, blocktype)