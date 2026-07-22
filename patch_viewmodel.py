import re

with open("app/src/main/java/com/example/ui/AppViewModel.kt", "r") as f:
    content = f.read()

# Add _isDarkThemeEnabled and isDarkThemeEnabled
dark_theme_state = """    private val _isDarkThemeEnabled = MutableStateFlow(repository.getDarkThemeEnabled())
    val isDarkThemeEnabled: StateFlow<Boolean> = _isDarkThemeEnabled.asStateFlow()

"""
content = content.replace('    private val _isAutoThemeEnabled = MutableStateFlow(repository.getAutoThemeSwitcherEnabled())', dark_theme_state + '    private val _isAutoThemeEnabled = MutableStateFlow(repository.getAutoThemeSwitcherEnabled())')

# Add setDarkThemeEnabled function
dark_theme_func = """    fun setDarkThemeEnabled(enabled: Boolean) {
        _isDarkThemeEnabled.value = enabled
        repository.saveDarkThemeEnabled(enabled)
    }

"""
content = content.replace('    fun setAutoThemeEnabled(enabled: Boolean) {', dark_theme_func + '    fun setAutoThemeEnabled(enabled: Boolean) {')

with open("app/src/main/java/com/example/ui/AppViewModel.kt", "w") as f:
    f.write(content)
