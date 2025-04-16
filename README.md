# ECS Scale Components
Supplementary pack for ECS that adds scale components to all entities from [bedrock-samples](https://github.com/Mojang/bedrock-samples).

> [!CAUTION]
> This will **very** likely not be compatible with other addons, it changes `.json` files, including `player.json`.

It shouldn't be difficult to do a compatability patch with other addons, you only will need to combine the `.json` files from each pack into one. **This is not something I can do for you.**

> [!TIP]
> An `.mcpack`/`.mcaddon` file is in reality just a `.zip` file. You can zip it normally and rename the file extension, just make sure you include the manifest into the pack.

##

What may be useful if you're combining packs yourself are the python and shell scripts. The shell script downloads all the entities from [bedrock-samples](https://github.com/Mojang/bedrock-samples) and the python script will add `minecraft:scale` to all of them. The files inside of [entities](entities) have already been modified with the scripts.

Please make a backup of your `.json` files before running the scripts, they're not perfect.

Note that you **will** need [ECS](https://github.com/Aevarkan/MCBE-extended-commands-suite) or another addon that allows you to change the scale. This pack doesn't include any commands by itself.
