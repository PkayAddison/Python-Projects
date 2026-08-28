import subprocess
import re

output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'],
                                 text=True, 
                                 encoding='utf-8', 
                                 errors='ignore'
)

profiles = re.findall(r'All User Profile\s*:\s*(.*)', output)

for profile in profiles:
    profile = profile.strip()
    try:
        details = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'],
            text=True,
            encoding='utf-8',
            errors='ignore'
        )
        password_match = re.search(r'Key Content\s*:\s*(.*)', details)
        password = password_match.group(1).strip() if password_match else "No password found"
    except subprocess.CalledProcessError:
        password = "Could not retrieve (Access Denied or Special Profile)"
        
    print(f"Wifi: {profile}")
    print(f"Password: {password}")
    print("-" * 30)

input("\nPress Enter to close...")