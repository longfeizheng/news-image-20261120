#!/bin/sh
# Render src/frontpage.html to entry.png at exactly 1024x1024.
# Uses the Playwright Chromium build cached on the build machine; any
# headless Chromium with --screenshot and --window-size works the same.
set -eu
cd "$(dirname "$0")/.."
CHROME="${CHROME:-$HOME/.cache/ms-playwright/chromium-1223/chrome-linux64/chrome}"
"$CHROME" --headless=new --no-sandbox --disable-gpu --hide-scrollbars \
  --window-size=1024,1024 \
  --screenshot="$PWD/entry.png" \
  "file://$PWD/src/frontpage.html"
python3 -c "
from PIL import Image
im = Image.open('entry.png')
assert im.size == (1024, 1024), im.size
print('entry.png', im.size, 'ok')
"
