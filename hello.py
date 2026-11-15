
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Check that this is your Vite project
if not (ROOT / "package.json").exists():
    print("ERROR: package.json not found.")
    print("Put this Python file inside your zoralpp folder.")
    raise SystemExit(1)

folders = [
    "src/assets",
    "src/components/common",
    "src/components/layout",
    "src/components/ui",
    "src/pages",
    "src/services",
    "src/hooks",
    "src/context",
    "src/types",
    "src/utils",
    "src/styles",
]

files = [
    "src/pages/Login.tsx",
    "src/pages/Login.css",
    "src/pages/Register.tsx",
    "src/pages/Register.css",
    "src/pages/Dashboard.tsx",
    "src/pages/Dashboard.css",
    "src/pages/Workspace.tsx",
    "src/pages/Notes.tsx",
    "src/pages/ChatRoom.tsx",
    "src/pages/AIChat.tsx",
    "src/pages/Settings.tsx",
    "src/pages/Profile.tsx",
    "src/services/api.ts",
    "src/types/index.ts",
    "src/utils/helpers.ts",
]

for folder in folders:
    (ROOT / folder).mkdir(parents=True, exist_ok=True)

for filename in files:
    path = ROOT / filename
    if not path.exists():
        path.touch()
        print("Created:", filename)
    else:
        print("Already exists:", filename)

print("\nZoralpp folder structure created successfully!")
