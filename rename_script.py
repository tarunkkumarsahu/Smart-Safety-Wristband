import os
import re

root_dir = r"C:\Users\Tarun\OneDrive - MITADTU\Desktop\ALTU FALTU CHIZE\Sakti Armor\app\src"

rename_map = [
    (r"Sakti Armor", "AEGIS"),
    (r"SaktiArmor", "Aegis"),
    (r"saktiarmor", "aegis"),
    (r"Sakti Band", "AEGIS Band"),
    (r"SaktiBand", "AegisBand"),
    (r"saktiband", "aegisband"),
    (r"Sakti Bracelet", "AEGIS Bracelet"),
    (r"SaktiBracelet", "AegisBracelet"),
    (r"Sakti Colors", "AegisColors"),
    (r"SaktiColors", "AegisColors"),
    (r"saktiColors", "aegisColors"),
    (r"SaktiTheme", "AegisTheme"),
    (r"saktiTheme", "aegisTheme"),
    (r"SaktiArmorTheme", "AegisTheme"),
    (r"SAKTI_BLE", "AEGIS_BLE"),
    (r"SAKTI_PACKET", "AEGIS_PACKET"),
    (r"SAKTI ALERT", "AEGIS ALERT"),
    (r'Theme_SaktiArmor', 'Theme_Aegis'),
]

# Specifically protect the package name
package_pattern = re.compile(r"com\.example\.saktiarmor")

def rename_in_content(content):
    # Find all occurrences of the package name and temporarily replace them
    package_placeholders = []
    def sub_package(match):
        placeholder = f"__PACKAGE_PROTECT_{len(package_placeholders)}__"
        package_placeholders.append((placeholder, match.group(0)))
        return placeholder

    protected_content = package_pattern.sub(sub_package, content)

    # Apply renames
    for old, new in rename_map:
        protected_content = re.sub(old, new, protected_content)

    # Restore package names
    for placeholder, original in reversed(package_placeholders):
        protected_content = protected_content.replace(placeholder, original)
    
    return protected_content

def process_files():
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith((".kt", ".xml", ".gradle", ".kts", ".json", ".md")):
                filepath = os.path.join(subdir, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    new_content = rename_in_content(content)
                    
                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Updated: {filepath}")
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    process_files()
