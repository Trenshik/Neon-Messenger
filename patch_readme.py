with open("BOT_API_README.md", "r") as f:
    content = f.read()

target = """## Included Examples"""

replacement = """## Webhooks

The Bot API supports receiving real-time updates from the messenger server via webhooks. This is useful for integrating your bot with an external backend.

To configure a webhook:
1. Talk to **@BotFather** in the app.
2. Select your bot and navigate to the **Webhook** setting.
3. Enter your HTTPS URL (e.g., `https://your-server.com/webhook`).

When a message is received by the bot, the messenger server will send an HTTP POST request to your configured webhook URL with a JSON payload:

```json
{
  "update_type": "message",
  "bot_id": "your_bot_id",
  "message": {
    "text": "Hello bot!",
    "chat_id": "user_id_123"
  }
}
```

If your server responds with an HTTP `200 OK` status code and a JSON body containing a `text` field, the bot will automatically reply with that text:

```json
{
  "text": "Hello human!"
}
```

If no webhook is configured or the webhook fails, the bot will fall back to its internal evaluation logic.

## Included Examples"""

if target in content:
    content = content.replace(target, replacement)
    with open("BOT_API_README.md", "w") as f:
        f.write(content)
    print("Readme patched successfully.")
else:
    print("Target not found.")
