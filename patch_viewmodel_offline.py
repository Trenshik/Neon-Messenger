import re

with open("app/src/main/java/com/example/ui/AppViewModel.kt", "r") as f:
    content = f.read()

# Modify sendMessage
send_msg_logic = """    fun sendMessage(chatId: String, senderId: String, text: String, audioPath: String? = null, expiresIn: Long? = null, documentData: String? = null) {
        viewModelScope.launch {
            val sanitizedText = MessageSanitizer.sanitize(text)
            val encryptedMsg = signalProtocolManager.encryptMessage(sanitizedText)
            
            // If offline, message stays locally pending
            val isOnline = _connectionStatus.value == ConnectionStatus.ONLINE
            val msg = Message(
                id = java.util.UUID.randomUUID().toString(),
                chatId = chatId,
                senderId = senderId,
                text = encryptedMsg,
                audioPath = audioPath,
                timestamp = System.currentTimeMillis(),
                expiresAt = if (expiresIn != null) System.currentTimeMillis() + expiresIn else null,
                documentData = documentData,
                isDelivered = isOnline // if offline, it stays pending (not delivered)
            )
            repository.insertMessage(msg)
            
            if (isOnline) {
                // Simulate reply if online
                kotlinx.coroutines.delay(1000)
                simulateTyping(chatId)
                
                val chat = repository.allChats.firstOrNull()?.find { it.id == chatId }
                if (chat != null) {
                    kotlinx.coroutines.delay(1500)
                    val reply = Message(
                        id = java.util.UUID.randomUUID().toString(),
                        chatId = chatId,
                        senderId = "other_user",
                        text = signalProtocolManager.encryptMessage("Got it: $sanitizedText"),
                        timestamp = System.currentTimeMillis(),
                        isDelivered = true
                    )
                    repository.insertMessage(reply)
                }
            }
        }
    }"""

content = re.sub(r'    fun sendMessage\(chatId: String.*?(?=\n    fun (editMessage|updateReaction|toggle2FA))', send_msg_logic + '\n', content, flags=re.DOTALL)

# Add logic for when connection restores
connection_restore = """    fun setConnectionStatus(status: ConnectionStatus) {
        _connectionStatus.value = status
        if (status == ConnectionStatus.ONLINE) {
            processOfflineQueue()
        }
    }
    
    private fun processOfflineQueue() {
        viewModelScope.launch {
            val chats = repository.allChats.firstOrNull() ?: emptyList()
            for (chat in chats) {
                val messages = repository.getMessages(chat.id).firstOrNull() ?: emptyList()
                val pendingMessages = messages.filter { !it.isDelivered && it.senderId != "other_user" }
                for (msg in pendingMessages) {
                    // Mark as delivered
                    repository.updateMessageDelivery(msg.id, true)
                    
                    // Simulate reply
                    kotlinx.coroutines.delay(1000)
                    simulateTyping(chat.id)
                    kotlinx.coroutines.delay(1500)
                    val reply = Message(
                        id = java.util.UUID.randomUUID().toString(),
                        chatId = chat.id,
                        senderId = "other_user",
                        text = signalProtocolManager.encryptMessage("Offline msg received: ${msg.text}"),
                        timestamp = System.currentTimeMillis(),
                        isDelivered = true
                    )
                    repository.insertMessage(reply)
                }
            }
        }
    }"""

content = content.replace("    fun toggle2FA", connection_restore + "\n\n    fun toggle2FA")

with open("app/src/main/java/com/example/ui/AppViewModel.kt", "w") as f:
    f.write(content)

