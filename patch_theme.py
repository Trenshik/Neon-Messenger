import re

with open("app/src/main/java/com/example/ui/theme/Theme.kt", "r") as f:
    content = f.read()

light_colors = """
private val LightColorScheme = lightColorScheme(
    primary = md_theme_light_primary,
    onPrimary = md_theme_light_onPrimary,
    primaryContainer = md_theme_light_primaryContainer,
    onPrimaryContainer = md_theme_light_onPrimaryContainer,
    secondary = md_theme_light_secondary,
    onSecondary = md_theme_light_onSecondary,
    secondaryContainer = md_theme_light_secondaryContainer,
    onSecondaryContainer = md_theme_light_onSecondaryContainer,
    tertiary = md_theme_light_tertiary,
    onTertiary = md_theme_light_onTertiary,
    tertiaryContainer = md_theme_light_tertiaryContainer,
    onTertiaryContainer = md_theme_light_onTertiaryContainer,
    error = md_theme_light_error,
    errorContainer = md_theme_light_errorContainer,
    onError = md_theme_light_onError,
    onErrorContainer = md_theme_light_onErrorContainer,
    background = md_theme_light_background,
    onBackground = md_theme_light_onBackground,
    surface = md_theme_light_surface,
    onSurface = md_theme_light_onSurface,
    surfaceVariant = md_theme_light_surfaceVariant,
    onSurfaceVariant = md_theme_light_onSurfaceVariant,
    outline = md_theme_light_outline,
    inverseOnSurface = md_theme_light_inverseOnSurface,
    inverseSurface = md_theme_light_inverseSurface,
    inversePrimary = md_theme_light_inversePrimary,
)
"""

content = content.replace("@Composable", light_colors + "\n@Composable", 1)

new_theme_logic = """
    val baseColorScheme = if (darkTheme) DarkColorScheme else LightColorScheme
    val colorScheme = baseColorScheme.copy(
        primary = customPrimary ?: baseColorScheme.primary,
        secondary = customSecondary ?: baseColorScheme.secondary
    )
"""

content = content.replace("""    val colorScheme = DarkColorScheme.copy(
        primary = customPrimary ?: DarkColorScheme.primary,
        secondary = customSecondary ?: DarkColorScheme.secondary
    )""", new_theme_logic.strip())

content = content.replace("WindowCompat.getInsetsController(window, view).isAppearanceLightStatusBars = false", "WindowCompat.getInsetsController(window, view).isAppearanceLightStatusBars = !darkTheme")

with open("app/src/main/java/com/example/ui/theme/Theme.kt", "w") as f:
    f.write(content)

