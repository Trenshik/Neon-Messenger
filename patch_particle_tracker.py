import re

with open("app/src/main/java/com/example/ui/ParticleSystem.kt", "r") as f:
    content = f.read()

content = content.replace(
    'val dt = (time - lastFrameTime) / 1_000_000_000f // seconds',
    'val dt = (time - lastFrameTime) / 1_000_000_000f // seconds\n                    com.example.utils.PerformanceMonitor.trackFrame(dt * 1000f, time / 1_000_000L)'
)

with open("app/src/main/java/com/example/ui/ParticleSystem.kt", "w") as f:
    f.write(content)
