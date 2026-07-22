import re

with open("app/src/main/java/com/example/data/AppDatabase.kt", "r") as f:
    content = f.read()

dark_theme_methods = """
    fun getDarkThemeEnabled(): Boolean = sharedPrefs.getBoolean("dark_theme", true)
    fun saveDarkThemeEnabled(enabled: Boolean) = sharedPrefs.edit().putBoolean("dark_theme", enabled).apply()
"""
content = content.replace('fun getAutoThemeSwitcherEnabled(): Boolean', dark_theme_methods.strip() + '\n    fun getAutoThemeSwitcherEnabled(): Boolean')

with open("app/src/main/java/com/example/data/AppDatabase.kt", "w") as f:
    f.write(content)
