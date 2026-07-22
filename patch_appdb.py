import re

with open("app/src/main/java/com/example/data/AppDatabase.kt", "r") as f:
    content = f.read()

content = content.replace('val passphrase = "messenger_secret_passphrase".toCharArray()', 'val passphrase = CryptoManager.getDatabasePassphrase(context)')
content = content.replace('val factory = SupportFactory("messenger_secret_passphrase".toByteArray())', 'val factory = SupportFactory(String(passphrase).toByteArray())')

with open("app/src/main/java/com/example/data/AppDatabase.kt", "w") as f:
    f.write(content)
