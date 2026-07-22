with open("app/src/main/java/com/example/ui/ChatScreen.kt", "r") as f:
    lines = f.readlines()

dialog_code = """
        if (showFilePreviewDialog) {
            androidx.compose.material3.AlertDialog(
                onDismissRequest = { showFilePreviewDialog = false },
                title = { Text("Send File") },
                text = {
                    Column(horizontalAlignment = Alignment.CenterHorizontally) {
                        val icon = if (selectedFileMime.startsWith("image/")) Icons.Filled.Image
                            else if (selectedFileMime.startsWith("video/")) Icons.Filled.VideoFile
                            else if (selectedFileMime.startsWith("audio/")) Icons.Filled.AudioFile
                            else Icons.Filled.InsertDriveFile
                            
                        Icon(
                            icon,
                            contentDescription = "File Icon",
                            modifier = Modifier.size(64.dp),
                            tint = MaterialTheme.colorScheme.primary
                        )
                        Spacer(Modifier.height(16.dp))
                        Text(selectedFileName, style = MaterialTheme.typography.bodyLarge, fontWeight = androidx.compose.ui.text.font.FontWeight.Bold)
                        Text("Size: ${selectedFileSize / 1024} KB", style = MaterialTheme.typography.bodyMedium)
                        Spacer(Modifier.height(16.dp))
                        OutlinedTextField(
                            value = inputText,
                            onValueChange = { inputText = it },
                            label = { Text("Add a caption...") },
                            modifier = Modifier.fillMaxWidth()
                        )
                    }
                },
                confirmButton = {
                    TextButton(onClick = {
                        showFilePreviewDialog = false
                        val documentJson = org.json.JSONObject().apply {
                            put("uri", selectedFileUri.toString())
                            put("name", selectedFileName)
                            put("size", selectedFileSize)
                            put("mimeType", selectedFileMime)
                        }.toString()
                        viewModel.sendMessage(
                            chatId = chatId,
                            senderId = activeAccount?.id ?: "",
                            text = inputText, // caption
                            audioPath = null,
                            expiresIn = expiresIn,
                            documentData = documentJson
                        )
                        inputText = ""
                    }) {
                        Text("Send")
                    }
                },
                dismissButton = {
                    TextButton(onClick = { showFilePreviewDialog = false }) {
                        Text("Cancel")
                    }
                }
            )
        }
"""

for i, line in enumerate(lines):
    if "Column(modifier = Modifier.fillMaxSize().padding(padding).consumeWindowInsets(padding).imePadding())" in line:
        lines.insert(i, dialog_code)
        break

with open("app/src/main/java/com/example/ui/ChatScreen.kt", "w") as f:
    f.writelines(lines)
