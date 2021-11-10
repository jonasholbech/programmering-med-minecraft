import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import time
import random
mc = minecraft.Minecraft.create()

#state værdier her
follow = False
goldwalk = False
safeMode = False

def UpdateState():
    if follow == True:
        pos = mc.player.getPos()
        mc.entity.setPos(spawnedPet, pos.x + 2, pos.y, pos.z)
    if goldwalk == True:
        pos = mc.player.getPos()
        mc.setBlock(pos.x, pos.y - 1, pos.z, block.GOLD_BLOCK.id)
    if safeMode == True:
        pos = mc.player.getPos()
        block = mc.getBlock(pos.x, pos.y, pos.z)
        if block == 10 or block == 11:
            cowPos = mc.entity.getPos(spawnedPet)
            mc.entity.setPos(spawnedPet, pos.x, pos.y, pos.z)
            mc.player.setPos(cowPos.x, cowPos.y, cowPos.z)

while True:
    chat = mc.player.pollChatPosts()
    pos = mc.player.getPos()

    if len(chat) > 0:
        
        message = chat[0].message
        parts = message.split(" ")
        if message == "safe":
            safeMode=True
        if parts[0] == 'spawn':
            for i in parts[1::]:
                spawnedPet = mc.spawnEntity(pos.x + 2, pos.y, pos.z, i)
        if message == 'teleport':
            mc.entity.setPos(spawnedPet, pos.x + 2, pos.y, pos.z)
        if message == 'dance':
            for i in range(10):
               petPos = mc.entity.getPos(spawnedPet)
               rand = random.randint(-3,3)
               mc.entity.setPos(spawnedPet, petPos.x + rand, petPos.y, petPos.z + rand)
               time.sleep(0.2)
        if message == 'boom':
            petPos = mc.entity.getPos(spawnedPet)
            mc.spawnEntity(petPos.x, petPos.y + 2, petPos.z, entity.PRIMED_TNT.id)
        if message == 'follow':
            follow = True
        if message == 'unfollow':
            follow = False
        if message == 'goldwalk':
            goldwalk = True
        
        #Tilføj flere kommandoer her
        """
        teleporter op i luften
Koen løber over til en og kaster diamanter
Lege aport
Koen bliver stående og kan ikke rykke sig
Få koen til at dreje rundt (spin)
Hente blocks der ligger på jorden
Løb over til nærmeste diamantblok
Koen følger efter spilleren
Når man rører lava hjælper den en
 - Når du rører lava, skifter du plads med koen
        """
    UpdateState()

    time.sleep(0.1)