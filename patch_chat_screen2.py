with open("app/src/main/java/com/example/ui/ChatScreen.kt", "r") as f:
    lines = f.readlines()

replacement = """                    }
                    IconButton(onClick = { filePickerLauncher.launch(arrayOf("*/*")) }) {
                        Icon(Icons.Filled.AttachFile, contentDescription = "Attach File", tint = MaterialTheme.colorScheme.onSurfaceVariant)
                    }
                    OutlinedTextField(
"""

for i, line in enumerate(lines):
    if "OutlinedTextField(" in line:
        # Check if previous lines have the end of if/else block for emojis
        if lines[i-1].strip() == "}":
            lines[i-1] = replacement
        else:
            # Maybe just insert before OutlinedTextField
            lines.insert(i, """                    IconButton(onClick = { filePickerLauncher.launch(arrayOf("*/*")) }) {
                        Icon(Icons.Filled.AttachFile, contentDescription = "Attach File", tint = MaterialTheme.colorScheme.onSurfaceVariant)
                    }\n""")
        break

with open("app/src/main/java/com/example/ui/ChatScreen.kt", "w") as f:
    f.writelines(lines)
