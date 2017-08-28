#!/bin/bash
#cd /project/code/c/SAX-SEQL/build/Release/bin
cd /home/ubuntu/seql/sax
#export TRAIN_DIR='/project/data/musicnet/representations/time_series/frequency_domain/train'
#export TEST_DIR='/project/data/musicnet/representations/time_series/frequency_domain/test'
#export RESULTS_DIR='/project/data/musicnet/models/time_series/frequency_domain/sax_seql/results'
#export MODEL_DIR='/project/data/musicnet/models/time_series/frequency_domain/sax_seql'
#export SAX_CONVERT='./sax_convert -n 0 -s 1 -N 600 -w 16 -a 4  -i'
#export SEQL_LEARN='./seql_learn -n 1 -v 1 -A 4 -d 1'
#export SEQL_MK_MODEL='./seql_mkmodel -i'
#export SEQL_CLASSIFIY='./seql_classify -n 1 -v 1 -p '

export TRAIN_DIR='/src/msc-ucd-2016-ml4music/data/musicnet/representations/time_series/frequency_domain/train'
export TEST_DIR='/src/msc-ucd-2016-ml4music/data/musicnet/representations/time_series/frequency_domain/test'
export RESULTS_DIR='/src/msc-ucd-2016-ml4music/data/musicnet/models/time_series/frequency_domain/sax_seql/results'
export MODEL_DIR='/src/msc-ucd-2016-ml4music/data/musicnet/models/time_series/frequency_domain/sax_seql'


export SAX_CONVERT='./sax_convert -n 0 -s 1 -N 60 -w 16 -a 4  -i'
export SEQL_LEARN='./seql_learn -n 1  -v 2 -A 4 -d 1'
export SEQL_MK_MODEL='./seql_mkmodel -i'
export SEQL_CLASSIFIY='./seql_classify -n 1 -v 1 -p '

#$SAX_CONVERT $TRAIN_DIR/train.A+.txt -o $MODEL_DIR/sax.train.A+.txt -I $TEST_DIR/test.A+.txt -O $MODEL_DIR/sax.test.A+.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.A+.txt  $MODEL_DIR/seql.model.A+
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.A+ -o $MODEL_DIR/seql.model.bin.A+ -O $MODEL_DIR/seql.model.predictor.A+
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.A+ $MODEL_DIR/sax.test.A+.txt $MODEL_DIR/seql.model.bin.A+ > $RESULTS_DIR/results.A+



#$SAX_CONVERT $TRAIN_DIR/train.A#+.txt -o $MODEL_DIR/sax.train.A#+.txt -I $TEST_DIR/test.A#+.txt -O $MODEL_DIR/sax.test.A#+.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.A#+.txt  $MODEL_DIR/seql.model.A#+
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.A#+ -o $MODEL_DIR/seql.model.bin.A#+ -O $MODEL_DIR/seql.model.predictor.A#+
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.A#+ $MODEL_DIR/sax.test.A#+.txt $MODEL_DIR/seql.model.bin.A#+ > $RESULTS_DIR/results.A#+




#$SAX_CONVERT $TRAIN_DIR/train.B+.txt -o $MODEL_DIR/sax.train.B+.txt -I $TEST_DIR/test.B+.txt -O $MODEL_DIR/sax.test.B+.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.B+.txt  $MODEL_DIR/seql.model.B+
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.B+ -o $MODEL_DIR/seql.model.bin.B+ -O $MODEL_DIR/seql.model.predictor.B+
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.B+ $MODEL_DIR/sax.test.B+.txt $MODEL_DIR/seql.model.bin.B+ > $RESULTS_DIR/results.B+




#$SAX_CONVERT $TRAIN_DIR/train.C+.txt -o $MODEL_DIR/sax.train.C+.txt -I $TEST_DIR/test.C+.txt -O $MODEL_DIR/sax.test.C+.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.C+.txt  $MODEL_DIR/seql.model.C+
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.C+ -o $MODEL_DIR/seql.model.bin.C+ -O $MODEL_DIR/seql.model.predictor.C+
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.C+ $MODEL_DIR/sax.test.C+.txt $MODEL_DIR/seql.model.bin.C+ > $RESULTS_DIR/results.C+



#$SAX_CONVERT $TRAIN_DIR/train.C#+.txt -o $MODEL_DIR/sax.train.C#+.txt -I $TEST_DIR/test.C#+.txt -O $MODEL_DIR/sax.test.C#+.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.C#+.txt  $MODEL_DIR/seql.model.C#+
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.C#+ -o $MODEL_DIR/seql.model.bin.C#+ -O $MODEL_DIR/seql.model.predictor.C#+
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.C#+ $MODEL_DIR/sax.test.C#+.txt $MODEL_DIR/seql.model.bin.C#+ > $RESULTS_DIR/results.C#+





#$SAX_CONVERT $TRAIN_DIR/train.D+.txt -o $MODEL_DIR/sax.train.D+.txt -I $TEST_DIR/test.D+.txt -O $MODEL_DIR/sax.test.D+.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.D+.txt  $MODEL_DIR/seql.model.D+
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.D+ -o $MODEL_DIR/seql.model.bin.D+ -O $MODEL_DIR/seql.model.predictor.D+
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.D+ $MODEL_DIR/sax.test.D+.txt $MODEL_DIR/seql.model.bin.D+ > $RESULTS_DIR/results.D+



#$SAX_CONVERT $TRAIN_DIR/train.D#+.txt -o $MODEL_DIR/sax.train.D#+.txt -I $TEST_DIR/test.D#+.txt -O $MODEL_DIR/sax.test.D#+.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.D#+.txt  $MODEL_DIR/seql.model.D#+
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.D#+ -o $MODEL_DIR/seql.model.bin.D#+ -O $MODEL_DIR/seql.model.predictor.D#+
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.D#+ $MODEL_DIR/sax.test.D#+.txt $MODEL_DIR/seql.model.bin.D#+ > $RESULTS_DIR/results.D#+




#$SAX_CONVERT $TRAIN_DIR/train.E+.txt -o $MODEL_DIR/sax.train.E+.txt -I $TEST_DIR/test.E+.txt -O $MODEL_DIR/sax.test.E+.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.E+.txt  $MODEL_DIR/seql.model.E+
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.E+ -o $MODEL_DIR/seql.model.bin.E+ -O $MODEL_DIR/seql.model.predictor.E+
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.E+  $MODEL_DIR/sax.test.E+.txt $MODEL_DIR/seql.model.bin.E+ > $RESULTS_DIR/results.E+


#$SAX_CONVERT $TRAIN_DIR/train.F+.txt -o $MODEL_DIR/sax.train.F+.txt -I $TEST_DIR/test.F+.txt -O $MODEL_DIR/sax.test.F+.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.F+.txt  $MODEL_DIR/seql.model.F+
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.F+ -o $MODEL_DIR/seql.model.bin.F+ -O $MODEL_DIR/seql.model.predictor.F+
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.F+ $MODEL_DIR/sax.test.F+.txt $MODEL_DIR/seql.model.bin.F+ > $RESULTS_DIR/results.F+



#$SAX_CONVERT $TRAIN_DIR/train.F#+.txt -o $MODEL_DIR/sax.train.F#+.txt -I $TEST_DIR/test.F#+.txt -O $MODEL_DIR/sax.test.F#+.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.F#+.txt  $MODEL_DIR/seql.model.F#+
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.F#+ -o $MODEL_DIR/seql.model.bin.F#+ -O $MODEL_DIR/seql.model.predictor.F#+
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.F#+ $MODEL_DIR/sax.test.F#+.txt $MODEL_DIR/seql.model.bin.F#+ > $RESULTS_DIR/results.F#+




#$SAX_CONVERT $TRAIN_DIR/train.G+.txt -o $MODEL_DIR/sax.train.G+.txt -I $TEST_DIR/test.G+.txt -O $MODEL_DIR/sax.test.G+.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.G+.txt  $MODEL_DIR/seql.model.G+
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.G+ -o $MODEL_DIR/seql.model.bin.G+ -O $MODEL_DIR/seql.model.predictor.G+
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.G+ $MODEL_DIR/sax.test.G+.txt $MODEL_DIR/seql.model.bin.G+ > $RESULTS_DIR/results.G+



#$SAX_CONVERT $TRAIN_DIR/train.G#+.txt -o $MODEL_DIR/sax.train.G#+.txt -I $TEST_DIR/test.G#+.txt -O $MODEL_DIR/sax.test.G#+.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.G#+.txt  $MODEL_DIR/seql.model.G#+
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.G#+ -o $MODEL_DIR/seql.model.bin.G#+ -O $MODEL_DIR/seql.model.predictor.G#+
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.G#+ $MODEL_DIR/sax.test.G#+.txt $MODEL_DIR/seql.model.bin.G#+ > $RESULTS_DIR/results.G#+


#$SAX_CONVERT $TRAIN_DIR/train.A-.txt -o $MODEL_DIR/sax.train.A-.txt -I $TEST_DIR/test.A-.txt -O $MODEL_DIR/sax.test.A-.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.A-.txt  $MODEL_DIR/seql.model.A-
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.A- -o $MODEL_DIR/seql.model.bin.A- -O $MODEL_DIR/seql.model.predictor.A-
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.A- $MODEL_DIR/sax.test.A-.txt $MODEL_DIR/seql.model.bin.A- > $RESULTS_DIR/results.A-



#$SAX_CONVERT $TRAIN_DIR/train.A#-.txt -o $MODEL_DIR/sax.train.A#-.txt -I $TEST_DIR/test.A#-.txt -O $MODEL_DIR/sax.test.A#-.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.A#-.txt  $MODEL_DIR/seql.model.A#-
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.A#- -o $MODEL_DIR/seql.model.bin.A#- -O $MODEL_DIR/seql.model.predictor.A#-
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.A#- $MODEL_DIR/sax.test.A#-.txt $MODEL_DIR/seql.model.bin.A#- > $RESULTS_DIR/results.A#-



#$SAX_CONVERT $TRAIN_DIR/train.B-.txt -o $MODEL_DIR/sax.train.B-.txt -I $TEST_DIR/test.B-.txt -O $MODEL_DIR/sax.test.B-.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.B-.txt  $MODEL_DIR/seql.model.B-
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.B- -o $MODEL_DIR/seql.model.bin.B- -O $MODEL_DIR/seql.model.predictor.B-
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.B- $MODEL_DIR/sax.test.B-.txt $MODEL_DIR/seql.model.bin.B- > $RESULTS_DIR/results.B-



#$SAX_CONVERT $TRAIN_DIR/train.C-.txt -o $MODEL_DIR/sax.train.C-.txt -I $TEST_DIR/test.C-.txt -O $MODEL_DIR/sax.test.C-.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.C-.txt  $MODEL_DIR/seql.model.C-
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.C- -o $MODEL_DIR/seql.model.bin.C- -O $MODEL_DIR/seql.model.predictor.C-
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.C- $MODEL_DIR/sax.test.C-.txt $MODEL_DIR/seql.model.bin.C- > $RESULTS_DIR/results.C-



#$SAX_CONVERT $TRAIN_DIR/train.C#-.txt -o $MODEL_DIR/sax.train.C#-.txt -I $TEST_DIR/test.C#-.txt -O $MODEL_DIR/sax.test.C#-.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.C#-.txt  $MODEL_DIR/seql.model.C#-
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.C#- -o $MODEL_DIR/seql.model.bin.C#- -O $MODEL_DIR/seql.model.predictor.C#-
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.C#- $MODEL_DIR/sax.test.C#-.txt $MODEL_DIR/seql.model.bin.C#- > $RESULTS_DIR/results.C#-


#$SAX_CONVERT $TRAIN_DIR/train.D-.txt -o $MODEL_DIR/sax.train.D-.txt -I $TEST_DIR/test.D-.txt -O $MODEL_DIR/sax.test.D-.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.D-.txt  $MODEL_DIR/seql.model.D-
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.D- -o $MODEL_DIR/seql.model.bin.D- -O $MODEL_DIR/seql.model.predictor.D-
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.D- $MODEL_DIR/sax.test.D-.txt $MODEL_DIR/seql.model.bin.D- > $RESULTS_DIR/results.D-




#$SAX_CONVERT $TRAIN_DIR/train.D#-.txt -o $MODEL_DIR/sax.train.D#-.txt -I $TEST_DIR/test.D#-.txt -O $MODEL_DIR/sax.test.D#-.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.D#-.txt  $MODEL_DIR/seql.model.D#-
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.D#- -o $MODEL_DIR/seql.model.bin.D#- -O $MODEL_DIR/seql.model.predictor.D#-
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.D#- $MODEL_DIR/sax.test.D#-.txt $MODEL_DIR/seql.model.bin.D#- > $RESULTS_DIR/results.D#-



#$SAX_CONVERT $TRAIN_DIR/train.E-.txt -o $MODEL_DIR/sax.train.E-.txt -I $TEST_DIR/test.E-.txt -O $MODEL_DIR/sax.test.E-.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.E-.txt  $MODEL_DIR/seql.model.E-
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.E- -o $MODEL_DIR/seql.model.bin.E- -O $MODEL_DIR/seql.model.predictor.E-
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.E- $MODEL_DIR/sax.test.E-.txt $MODEL_DIR/seql.model.bin.E- > $RESULTS_DIR/results.E-



#$SAX_CONVERT $TRAIN_DIR/train.F-.txt -o $MODEL_DIR/sax.train.F-.txt -I $TEST_DIR/test.F-.txt -O $MODEL_DIR/sax.test.F-.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.F-.txt  $MODEL_DIR/seql.model.F-
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.F- -o $MODEL_DIR/seql.model.bin.F- -O $MODEL_DIR/seql.model.predictor.F-
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.F- $MODEL_DIR/sax.test.F-.txt $MODEL_DIR/seql.model.bin.F- > $RESULTS_DIR/results.F-



#$SAX_CONVERT $TRAIN_DIR/train.F#-.txt -o $MODEL_DIR/sax.train.F#-.txt -I $TEST_DIR/test.F#-.txt -O $MODEL_DIR/sax.test.F#-.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.F#-.txt  $MODEL_DIR/seql.model.F#-
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.F#- -o $MODEL_DIR/seql.model.bin.F#- -O $MODEL_DIR/seql.model.predictor.F#-
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.F#- $MODEL_DIR/sax.test.F#-.txt $MODEL_DIR/seql.model.bin.F#- > $RESULTS_DIR/results.F#-



#$SAX_CONVERT $TRAIN_DIR/train.G-.txt -o $MODEL_DIR/sax.train.G-.txt -I $TEST_DIR/test.G-.txt -O $MODEL_DIR/sax.test.G-.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.G-.txt  $MODEL_DIR/seql.model.G-
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.G- -o $MODEL_DIR/seql.model.bin.G- -O $MODEL_DIR/seql.model.predictor.G-
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.G- $MODEL_DIR/sax.test.G-.txt $MODEL_DIR/seql.model.bin.G- > $RESULTS_DIR/results.G-



#$SAX_CONVERT $TRAIN_DIR/train.G#-.txt -o $MODEL_DIR/sax.train.G#-.txt -I $TEST_DIR/test.G#-.txt -O $MODEL_DIR/sax.test.G#-.txt
#$SEQL_LEARN $MODEL_DIR/sax.train.G#-.txt  $MODEL_DIR/seql.model.G#-
#$SEQL_MK_MODEL  $MODEL_DIR/seql.model.G#- -o $MODEL_DIR/seql.model.bin.G#- -O $MODEL_DIR/seql.model.predictor.G#-
$SEQL_CLASSIFIY $MODEL_DIR/seql.model.predictor.G#- $MODEL_DIR/sax.test.G#-.txt $MODEL_DIR/seql.model.bin.G#- > $RESULTS_DIR/results.G#-













#./sax_convert -n 0 -s 1 -N 60 -w 16 -a 4  -i /project/data/musicnet/representations/time_series/time_domain/train/train.A+.txt -o sax.train -I /project/data/musicnet/representations/time_series/time_domain/test/test.A+.txt -O sax.test
#./seql_learn -n 1 -v 1 -A 4 -d 1 sax.train seql.model
#./seql_mkmodel -i seql.model -o seql.model.bin -O seql.predictor
#./seql_classify -n 1 -v 0 -p seql.predictor -d 1 sax.test seql.model.bin
