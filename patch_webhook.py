with open("app/src/main/java/com/example/ui/botapi/BotFather.kt", "r") as f:
    content = f.read()

target = """        // Simple echo for custom bots. In a real system, this would evaluate `code` or call `webhookUrl`.
        val reply = "Echo from $name: $messageText"
        logs.add(LogEntry(message = "Replied: $reply"))
        sendReply(reply, chat.id, repository, signalProtocolManager)"""

replacement = """        if (!webhookUrl.isNullOrBlank()) {
            logs.add(LogEntry(message = "Dispatching to webhook: $webhookUrl"))
            try {
                val responseText = kotlinx.coroutines.withContext(kotlinx.coroutines.Dispatchers.IO) {
                    val url = java.net.URL(webhookUrl)
                    val conn = url.openConnection() as java.net.HttpURLConnection
                    conn.requestMethod = "POST"
                    conn.setRequestProperty("Content-Type", "application/json")
                    conn.doOutput = true
                    
                    val payload = \"\"\"
                    {
                      "update_type": "message",
                      "bot_id": "$id",
                      "message": {
                        "text": "$messageText",
                        "chat_id": "${chat.id}"
                      }
                    }
                    \"\"\".trimIndent()
                    
                    conn.outputStream.use { os ->
                        val input = payload.toByteArray(Charsets.UTF_8)
                        os.write(input, 0, input.size)
                    }
                    
                    val responseCode = conn.responseCode
                    if (responseCode in 200..299) {
                        conn.inputStream.bufferedReader().readText()
                    } else {
                        null
                    }
                }
                logs.add(LogEntry(message = "Webhook dispatched successfully."))
                if (!responseText.isNullOrBlank()) {
                    var reply = responseText
                    if (responseText!!.contains("\\"text\\":")) {
                        val textMatch = "\\"text\\"\\\\s*:\\\\s*\\"([^\\"]+)\\"".toRegex().find(responseText!!)
                        if (textMatch != null) {
                            reply = textMatch.groupValues[1]
                        }
                    }
                    logs.add(LogEntry(message = "Webhook reply: $reply"))
                    sendReply(reply, chat.id, repository, signalProtocolManager)
                }
                return
            } catch (e: Exception) {
                logs.add(LogEntry(level = "ERROR", message = "Webhook failed: ${e.message}"))
            }
        }

        // Simple echo for custom bots. In a real system, this would evaluate `code` or call `webhookUrl`.
        val reply = "Echo from $name: $messageText"
        logs.add(LogEntry(message = "Replied: $reply"))
        sendReply(reply, chat.id, repository, signalProtocolManager)"""

if target in content:
    content = content.replace(target, replacement)
    with open("app/src/main/java/com/example/ui/botapi/BotFather.kt", "w") as f:
        f.write(content)
    print("Patch applied successfully.")
else:
    print("Target not found.")

