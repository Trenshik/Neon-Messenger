import re

with open("app/src/main/java/com/example/MainActivity.kt", "r") as f:
    content = f.read()

content = content.replace("Context.CONNECTIVITY_SERVICE", "android.content.Context.CONNECTIVITY_SERVICE")

with open("app/src/main/java/com/example/MainActivity.kt", "w") as f:
    f.write(content)
