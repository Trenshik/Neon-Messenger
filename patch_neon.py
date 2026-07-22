import re

with open("app/src/main/java/com/example/ui/NeonCanvases.kt", "r") as f:
    content = f.read()

# Snowflakes
content = content.replace(
    'val currentDt = dt\n        snowflakes.forEach { flake ->',
    'val currentDt = dt\n        val intensity = com.example.utils.PerformanceMonitor.animationIntensity.value\n        val limit = (snowflakes.size * intensity).toInt().coerceAtLeast(2)\n        snowflakes.take(limit).forEach { flake ->'
)

# Petals
content = content.replace(
    'val currentDt = dt\n        petals.forEach { petal ->',
    'val currentDt = dt\n        val intensity = com.example.utils.PerformanceMonitor.animationIntensity.value\n        val limit = (petals.size * intensity).toInt().coerceAtLeast(2)\n        petals.take(limit).forEach { petal ->'
)

# Confetti
content = content.replace(
    'val currentDt = dt\n        confettiList.forEach { confetti ->',
    'val currentDt = dt\n        val intensity = com.example.utils.PerformanceMonitor.animationIntensity.value\n        val limit = (confettiList.size * intensity).toInt().coerceAtLeast(2)\n        confettiList.take(limit).forEach { confetti ->'
)

with open("app/src/main/java/com/example/ui/NeonCanvases.kt", "w") as f:
    f.write(content)
