#!/bin/bash

# pyenv
export PATH="/home/osboxes/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pyenv activate anaconda3-2020.02
python ./g2m.py

# Linux
google-chrome --headless --incognito --disable-gpu --window-size=1600,900 --screenshot=gantt.png ./gantt.html

exit 0
