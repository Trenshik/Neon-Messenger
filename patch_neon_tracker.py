import re

with open("app/src/main/java/com/example/ui/NeonCanvases.kt", "r") as f:
    content = f.read()

content = content.replace(
    'dt = (time - lastTime) / 1_000_000_000f',
    'val dtSec = (time - lastTime) / 1_000_000_000f\n                        dt = dtSec\n                        com.example.utils.PerformanceMonitor.trackFrame(dtSec * 1000f, time / 1_000_000L)'
)

with open("app/src/main/java/com/example/ui/NeonCanvases.kt", "w") as f:
    f.write(content)
