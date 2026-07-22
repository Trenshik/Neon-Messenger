import re

with open("app/src/main/java/com/example/ui/ChatScreen.kt", "r") as f:
    content = f.read()

replacement = """                    val icon = if (mime.startsWith("image/")) Icons.Filled.Image
                        else if (mime.startsWith("video/")) Icons.Filled.VideoFile
                        else if (mime.startsWith("audio/")) Icons.Filled.AudioFile
                        else Icons.AutoMirrored.Filled.InsertDriveFile

                    var showDownloadDialog by androidx.compose.runtime.remember { androidx.compose.runtime.mutableStateOf(false) }

                    if (showDownloadDialog) {
                        androidx.compose.material3.AlertDialog(
                            onDismissRequest = { showDownloadDialog = false },
                            title = { Text("File Preview") },
                            text = {
                                Column(horizontalAlignment = Alignment.CenterHorizontally, modifier = Modifier.fillMaxWidth()) {
                                    Icon(icon, contentDescription = null, modifier = Modifier.size(64.dp), tint = MaterialTheme.colorScheme.primary)
                                    Spacer(Modifier.height(16.dp))
                                    Text(name, fontWeight = androidx.compose.ui.text.font.FontWeight.Bold)
                                    Text("${size / 1024} KB", style = MaterialTheme.typography.bodyMedium)
                                    Spacer(Modifier.height(16.dp))
                                    Text("Open or download this file to your device?", textAlign = androidx.compose.ui.text.style.TextAlign.Center)
                                }
                            },
                            confirmButton = {
                                TextButton(onClick = { showDownloadDialog = false }) { Text("Download") }
                            },
                            dismissButton = {
                                TextButton(onClick = { showDownloadDialog = false }) { Text("Cancel") }
                            }
                        )
                    }

                    Column {
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            modifier = Modifier
                                .background(MaterialTheme.colorScheme.surface.copy(alpha = 0.2f), RoundedCornerShape(8.dp))
                                .clickable { showDownloadDialog = true }
                                .padding(8.dp)
                        ) {"""

# Replace from `val icon = if (mime...` up to `Row(`
pattern = r'                    val icon = if \(mime\.startsWith\("image/"\)\) Icons\.Filled\.Image.*?Row\('
content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open("app/src/main/java/com/example/ui/ChatScreen.kt", "w") as f:
    f.write(content)

