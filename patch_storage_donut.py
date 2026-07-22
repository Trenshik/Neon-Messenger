import re

with open("app/src/main/java/com/example/ui/StorageSettingsScreen.kt", "r") as f:
    content = f.read()

donut_chart = """
            // Usage overview
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(32.dp),
                contentAlignment = Alignment.Center
            ) {
                Canvas(modifier = Modifier.size(200.dp)) {
                    var startAngle = -90f
                    val strokeWidth = 32.dp.toPx()
                    
                    if (totalSize > 0) {
                        for (category in categories) {
                            val sweepAngle = (category.sizeMb / totalSize) * 360f
                            drawArc(
                                color = category.color,
                                startAngle = startAngle,
                                sweepAngle = sweepAngle,
                                useCenter = false,
                                style = androidx.compose.ui.graphics.drawscope.Stroke(width = strokeWidth)
                            )
                            startAngle += sweepAngle
                        }
                    } else {
                        drawArc(
                            color = Color.DarkGray,
                            startAngle = 0f,
                            sweepAngle = 360f,
                            useCenter = false,
                            style = androidx.compose.ui.graphics.drawscope.Stroke(width = strokeWidth)
                        )
                    }
                }
                
                Column(horizontalAlignment = Alignment.CenterHorizontally) {
                    Text(String.format("%.1f", totalSize), style = MaterialTheme.typography.displayMedium)
                    Text("MB", style = MaterialTheme.typography.titleMedium, color = MaterialTheme.colorScheme.onSurfaceVariant)
                }
            }
"""

content = re.sub(r'            // Usage overview.*?            // Categories list', donut_chart + '\n            // Categories list', content, flags=re.DOTALL)

with open("app/src/main/java/com/example/ui/StorageSettingsScreen.kt", "w") as f:
    f.write(content)

