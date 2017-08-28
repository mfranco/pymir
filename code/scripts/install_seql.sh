#!/bin/bash

cd /project/code/c
rm -rf /project/code/c/seql-sequence-learner
git clone https://github.com/heerme/seql-sequence-learner.git
cd /project/code/c/seql-sequence-learner
sudo apt-get install libgetopt++-dev -y
make
sudo make all
make test_char
make test_word
