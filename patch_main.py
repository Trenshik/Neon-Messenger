import re

with open("app/src/main/java/com/example/MainActivity.kt", "r") as f:
    content = f.read()

# Pass isDarkThemeEnabled to NeonMessengerTheme
dark_theme_state = """                val isDarkThemeEnabled by viewModel.isDarkThemeEnabled.collectAsState()
                
                NeonMessengerTheme(darkTheme = isDarkThemeEnabled, customPrimary = primary, customSecondary = secondary) {"""

content = content.replace('                NeonMessengerTheme(customPrimary = primary, customSecondary = secondary) {', dark_theme_state)

with open("app/src/main/java/com/example/MainActivity.kt", "w") as f:
    f.write(content)

