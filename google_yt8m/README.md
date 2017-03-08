
## Introduction

This folder saves the code from [Google YouTube-8M starter code](https://github.com/google/youtube-8m/).

And at the same time, I use this README.md to record some operations when I use the code.

## Operation records
### LogisticModel
Training with LogisticModel:
```bash
$ CUDA_VISIBLE_DEVICES=0 python train.py --train_data_pattern="../data/video_level/train_feats/train*.tfrecord" --train_dir=./models/video_level_mymodel_1 --feature_names="mean_rgb, mean_audio" --feature_sizes="1024, 128" --model=MyModel_1
```

### MoeModel
Training with MoeModel:
```bash
$ CUDA_VISIBLE_DEVICES=0 python train.py --train_data_pattern="../data/video_level/train_feats/train*.tfrecord" --train_dir=./models/video_level_moe --feature_names="mean_rgb, mean_audio" --feature_sizes="1024, 128" --model=MoeModel
```

Evaluation on MoeModel:
```bash
$ CUDA_VISIBLE_DEVICES=1 python eval.py --train_dir=./models/video_level_moe --feature_names="mean_rgb, mean_audio" --feature_sizes="1024,128" --model=MoeModel --run_once=True --eval_data_pattern="../data/video_level/val_feats/validate*.tfrecord"
```

Inference on MoeModel:
```bash
$ CUDA_VISIBLE_DEVICES=1 python inference.py --output_file=./models/video_level_moe/predictions.csv --input_data_pattern='../data/video_level/test_feats/test*.tfrecord' --train_dir=./models/video_level_moe --feature_names="mean_rgb, mean_audio" --feature_sizes="1024, 128"
```
