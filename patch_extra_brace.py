import re
with open("app/src/main/java/com/example/ui/AppViewModel.kt", "r") as f:
    content = f.read()

# Fix the duplicate '}' left over by the regex
content = content.replace("    }\n    }\n    fun createChat", "    }\n    fun createChat")
# Wait, let's just do a clean replace using standard string replacement since we know the exact text now.

