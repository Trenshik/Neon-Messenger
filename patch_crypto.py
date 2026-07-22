import re

with open("app/src/main/java/com/example/data/CryptoManager.kt", "r") as f:
    content = f.read()

# Add a function to get or create a database passphrase
db_passphrase_func = """
    private const val PREF_DB_PASSPHRASE = "db_passphrase"

    fun getDatabasePassphrase(context: Context): CharArray {
        val prefs = context.getSharedPreferences(PREF_FILE_NAME, Context.MODE_PRIVATE)
        var encryptedPassphrase = prefs.getString(PREF_DB_PASSPHRASE, null)
        if (encryptedPassphrase == null) {
            val randomBytes = ByteArray(32)
            java.security.SecureRandom().nextBytes(randomBytes)
            val newPassphrase = android.util.Base64.encodeToString(randomBytes, android.util.Base64.NO_WRAP)
            encryptedPassphrase = encrypt(newPassphrase)
            prefs.edit().putString(PREF_DB_PASSPHRASE, encryptedPassphrase).apply()
            return newPassphrase.toCharArray()
        }
        return decrypt(encryptedPassphrase).toCharArray()
    }
"""

content = content.replace("fun init(context: Context) {", db_passphrase_func + "\n    fun init(context: Context) {")

with open("app/src/main/java/com/example/data/CryptoManager.kt", "w") as f:
    f.write(content)
