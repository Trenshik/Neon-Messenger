import re

with open("app/src/main/java/com/example/ui/SettingsScreens.kt", "r") as f:
    content = f.read()

battery_switch = """
            val batterySaverEnabled by viewModel.batterySaverEnabled.collectAsState()
            Row(
                modifier = Modifier.fillMaxWidth().padding(horizontal = 16.dp, vertical = 14.dp),
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.SpaceBetween
            ) {
                Text("Battery Saver (Disables Neon)", style = MaterialTheme.typography.bodyLarge)
                Switch(checked = batterySaverEnabled, onCheckedChange = { viewModel.setBatterySaverEnabled(it) })
            }
"""

content = content.replace('            SettingsSimpleItem("Chat Background", "Default", onClick = {})', '            SettingsSimpleItem("Chat Background", "Default", onClick = {})\n' + battery_switch)

with open("app/src/main/java/com/example/ui/SettingsScreens.kt", "w") as f:
    f.write(content)

