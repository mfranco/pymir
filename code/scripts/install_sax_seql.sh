#!/bin/bash

cd /project/code/c
rm -rf /project/code/c/SAX-SEQL
git clone https://github.com/lnthach/SAX-SEQL.git
cd /project/code/c/SAX-SEQL
sudo apt-get install libgetopt++-dev cmake -y
mkdir -p build
cd build
mkdir -p Release
cd Release
cmake -DCMAKE_BUILD_TYPE=Release ../../
make
cd /tmp
/project/code/c/SAX-SEQL/build/Release/bin/sax_convert -n 0 -s 1 -N 60 -w 16 -a 4  -i   /project/code/c/SAX-SEQL/data/Coffee_TRAIN -o sax.train -I    /project/code/c/SAX-SEQL/data/Coffee_TEST -O sax.test
/project/code/c/SAX-SEQL/build/Release/bin/seql_learn -n 1 -v 1 -A 4 -d 1 sax.train seql.model
/project/code/c/SAX-SEQL/build/Release/bin/seql_mkmodel -i seql.model -o seql.model.bin -O seql.predictor
/project/code/c/SAX-SEQL/build/Release/bin/seql_classify -n 1 -v 0 -p seql.predictor -d 1 sax.test seql.model.bin
