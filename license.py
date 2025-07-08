async def check_license(event, client):
    user_id = str(event.sender_id)
    await event.respond("Entrez votre licence :")
    response = await client.wait_for(events.NewMessage(from_users=user_id))
    code = response.raw_text.strip()

    if code.startswith(user_id) and len(code) > 20:
        await event.respond("✅ Licence validée. Accès débloqué.")
    else:
        await event.respond("❌ Licence invalide ou volée.")
