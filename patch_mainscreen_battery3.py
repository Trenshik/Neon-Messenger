import re

with open("app/src/main/java/com/example/ui/MainScreen.kt", "r") as f:
    content = f.read()

battery_logic = """    var isCharging by remember { mutableStateOf(false) }
    var batteryLevel by remember { mutableStateOf(100f) }
    androidx.compose.runtime.DisposableEffect(context) {
        val filter = android.content.IntentFilter(android.content.Intent.ACTION_BATTERY_CHANGED)
        val receiver = object : android.content.BroadcastReceiver() {
            override fun onReceive(ctx: android.content.Context, intent: android.content.Intent) {
                val status: Int = intent.getIntExtra(android.os.BatteryManager.EXTRA_STATUS, -1)
                isCharging = status == android.os.BatteryManager.BATTERY_STATUS_CHARGING || status == android.os.BatteryManager.BATTERY_STATUS_FULL
                
                val level: Int = intent.getIntExtra(android.os.BatteryManager.EXTRA_LEVEL, -1)
                val scale: Int = intent.getIntExtra(android.os.BatteryManager.EXTRA_SCALE, -1)
                if (level != -1 && scale != -1) {
                    batteryLevel = level * 100f / scale.toFloat()
                }
            }
        }
        context.registerReceiver(receiver, filter)
        onDispose {
            context.unregisterReceiver(receiver)
        }
    }"""

# I need to replace from 'var isCharging' to '    }'
content = re.sub(
    r"    var isCharging by remember \{ mutableStateOf\(false\) \}.*?        }\n    }",
    battery_logic,
    content,
    flags=re.DOTALL
)

with open("app/src/main/java/com/example/ui/MainScreen.kt", "w") as f:
    f.write(content)
