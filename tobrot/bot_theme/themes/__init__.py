from tobrot import BOT_THEME
from tobrot.bot_theme.themes import fx_optimised

def BotTheme():
    if BOT_THEME == "fx-optimized-theme":
        return fx_optimised.TXStyle()
    elif BOT_THEME == "fx-minimal-theme":
        TXStyle()
    elif BOT_THEME == "fx-destructive-theme":
        TXStyle()
