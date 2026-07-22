import re

with open("app/src/main/java/com/example/ui/MainScreen.kt", "r") as f:
    content = f.read()

content = content.replace('                            composable("settings/general") { SettingsGeneralScreen(viewModel, mainNavController) }', '                            composable("settings/general") { SettingsGeneralScreen(viewModel, mainNavController) }\n                            composable("settings/storage") { SettingsStorageScreen(viewModel, mainNavController) }')

with open("app/src/main/java/com/example/ui/MainScreen.kt", "w") as f:
    f.write(content)
