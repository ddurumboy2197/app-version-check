import requests
import os
import sys

def get_latest_version():
    response = requests.get('https://example.com/latest-version')
    return response.text

def check_version(current_version):
    latest_version = get_latest_version()
    if current_version != latest_version:
        return True
    return False

def force_update():
    os.system('pip install --upgrade app-name')

def main():
    current_version = '1.0.0'  # Appning hozirgi versiyasi
    if check_version(current_version):
        print('Yangi versiya mavjud!')
        force_update()
        sys.exit(0)
    print('App versiyasi yangi versiyaga teng.')

if __name__ == '__main__':
    main()
```

```python
# App versiyasi yangi versiyaga teng.
# Yangi versiya mavjud!
# pip install --upgrade app-name
