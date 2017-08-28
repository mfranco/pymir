#!/bin/bash
cd /home/ubuntu/seql/seql

export TRAIN_DIR='/src/msc-ucd-2016-ml4music/data/musicnet/representations/sequence_of_notes/train'
export TEST_DIR='/src/msc-ucd-2016-ml4music/data/musicnet/representations/sequence_of_notes/test'
export RESULTS_DIR='/src/msc-ucd-2016-ml4music/data/musicnet/models/sequence_of_notes/seql/results'
export MODEL_DIR='/src/msc-ucd-2016-ml4music/data/musicnet/models/sequence_of_notes/seql'

./seql_learn -n 0 -v 2 /project/data/musicnet/representations/sequence_of_notes/train/train.A+.txt  /project/data/musicnet/models/sequence_of_notes/seql/A+.model.txt
./seql_mkmodel -i /project/data/musicnet/models/sequence_of_notes/seql/A+.model.txt -o /project/data/musicnet/models/sequence_of_notes/seql/A+.model.bin -O /project/data/musicnet/models/sequence_of_notes/seql/A+.model.predictors
./seql_classify -n 0 -v 2 /project/data/musicnet/representations/sequence_of_notes/test/test.A+.txt /project/data/musicnet/models/sequence_of_notes/seql/A+.model.bin > /project/data/musicnet/models/sequence_of_notes/seql/results/A+.txt


./seql_learn -n 0 -v 2 /project/data/musicnet/representations/sequence_of_notes/train/train.A#+.txt  /project/data/musicnet/models/sequence_of_notes/seql/A#+.model.txt
./seql_mkmodel -i /project/data/musicnet/models/sequence_of_notes/seql/A#+.model.txt -o /project/data/musicnet/models/sequence_of_notes/seql/A#+.model.bin -O /project/data/musicnet/models/sequence_of_notes/seql/A#+.model.predictors
./seql_classify -n 0 -v 2 /project/data/musicnet/representations/sequence_of_notes/test/test.A#+.txt /project/data/musicnet/models/sequence_of_notes/seql/A#+.model.bin > /project/data/musicnet/models/sequence_of_notes/seql/results/A#+.txt


./seql_learn -n 0 -v 2 /project/data/musicnet/representations/sequence_of_notes/train/train.B+.txt  /project/data/musicnet/models/sequence_of_notes/seql/B+.model.txt
./seql_mkmodel -i /project/data/musicnet/models/sequence_of_notes/seql/B+.model.txt -o /project/data/musicnet/models/sequence_of_notes/seql/B+.model.bin -O /project/data/musicnet/models/sequence_of_notes/seql/B+.model.predictors
./seql_classify -n 0 -v 2 /project/data/musicnet/representations/sequence_of_notes/test/test.B+.txt /project/data/musicnet/models/sequence_of_notes/seql/B+.model.bin > /project/data/musicnet/models/sequence_of_notes/seql/results/B+.txt


./seql_learn -n 0 -v 2 /project/data/musicnet/representations/sequence_of_notes/train/train.C+.txt  /project/data/musicnet/models/sequence_of_notes/seql/C+.model.txt
./seql_mkmodel -i /project/data/musicnet/models/sequence_of_notes/seql/C+.model.txt -o /project/data/musicnet/models/sequence_of_notes/seql/C+.model.bin -O /project/data/musicnet/models/sequence_of_notes/seql/C+.predictors
./seql_classify -n 0 -v 2 /project/data/musicnet/representations/sequence_of_notes/test/test.C+.txt /project/data/musicnet/models/sequence_of_notes/seql/C+.model.bin > /project/data/musicnet/models/sequence_of_notes/seql/results/C+.txt


./seql_learn -n 0 -v 2 $TRAIN_DIR/train.C#+.txt  $MODEL_DIR/C#+.model.txt
./seql_mkmodel -i $MODEL_DIR/C#+.model.txt -o $MODEL_DIR/C#+.model.bin -O $MODEL_DIR/C#+.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.C#+.txt $MODEL_DIR/C#+.model.bin > $RESULTS_DIR/C#+.results.txt

./seql_learn -n 0 -v 2 $TRAIN_DIR/train.D+.txt  $MODEL_DIR/D+.model.txt
./seql_mkmodel -i $MODEL_DIR/D+.model.txt -o $MODEL_DIR/D+.model.bin -O $MODEL_DIR/D+.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.D+.txt $MODEL_DIR/D+.model.bin > $RESULTS_DIR/D+.results.txt


./seql_learn -n 0 -v 2 $TRAIN_DIR/train.D#+.txt  $MODEL_DIR/D#+.model.txt
./seql_mkmodel -i $MODEL_DIR/D#+.model.txt -o $MODEL_DIR/D#+.model.bin -O $MODEL_DIR/D#+.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.D#+.txt $MODEL_DIR/D#+.model.bin > $RESULTS_DIR/D#+.results.txt



./seql_learn -n 0 -v 2 $TRAIN_DIR/train.E+.txt  $MODEL_DIR/E+.model.txt
./seql_mkmodel -i $MODEL_DIR/E+.model.txt -o $MODEL_DIR/E+.model.bin -O $MODEL_DIR/E+.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.E+.txt $MODEL_DIR/E+.model.bin > $RESULTS_DIR/E+.results.txt



./seql_learn -n 0 -v 2 $TRAIN_DIR/train.F+.txt  $MODEL_DIR/F+.model.txt
./seql_mkmodel -i $MODEL_DIR/F+.model.txt -o $MODEL_DIR/F+.model.bin -O $MODEL_DIR/F+.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.F+.txt $MODEL_DIR/F+.model.bin > $RESULTS_DIR/F+.results.txt


./seql_learn -n 0 -v 2 $TRAIN_DIR/train.F#+.txt  $MODEL_DIR/F#+.model.txt
./seql_mkmodel -i $MODEL_DIR/F#+.model.txt -o $MODEL_DIR/F#+.model.bin -O $MODEL_DIR/F#+.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.F#+.txt $MODEL_DIR/F#+.model.bin > $RESULTS_DIR/F#+.results.txt


./seql_learn -n 0 -v 2 $TRAIN_DIR/train.G+.txt  $MODEL_DIR/G+.model.txt
./seql_mkmodel -i $MODEL_DIR/G+.model.txt -o $MODEL_DIR/G+.model.bin -O $MODEL_DIR/G+.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.G+.txt $MODEL_DIR/G+.model.bin > $RESULTS_DIR/G+.results.txt


./seql_learn -n 0 -v 2 $TRAIN_DIR/train.G#+.txt  $MODEL_DIR/G#+.model.txt
./seql_mkmodel -i $MODEL_DIR/G#+.model.txt -o $MODEL_DIR/G#+.model.bin -O $MODEL_DIR/G#+.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.G#+.txt $MODEL_DIR/G#+.model.bin > $RESULTS_DIR/G#+.results.txt


./seql_learn -n 0 -v 2 $TRAIN_DIR/train.A-.txt  $MODEL_DIR/A-.model.txt
./seql_mkmodel -i $MODEL_DIR/A-.model.txt -o $MODEL_DIR/A-.model.bin -O $MODEL_DIR/A-.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.A-.txt $MODEL_DIR/A-.model.bin > $RESULTS_DIR/A-.results.txt


./seql_learn -n 0 -v 2 $TRAIN_DIR/train.A#-.txt  $MODEL_DIR/A#-.model.txt
./seql_mkmodel -i $MODEL_DIR/A#-.model.txt -o $MODEL_DIR/A#-.model.bin -O $MODEL_DIR/A#-.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.A#-.txt $MODEL_DIR/A#-.model.bin > $RESULTS_DIR/A#-.results.txt


./seql_learn -n 0 -v 2 $TRAIN_DIR/train.B-.txt  $MODEL_DIR/B-.model.txt
./seql_mkmodel -i $MODEL_DIR/B-.model.txt -o $MODEL_DIR/B-.model.bin -O $MODEL_DIR/B-.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.B-.txt $MODEL_DIR/B-.model.bin > $RESULTS_DIR/B-.results.txt




./seql_learn -n 0 -v 2 $TRAIN_DIR/train.C-.txt  $MODEL_DIR/C-.model.txt
./seql_mkmodel -i $MODEL_DIR/C-.model.txt -o $MODEL_DIR/C-.model.bin -O $MODEL_DIR/C-.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.C-.txt $MODEL_DIR/C-.model.bin > $RESULTS_DIR/C-.results.txt




./seql_learn -n 0 -v 2 $TRAIN_DIR/train.C#-.txt  $MODEL_DIR/C#-.model.txt
./seql_mkmodel -i $MODEL_DIR/C#-.model.txt -o $MODEL_DIR/C#-.model.bin -O $MODEL_DIR/C#-.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.C#-.txt $MODEL_DIR/C#-.model.bin > $RESULTS_DIR/C#-.results.txt



./seql_learn -n 0 -v 2 $TRAIN_DIR/train.D-.txt  $MODEL_DIR/D-.model.txt
./seql_mkmodel -i $MODEL_DIR/D-.model.txt -o $MODEL_DIR/D-.model.bin -O $MODEL_DIR/D-.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.D-.txt $MODEL_DIR/D-.model.bin > $RESULTS_DIR/D-.results.txt



./seql_learn -n 0 -v 2 $TRAIN_DIR/train.D#-.txt  $MODEL_DIR/D#-.model.txt
./seql_mkmodel -i $MODEL_DIR/D#-.model.txt -o $MODEL_DIR/D#-.model.bin -O $MODEL_DIR/D#-.model.predictors
./seql_classify -n 0 -v 2 $TEST_DIR/test.D#-.txt $MODEL_DIR/D#-.model.bin > $RESULTS_DIR/D#-.results.txt
