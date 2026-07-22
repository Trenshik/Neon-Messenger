import re

with open("app/src/main/java/com/example/ui/ParticleSystem.kt", "r") as f:
    content = f.read()

content = content.replace(
    'for (p in particles) {',
    'val intensity = com.example.utils.PerformanceMonitor.animationIntensity.value\n        val limit = (particles.size * intensity).toInt().coerceAtLeast(2)\n        for (i in 0 until limit) {\n            val p = particles[i]'
)

with open("app/src/main/java/com/example/ui/ParticleSystem.kt", "w") as f:
    f.write(content)
