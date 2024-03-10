from mcpi_e.minecraft import *
from mcpi_e import block

serverAddress = "localhost"
pythonApiPort = 4711

mc=Minecraft.create(serverAddress,pythonApiPort, "cefothe")
pos=mc.player.getTilePos()
(x,y,z)=pos=mc.player.getPos()

mc.setBlock(x+1,y,z,block.WOOL_GREEN)
mc.setBlock(x+2,y,z,block.WOOL_RED)
mc.setBlock(x+3,y,z,block.WOOL_BLUE)