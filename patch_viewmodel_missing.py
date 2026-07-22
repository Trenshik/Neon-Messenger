import re

with open("app/src/main/java/com/example/ui/AppViewModel.kt", "r") as f:
    content = f.read()

# Fix unpinMessage, pinMessage, etc.
content = content.replace(
    'fun unpinMessage(messageId: String) {',
    'fun unpinMessage(chatId: String, messageId: String) {'
)
content = content.replace(
    'fun pinMessage(messageId: String) {',
    'fun pinMessage(chatId: String, messageId: String) {'
)

# Fix verify2FA
content = content.replace(
    'fun verify2FA(accountId: String, code: String) {',
    'fun verify2FA(code: String) {'
)

# Fix addBot
content = content.replace(
    'fun addBot(chatId: String, botId: String, botName: String) {}',
    'fun addBot(chat: Chat) { viewModelScope.launch { repository.insertChat(chat) } }'
)

# Fix toggleArchive
content = content.replace(
    'fun toggleArchive(chatId: String) {',
    'fun toggleArchive(chatId: String, isArchived: Boolean) {'
)

# Fix createChat
create_chat_old = """    fun createChat(name: String, isGroup: Boolean = false, isSecret: Boolean = false, isChannel: Boolean = false) {
        viewModelScope.launch {
            val chat = Chat(id = java.util.UUID.randomUUID().toString(), name = name, isGroup = isGroup, isSecret = isSecret, isChannel = isChannel)
            repository.insertChat(chat)
        }
    }"""
create_chat_new = """    fun createChat(name: String, desc: String, photo: String, isPrivate: Boolean, linkOrUsername: String, isGroup: Boolean = false, isChannel: Boolean = false) {
        viewModelScope.launch {
            val chat = Chat(id = java.util.UUID.randomUUID().toString(), title = name, isGroup = isGroup, isSecret = false, isChannel = isChannel, lastMessage = "")
            repository.insertChat(chat)
        }
    }"""
content = content.replace(create_chat_old, create_chat_new)

# Fix createSecretChat
create_secret_chat_old = """    fun createSecretChat(contactId: String) {
        viewModelScope.launch {
            val chat = Chat(id = java.util.UUID.randomUUID().toString(), name = "Secret Chat", isGroup = false, isSecret = true)
            repository.insertChat(chat)
        }
    }"""
create_secret_chat_new = """    fun createSecretChat(contactId: String) {
        viewModelScope.launch {
            val chat = Chat(id = java.util.UUID.randomUUID().toString(), title = "Secret Chat", isGroup = false, isSecret = true, lastMessage = "")
            repository.insertChat(chat)
        }
    }"""
content = content.replace(create_secret_chat_old, create_secret_chat_new)

with open("app/src/main/java/com/example/ui/AppViewModel.kt", "w") as f:
    f.write(content)
