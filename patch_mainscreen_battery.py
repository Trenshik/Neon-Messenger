import re

with open("app/src/main/java/com/example/ui/MainScreen.kt", "r") as f:
    content = f.read()

battery_logic = """    var batteryLevel by remember { mutableStateOf(100f) }
    DisposableEffect(Unit) {
        val filter = IntentFilter(Intent.ACTION_BATTERY_CHANGED)
        val receiver = object : BroadcastReceiver() {
            override fun onReceive(ctx: Context?, intent: Intent?) {
                val status: Int = intent?.getIntExtra(BatteryManager.EXTRA_STATUS, -1) ?: -1
                isCharging = status == BatteryManager.BATTERY_STATUS_CHARGING || status == BatteryManager.BATTERY_STATUS_FULL
                
                val level: Int = intent?.getIntExtra(BatteryManager.EXTRA_LEVEL, -1) ?: -1
                val scale: Int = intent?.getIntExtra(BatteryManager.EXTRA_SCALE, -1) ?: -1
                if (level != -1 && scale != -1) {
                    batteryLevel = level * 100f / scale.toFloat()
                }
            }
        }
        context.registerReceiver(receiver, filter)
        onDispose {
            context.unregisterReceiver(receiver)
        }
    }
    
    val isBatterySaver = isBatterySaverSetting && batteryLevel < 20f
"""

content = re.sub(
    r"    DisposableEffect\(Unit\) \{.*?\n    val isBatterySaver = isBatterySaverSetting && !isCharging",
    battery_logic,
    content,
    flags=re.DOTALL
)

with open("app/src/main/java/com/example/ui/MainScreen.kt", "w") as f:
    f.write(content)

