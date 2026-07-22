import re

with open("app/src/main/java/com/example/ui/SettingsScreens.kt", "r") as f:
    content = f.read()

dark_theme_switch = """            Row(
                modifier = Modifier.fillMaxWidth().padding(16.dp),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                Text("Global Dark Theme", style = MaterialTheme.typography.bodyLarge)
                Switch(
                    checked = isDarkThemeEnabled,
                    onCheckedChange = { viewModel.setDarkThemeEnabled(it) }
                )
            }
"""

content = content.replace('            HorizontalDivider()\n            Text("Primary Color"', dark_theme_switch + '            HorizontalDivider()\n            Text("Primary Color"')

with open("app/src/main/java/com/example/ui/SettingsScreens.kt", "w") as f:
    f.write(content)
