import os
import re

SCREENS_DIR = r"app/src/main/java/com/example/saktiarmor/ui/screen"
BAND_SCREENS_DIR = r"app/src/main/java/com/example/saktiarmor/band/ui/screen"

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # Fix the extra parenthesis bug: fillMaxSize().background(Color(0xFFFFFFFF)))
    content = content.replace('fillMaxSize().background(Color(0xFFFFFFFF)))', 'fillMaxSize().background(Color(0xFFFFFFFF))')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filepath}")

for root_dir in [SCREENS_DIR, BAND_SCREENS_DIR]:
    if os.path.exists(root_dir):
        for root, _, files in os.walk(root_dir):
            for file in files:
                if file.endswith('.kt'):
                    process_file(os.path.join(root, file))
