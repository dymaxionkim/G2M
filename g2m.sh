#!/bin/bash

# pyenv
export PATH="/home/osboxes/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pyenv activate anaconda3-5.3.1
python ./g2m.py
exit 0
