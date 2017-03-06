#! encoding:UTF-8

import os
import glob
import tensorflow as tf

import ipdb

train_tfrecord_path = "../data/video_level/train_feats"
val_tfrecord_path = "../data/video_level/val_feats"
test_tfrecord_path = "../data/video_level/test_feats"

train_filenames = glob.glob(train_tfrecord_path + "/train*.tfrecord")
val_filenames = glob.glob(val_tfrecord_path + "/validate*.tfrecord")
test_filenames = glob.glob(test_tfrecord_path + "/test*.tfrecord")

file_val_ids = open("val_ids.txt", "w")
file_val_urls = open("val_urls.txt", "w")
for tmp_idx, each_val_filenames in enumerate(val_filenames):
    print "{}  {}".format(tmp_idx, each_val_filenames)
    for serialized_example in tf.python_io.tf_record_iterator(each_val_filenames):
        example = tf.train.Example.FromString(serialized_example)

        # video_id
        tmp_IDs = example.features.feature["video_id"]
        file_val_ids.write(tmp_IDs.bytes_list.value[0] + "\n")
        file_val_urls.write("https://youtube.com/watch?v=" + tmp_IDs.bytes_list.value[0] + "\n")


file_val_ids.close()
file_val_urls.close()
