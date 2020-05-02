#!/bin/bash

# pyenv
export PATH="/home/osboxes/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
pyenv activate anaconda3-2019.03

# backup
mv ./gantt.csv ./gantt.csv.old
mv ./gantt.html ./gantt.html.old
mv ./gantt.png ./gantt.png.old

# Make gantt.csv
/usr/bin/ganttproject -export csv gantt.gan
sleep 2
echo "Done for gantt.csv"

# Make gantt.png
/usr/bin/ganttproject -export png gantt.gan
sleep 2
echo "Done for gantt.png"

# Make gantt.html
python ./g2m.py
sleep 2
echo "Done for gantt.html"

# Make gantt_mermaid.png
/usr/bin/google-chrome --headless --incognito --disable-gpu --window-size=1600,900 --screenshot=gantt_mermaid.png ./gantt.html
sleep 2
echo "Done for gantt_mermaid.png"

exit 0
