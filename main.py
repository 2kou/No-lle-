from config.env_loader import load_env
from bot.handlers import start_bot_sync

if __name__ == "__main__":
    load_env()
    print("🚀 Bot déployé avec succès")
    print("✅ Lancement du bot...")
    start_bot_sync()
