import re

with open("app/src/main/java/com/example/MainActivity.kt", "r") as f:
    content = f.read()

imports = """
import android.net.ConnectivityManager
import android.net.Network
import android.net.NetworkCapabilities
import android.net.NetworkRequest
import com.example.ui.ConnectionStatus
"""

content = content.replace('import androidx.compose.runtime.setValue', 'import androidx.compose.runtime.setValue' + imports)

network_logic = """
            val viewModel: AppViewModel by viewModels { factory }
            viewModel.checkAutoTheme()

            val connectivityManager = getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
            val networkRequest = NetworkRequest.Builder()
                .addCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
                .build()

            val networkCallback = object : ConnectivityManager.NetworkCallback() {
                override fun onAvailable(network: Network) {
                    viewModel.setConnectionStatus(ConnectionStatus.ONLINE)
                }
                override fun onLost(network: Network) {
                    viewModel.setConnectionStatus(ConnectionStatus.OFFLINE)
                }
            }

            try {
                connectivityManager.registerNetworkCallback(networkRequest, networkCallback)
            } catch (e: Exception) {
                e.printStackTrace()
            }
"""

content = content.replace("""            val viewModel: AppViewModel by viewModels { factory }
            viewModel.checkAutoTheme()""", network_logic.strip())

with open("app/src/main/java/com/example/MainActivity.kt", "w") as f:
    f.write(content)

