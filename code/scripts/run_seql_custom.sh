#!/bin/bash
cd /home/manuel/src/msc-ucd-2016-ml4music/code/c/seql-sequence-learner


export TRAIN_DIR='/home/manuel/src/msc-ucd-2016-ml4music/data/musicnet/representations/sequence_of_notes/train'
export TEST_DIR='/home/manuel/src/msc-ucd-2016-ml4music/data/musicnet/representations/sequence_of_notes/test'
export MODEL_DIR='/home/manuel/src/msc-ucd-2016-ml4music/data/musicnet/models/sequence_of_notes/seql_custom'
export RESULTS_DIR=$MODEL_DIR'/results'
export SEQL_LEARN='./seql_learn -n 0 -v 2 -g 3 -L 3 -c 0.00005'


$SEQL_LEARN  $TRAIN_DIR/train.A+.txt  $MODEL_DIR/A+.model.txt
./seql_mkmodel -i $MODEL_DIR/A+.model.txt -o $MODEL_DIR/A+.model.bin -O $MODEL_DIR/A+.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.A+.txt $MODEL_DIR/A+.model.bin > $RESULTS_DIR/A+.txt


$SEQL_LEARN $TRAIN_DIR/train.A#+.txt  $MODEL_DIR/A#+.model.txt
./seql_mkmodel -i $MODEL_DIR/A#+.model.txt -o $MODEL_DIR/A#+.model.bin -O $MODEL_DIR/A#+.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.A#+.txt $MODEL_DIR/A#+.model.bin > $RESULTS_DIR/A#+.txt


$SEQL_LEARN $TRAIN_DIR/train.B+.txt  $MODEL_DIR/B+.model.txt
./seql_mkmodel -i $MODEL_DIR/B+.model.txt -o $MODEL_DIR/B+.model.bin -O $MODEL_DIR/B+.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.B+.txt $MODEL_DIR/B+.model.bin > $RESULTS_DIR/B+.txt


$SEQL_LEARN $TRAIN_DIR/train.C+.txt  $MODEL_DIR/C+.model.txt
./seql_mkmodel -i $MODEL_DIR/C+.model.txt -o $MODEL_DIR/C+.model.bin -O $MODEL_DIR/C+.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.C+.txt $MODEL_DIR/C+.model.bin > $RESULTS_DIR/C+.txt


$SEQL_LEARN $TRAIN_DIR/train.C#+.txt  $MODEL_DIR/C#+.model.txt
./seql_mkmodel -i $MODEL_DIR/C#+.model.txt -o $MODEL_DIR/C#+.model.bin -O $MODEL_DIR/C#+.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.C#+.txt $MODEL_DIR/C#+.model.bin > $RESULTS_DIR/C#+.results.txt

$SEQL_LEARN $TRAIN_DIR/train.D+.txt  $MODEL_DIR/D+.model.txt
./seql_mkmodel -i $MODEL_DIR/D+.model.txt -o $MODEL_DIR/D+.model.bin -O $MODEL_DIR/D+.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.D+.txt $MODEL_DIR/D+.model.bin > $RESULTS_DIR/D+.results.txt


$SEQL_LEARN $TRAIN_DIR/train.D#+.txt  $MODEL_DIR/D#+.model.txt
./seql_mkmodel -i $MODEL_DIR/D#+.model.txt -o $MODEL_DIR/D#+.model.bin -O $MODEL_DIR/D#+.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.D#+.txt $MODEL_DIR/D#+.model.bin > $RESULTS_DIR/D#+.results.txt



$SEQL_LEARN $TRAIN_DIR/train.E+.txt  $MODEL_DIR/E+.model.txt
./seql_mkmodel -i $MODEL_DIR/E+.model.txt -o $MODEL_DIR/E+.model.bin -O $MODEL_DIR/E+.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.E+.txt $MODEL_DIR/E+.model.bin > $RESULTS_DIR/E+.results.txt



$SEQL_LEARN $TRAIN_DIR/train.F+.txt  $MODEL_DIR/F+.model.txt
./seql_mkmodel -i $MODEL_DIR/F+.model.txt -o $MODEL_DIR/F+.model.bin -O $MODEL_DIR/F+.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.F+.txt $MODEL_DIR/F+.model.bin > $RESULTS_DIR/F+.results.txt


$SEQL_LEARN $TRAIN_DIR/train.F#+.txt  $MODEL_DIR/F#+.model.txt
./seql_mkmodel -i $MODEL_DIR/F#+.model.txt -o $MODEL_DIR/F#+.model.bin -O $MODEL_DIR/F#+.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.F#+.txt $MODEL_DIR/F#+.model.bin > $RESULTS_DIR/F#+.results.txt


$SEQL_LEARN $TRAIN_DIR/train.G+.txt  $MODEL_DIR/G+.model.txt
./seql_mkmodel -i $MODEL_DIR/G+.model.txt -o $MODEL_DIR/G+.model.bin -O $MODEL_DIR/G+.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.G+.txt $MODEL_DIR/G+.model.bin > $RESULTS_DIR/G+.results.txt


$SEQL_LEARN $TRAIN_DIR/train.G#+.txt  $MODEL_DIR/G#+.model.txt
./seql_mkmodel -i $MODEL_DIR/G#+.model.txt -o $MODEL_DIR/G#+.model.bin -O $MODEL_DIR/G#+.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.G#+.txt $MODEL_DIR/G#+.model.bin > $RESULTS_DIR/G#+.results.txt


$SEQL_LEARN $TRAIN_DIR/train.A-.txt  $MODEL_DIR/A-.model.txt
./seql_mkmodel -i $MODEL_DIR/A-.model.txt -o $MODEL_DIR/A-.model.bin -O $MODEL_DIR/A-.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.A-.txt $MODEL_DIR/A-.model.bin > $RESULTS_DIR/A-.results.txt


$SEQL_LEARN $TRAIN_DIR/train.A#-.txt  $MODEL_DIR/A#-.model.txt
./seql_mkmodel -i $MODEL_DIR/A#-.model.txt -o $MODEL_DIR/A#-.model.bin -O $MODEL_DIR/A#-.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.A#-.txt $MODEL_DIR/A#-.model.bin > $RESULTS_DIR/A#-.results.txt


$SEQL_LEARN $TRAIN_DIR/train.B-.txt  $MODEL_DIR/B-.model.txt
./seql_mkmodel -i $MODEL_DIR/B-.model.txt -o $MODEL_DIR/B-.model.bin -O $MODEL_DIR/B-.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.B-.txt $MODEL_DIR/B-.model.bin > $RESULTS_DIR/B-.results.txt




$SEQL_LEARN $TRAIN_DIR/train.C-.txt  $MODEL_DIR/C-.model.txt
./seql_mkmodel -i $MODEL_DIR/C-.model.txt -o $MODEL_DIR/C-.model.bin -O $MODEL_DIR/C-.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.C-.txt $MODEL_DIR/C-.model.bin > $RESULTS_DIR/C-.results.txt




$SEQL_LEARN $TRAIN_DIR/train.C#-.txt  $MODEL_DIR/C#-.model.txt
./seql_mkmodel -i $MODEL_DIR/C#-.model.txt -o $MODEL_DIR/C#-.model.bin -O $MODEL_DIR/C#-.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.C#-.txt $MODEL_DIR/C#-.model.bin > $RESULTS_DIR/C#-.results.txt



$SEQL_LEARN $TRAIN_DIR/train.D-.txt  $MODEL_DIR/D-.model.txt
./seql_mkmodel -i $MODEL_DIR/D-.model.txt -o $MODEL_DIR/D-.model.bin -O $MODEL_DIR/D-.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.D-.txt $MODEL_DIR/D-.model.bin > $RESULTS_DIR/D-.results.txt



$SEQL_LEARN $TRAIN_DIR/train.D#-.txt  $MODEL_DIR/D#-.model.txt
./seql_mkmodel -i $MODEL_DIR/D#-.model.txt -o $MODEL_DIR/D#-.model.bin -O $MODEL_DIR/D#-.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.D#-.txt $MODEL_DIR/D#-.model.bin > $RESULTS_DIR/D#-.results.txt

$SEQL_LEARN $TRAIN_DIR/train.E-.txt  $MODEL_DIR/E-.model.txt
./seql_mkmodel -i $MODEL_DIR/E-.model.txt -o $MODEL_DIR/E-.model.bin -O $MODEL_DIR/E-.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.E-.txt $MODEL_DIR/E-.model.bin > $RESULTS_DIR/E-.results.txt


$SEQL_LEARN $TRAIN_DIR/train.F-.txt  $MODEL_DIR/F-.model.txt
./seql_mkmodel -i $MODEL_DIR/F-.model.txt -o $MODEL_DIR/F-.model.bin -O $MODEL_DIR/F-.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.F-.txt $MODEL_DIR/F-.model.bin > $RESULTS_DIR/F-.results.txt


$SEQL_LEARN $TRAIN_DIR/train.F#-.txt  $MODEL_DIR/F#-.model.txt
./seql_mkmodel -i $MODEL_DIR/F#-.model.txt -o $MODEL_DIR/F#-.model.bin -O $MODEL_DIR/F#-.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.F#-.txt $MODEL_DIR/F#-.model.bin > $RESULTS_DIR/F#-.results.txt


$SEQL_LEARN $TRAIN_DIR/train.G-.txt  $MODEL_DIR/G-.model.txt
./seql_mkmodel -i $MODEL_DIR/G-.model.txt -o $MODEL_DIR/G-.model.bin -O $MODEL_DIR/G-.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.G-.txt $MODEL_DIR/G-.model.bin > $RESULTS_DIR/G-.results.txt



$SEQL_LEARN $TRAIN_DIR/train.G#-.txt  $MODEL_DIR/G#-.model.txt
./seql_mkmodel -i $MODEL_DIR/G#-.model.txt -o $MODEL_DIR/G#-.model.bin -O $MODEL_DIR/G#-.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.G#-.txt $MODEL_DIR/G#-.model.bin > $RESULTS_DIR/G#-.results.txt


$SEQL_LEARN $TRAIN_DIR/train.G#-.txt  $MODEL_DIR/G#-.model.txt
./seql_mkmodel -i $MODEL_DIR/G#-.model.txt -o $MODEL_DIR/G#-.model.bin -O $MODEL_DIR/G#-.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.G#-.txt $MODEL_DIR/G#-.model.bin > $RESULTS_DIR/G#-.results.txt
