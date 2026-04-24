import os
import re

SCREENS_DIR = r"app/src/main/java/com/example/saktiarmor/ui/screen"
BAND_SCREENS_DIR = r"app/src/main/java/com/example/saktiarmor/band/ui/screen"

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # 1. Update Scaffold containerColor
    # Scaffold(containerColor = SaktiColors.Abyss) -> Scaffold(containerColor = Color(0xFFFFFFFF), contentColor = Color(0xFF0F172A),)
    content = re.sub(r'containerColor\s*=\s*[a-zA-Z0-9_.]+', 'containerColor = Color(0xFFFFFFFF), contentColor = Color(0xFF0F172A)', content)
    
    # 2. Update Column root background if it follows fillMaxSize
    # modifier = Modifier.fillMaxSize().background(SaktiColors.Abyss)
    content = re.sub(r'fillMaxSize\(\)\s*\.\s*background\([^)]+\)', 'fillMaxSize().background(Color(0xFFFFFFFF))', content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            # ensure Color is imported if modified
            if 'import androidx.compose.ui.graphics.Color' not in content:
                content = content.replace('import androidx.compose.ui.Modifier\n', 'import androidx.compose.ui.Modifier\nimport androidx.compose.ui.graphics.Color\n')
            f.write(content)
        print(f"Updated {filepath}")

for root_dir in [SCREENS_DIR, BAND_SCREENS_DIR]:
    if os.path.exists(root_dir):
        for root, _, files in os.walk(root_dir):
            for file in files:
                if file.endswith('.kt'):
                    process_file(os.path.join(root, file))
