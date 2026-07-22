import re

with open("app/src/main/java/com/example/ui/MainScreen.kt", "r") as f:
    content = f.read()

# Fix MainScreen.kt:257 createChat
content = content.replace("viewModel.createChat(name, desc, photo, isPrivate, linkOrUsername, isGroup = true, isChannel = false)", "viewModel.createChat(name, desc, photo, isPrivate, linkOrUsername, true, false)")
content = content.replace("viewModel.createChat(name, desc, photo, isPrivate, linkOrUsername, isGroup = false, isChannel = true)", "viewModel.createChat(name, desc, photo, isPrivate, linkOrUsername, false, true)")

with open("app/src/main/java/com/example/ui/MainScreen.kt", "w") as f:
    f.write(content)

