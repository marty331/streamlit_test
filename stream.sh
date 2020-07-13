#!/usr/bin/env bash

set -e
source /home/marty331/PycharmProjects/stream/env/bin/activate
## DO SOME STUFF -> USE FULL PATH HERE TOO #
which python
streamlit run src/main/python/stream_main.py
