import re

with open("app/src/main/java/com/example/ui/AppViewModel.kt", "r") as f:
    content = f.read()

pattern = r'fun sendMessage\(chatId: String, senderId: String, text: String, audioPath: String\? = null, expiresIn: Long\? = null\) \{.*?val msg = Message\((.*?)\)'
replacement = r'''fun sendMessage(chatId: String, senderId: String, text: String, audioPath: String? = null, expiresIn: Long? = null, documentData: String? = null) {
        viewModelScope.launch {
            val sanitizedText = MessageSanitizer.sanitize(text)
            val encryptedMsg = signalProtocolManager.encryptMessage(sanitizedText)
            val msg = Message(\1, documentData = documentData)'''

# Wait, the trailing `)` might be missing in \1. \1 includes all text up to `)`.
# Let's do it safer.

