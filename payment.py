import os

async def process_payment(event, client):
    user_id = event.sender_id
    message = f"💰 Nouvelle demande de paiement par l'utilisateur {user_id}"
    await client.send_message(int(os.getenv("ADMIN_ID")), message)
    await event.respond("✅ Votre demande a été envoyée à l'administrateur.")
