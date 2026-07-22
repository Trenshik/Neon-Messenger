import re

with open("app/src/main/java/com/example/ui/NeonCanvases.kt", "r") as f:
    content = f.read()

content = content.replace(
    'val currentDt = dt\n        confettiList.forEach { c ->',
    'val currentDt = dt\n        val intensity = com.example.utils.PerformanceMonitor.animationIntensity.value\n        val limit = (confettiList.size * intensity).toInt().coerceAtLeast(2)\n        confettiList.take(limit).forEach { c ->'
)

with open("app/src/main/java/com/example/ui/NeonCanvases.kt", "w") as f:
    f.write(content)
