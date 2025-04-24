from discord import Intents
from discord.ext import commands
from datetime import datetime
from pytz import timezone
from utilities import Utilities, Acolyte


class Bot(commands.Bot):
    def __init__(self):
        intents = Intents.default()
        intents.message_content = True
        intents.typing=True
        intents.members=True
        super().__init__(command_prefix='&', intents=intents, help_command=None, case_insensitive=True)

bot = Bot()

@bot.event
async def on_ready():
    date = datetime.now(timezone('Europe/Warsaw'))
    guild = bot.get_guild(Utilities.guildID)
    chann = bot.get_channel(Utilities.dailyRaportID)
    dayOfWeek = date.strftime("%A")

    print('\n— — — — —\nLoading cogs . . .')
    print("Cogs loaded.\n— — — — —\n")
    print(date.strftime("%d/%m/%Y | %H:%M"))
    print(f'{bot.user.display_name} zgłasza się na służbie!')

    # match dayOfWeek:
    #     case "Monday":
    #         ping = f"<@{}>"

if __name__ == "__main__":
    bot.run(Utilities.OPLOSH_TOKEN, reconnect=True)