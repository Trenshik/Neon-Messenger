import re

with open("app/src/main/java/com/example/ui/SettingsScreens.kt", "r") as f:
    content = f.read()

storage_item = """            SettingsListItem(
                icon = { Icon(Icons.Filled.Storage, null, tint = MaterialTheme.colorScheme.onPrimaryContainer) },
                title = "Data and Storage",
                subtitle = "Network and cache usage",
                onClick = { navController.navigate("settings/storage") }
            )"""

content = content.replace('            SettingsListItem(\n                icon = { Icon(Icons.Filled.Settings', storage_item + '\n            SettingsListItem(\n                icon = { Icon(Icons.Filled.Settings')

with open("app/src/main/java/com/example/ui/SettingsScreens.kt", "w") as f:
    f.write(content)

