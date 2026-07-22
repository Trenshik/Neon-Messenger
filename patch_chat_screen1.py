with open("app/src/main/java/com/example/ui/ChatScreen.kt", "r") as f:
    lines = f.readlines()

new_vars = """
    var selectedFileUri by remember { mutableStateOf<android.net.Uri?>(null) }
    var selectedFileName by remember { mutableStateOf("") }
    var selectedFileSize by remember { mutableStateOf(0L) }
    var selectedFileMime by remember { mutableStateOf("") }
    var showFilePreviewDialog by remember { mutableStateOf(false) }

    val filePickerLauncher = androidx.activity.compose.rememberLauncherForActivityResult(
        contract = androidx.activity.result.contract.ActivityResultContracts.OpenDocument()
    ) { uri: android.net.Uri? ->
        uri?.let {
            selectedFileUri = it
            var name = "Unknown File"
            var size = 0L
            var mime = context.contentResolver.getType(it) ?: "application/octet-stream"
            context.contentResolver.query(it, null, null, null, null)?.use { cursor ->
                if (cursor.moveToFirst()) {
                    val nameIdx = cursor.getColumnIndex(android.provider.OpenableColumns.DISPLAY_NAME)
                    if (nameIdx != -1) name = cursor.getString(nameIdx)
                    val sizeIdx = cursor.getColumnIndex(android.provider.OpenableColumns.SIZE)
                    if (sizeIdx != -1) size = cursor.getLong(sizeIdx)
                }
            }
            if (size > 5L * 1024 * 1024 * 1024) { // 5 GB limit
                android.widget.Toast.makeText(context, "File exceeds 5 GB limit", android.widget.Toast.LENGTH_SHORT).show()
            } else {
                selectedFileName = name
                selectedFileSize = size
                selectedFileMime = mime
                showFilePreviewDialog = true
            }
        }
    }
"""

for i, line in enumerate(lines):
    if "val context = androidx.compose.ui.platform.LocalContext.current" in line:
        lines.insert(i + 1, new_vars)
        break

with open("app/src/main/java/com/example/ui/ChatScreen.kt", "w") as f:
    f.writelines(lines)
