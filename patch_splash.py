import re

with open("app/src/main/java/com/example/ui/MainScreen.kt", "r") as f:
    content = f.read()

# Replace `startDestination = if (isLoggedIn) "main" else "auth"`
old_start = 'startDestination = if (isLoggedIn) "main" else "auth",'
new_start = 'startDestination = "splash",'
content = content.replace(old_start, new_start)

# Add composable("splash") block right after NavHost( ... ) {
# Let's find `NavHost( ... ) {`
navhost_pattern = r'(NavHost\([^)]*\)\s*\{)'
splash_composable = """
        composable("splash") {
            SplashScreen(onSplashFinished = {
                navController.navigate(if (isLoggedIn) "main" else "auth") {
                    popUpTo("splash") { inclusive = true }
                }
            })
        }
"""
content = re.sub(navhost_pattern, r'\1' + splash_composable, content, count=1)

with open("app/src/main/java/com/example/ui/MainScreen.kt", "w") as f:
    f.write(content)

