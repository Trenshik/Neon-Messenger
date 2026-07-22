import re

with open("app/src/main/java/com/example/MainActivity.kt", "r") as f:
    content = f.read()

imports = """
import android.content.Intent
import android.content.IntentFilter
import android.os.BatteryManager
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
"""

content = content.replace('import androidx.compose.foundation.verticalScroll', 'import androidx.compose.foundation.verticalScroll' + imports)

battery_logic = """
                val isDarkThemeEnabled by viewModel.isDarkThemeEnabled.collectAsState()
                val batterySaverEnabled by viewModel.batterySaverEnabled.collectAsState()
                
                var batteryLevel by androidx.compose.runtime.remember { mutableStateOf(100f) }
                LaunchedEffect(Unit) {
                    val batteryStatus: Intent? = IntentFilter(Intent.ACTION_BATTERY_CHANGED).let { ifilter ->
                        applicationContext.registerReceiver(null, ifilter)
                    }
                    val level: Int = batteryStatus?.getIntExtra(BatteryManager.EXTRA_LEVEL, -1) ?: -1
                    val scale: Int = batteryStatus?.getIntExtra(BatteryManager.EXTRA_SCALE, -1) ?: -1
                    if (level != -1 && scale != -1) {
                        batteryLevel = level * 100f / scale.toFloat()
                    }
                }
                
                val disableNeon = batterySaverEnabled && batteryLevel < 20f
                val finalCustomPrimary = if (disableNeon) null else primary
                val finalCustomSecondary = if (disableNeon) null else secondary

                NeonMessengerTheme(darkTheme = isDarkThemeEnabled, customPrimary = finalCustomPrimary, customSecondary = finalCustomSecondary) {
"""

content = content.replace("""                val isDarkThemeEnabled by viewModel.isDarkThemeEnabled.collectAsState()
                
                NeonMessengerTheme(darkTheme = isDarkThemeEnabled, customPrimary = primary, customSecondary = secondary) {""", battery_logic.strip())


with open("app/src/main/java/com/example/MainActivity.kt", "w") as f:
    f.write(content)
