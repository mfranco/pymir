#!/bin/bash
cd /home/manuel/src/msc-ucd-2016-ml4music/code/c/SAX-SEQL/build/Release/bin

export TRAIN_DIR='/home/manuel/src/msc-ucd-2016-ml4music/data/musicnet/representations/time_series/frequency_domain/train'
export TEST_DIR='/home/manuel/src/msc-ucd-2016-ml4music/data/musicnet/representations/time_series/frequency_domain/test'
export RESULTS_DIR='/home/manuel/src/msc-ucd-2016-ml4music/data/musicnet/models/time_series/frequency_domain/sax_seql/results'
export MODEL_DIR='/home/manuel/src/msc-ucd-2016-ml4music/data/musicnet/models/time_series/frequency_domain/sax_seql'
export SAX_CONVERT='./sax_convert -n 0 -s 1 -N 600 -w 16 -a 4  -i'
export SEQL_LEARN='./seql_learn -n 1 -v 1 -A 4 -d 1'
export SEQL_MK_MODEL='./seql_mkmodel -i'
export SEQL_CLASSIFIY='./seql_classify -n 1 -v 0 -p  -d 1'

$SAX_CONVERT $TRAIN_DIR/train.D#-.txt -o $MODEL_DIR/sax.train.D#-.txt -I $TEST_DIR/test.D#-.txt -O $MODEL_DIR/sax.test.D#-.txt
$SAX_CONVERT $TRAIN_DIR/train.E-.txt -o $MODEL_DIR/sax.train.E-.txt -I $TEST_DIR/test.E-.txt -O $MODEL_DIR/sax.test.E-.txt
