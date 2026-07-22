import re

with open("app/src/main/java/com/example/ui/AppViewModel.kt", "r") as f:
    content = f.read()

# Fix unpinMessage
content = re.sub(r'fun unpinMessage\(messageId: String\) \{', 'fun unpinMessage(chatId: String, messageId: String) {', content)
# Fix pinMessage
content = re.sub(r'fun pinMessage\(messageId: String\) \{', 'fun pinMessage(chatId: String, messageId: String) {', content)
# Fix createChat
content = re.sub(r'fun createChat\(name: String, isGroup: Boolean = false, isSecret: Boolean = false, isChannel: Boolean = false\) \{.*?\}', 'fun createChat(name: String, desc: String, photo: String, isPrivate: Boolean, linkOrUsername: String, isGroup: Boolean = false, isChannel: Boolean = false) {\n        viewModelScope.launch {\n            val chat = Chat(id = java.util.UUID.randomUUID().toString(), title = name, isGroup = isGroup, isSecret = false, isChannel = isChannel, lastMessage = "")\n            repository.insertChat(chat)\n        }\n    }', content, flags=re.DOTALL)
# Fix createSecretChat
content = re.sub(r'fun createSecretChat\(contactId: String\) \{.*?\}', 'fun createSecretChat(contactId: String) {\n        viewModelScope.launch {\n            val chat = Chat(id = java.util.UUID.randomUUID().toString(), title = "Secret Chat", isGroup = false, isSecret = true, lastMessage = "")\n            repository.insertChat(chat)\n        }\n    }', content, flags=re.DOTALL)

with open("app/src/main/java/com/example/ui/AppViewModel.kt", "w") as f:
    f.write(content)

with open("app/src/main/java/com/example/MainActivity.kt", "r") as f:
    content = f.read()
content = content.replace("Context.CONNECTIVITY_SERVICE", "android.content.Context.CONNECTIVITY_SERVICE")
content = content.replace("getSystemService(Context.CONNECTIVITY_SERVICE)", "getSystemService(android.content.Context.CONNECTIVITY_SERVICE)")
with open("app/src/main/java/com/example/MainActivity.kt", "w") as f:
    f.write(content)

