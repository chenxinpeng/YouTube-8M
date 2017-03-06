#! encoding:UTF-8

import os
import glob
import tensorflow as tf

#import ipdb

train_tfrecord_path = "../data/video_level/train_feats"
train_filenames = glob.glob(train_tfrecord_path + "/train*.tfrecord")

file_train_ids = open("train_ids.txt", "w")
file_train_urls = open("train_urls.txt", "w")
for tmp_idx, each_train_filenames in enumerate(train_filenames):
    print "{}  {}".format(tmp_idx, each_train_filenames)
    for serialized_example in tf.python_io.tf_record_iterator(each_train_filenames):
        example = tf.train.Example.FromString(serialized_example)

        # video_id
        tmp_IDs = example.features.feature["video_id"]
        file_train_ids.write(tmp_IDs.bytes_list.value[0] + "\n")
        file_train_urls.write("https://youtube.com/watch?v=" + tmp_IDs.bytes_list.value[0] + "\n")
file_train_ids.close()
file_train_urls.close()
