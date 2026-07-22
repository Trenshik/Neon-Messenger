import re

with open("app/src/main/java/com/example/ui/NeonCanvases.kt", "r") as f:
    content = f.read()

content = content.replace(
    'for (i in 0..200) {',
    'val intensity = com.example.utils.PerformanceMonitor.animationIntensity.value\n        val limit = (200 * intensity).toInt().coerceAtLeast(10)\n        for (i in 0..limit) {'
)

with open("app/src/main/java/com/example/ui/NeonCanvases.kt", "w") as f:
    f.write(content)
