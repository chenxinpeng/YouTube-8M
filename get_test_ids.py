#! encoding:UTF-8

import os
import glob
import tensorflow as tf

test_tfrecord_path = "../data/video_level/test_feats"
test_filenames = glob.glob(test_tfrecord_path + "/test*.tfrecord")

file_test_ids = open("test_ids.txt", "w")
file_test_urls = open("test_urls.txt", "w")
for tmp_idx, each_test_filenames in enumerate(test_filenames):
    print "{}  {}".format(tmp_idx, each_test_filenames)
    for serialized_example in tf.python_io.tf_record_iterator(each_test_filenames):
        example = tf.train.Example.FromString(serialized_example)

        # video_id
        tmp_IDs = example.features.feature["video_id"]
        file_test_ids.write(tmp_IDs.bytes_list.value[0] + "\n")
        file_test_urls.write("https://youtube.com/watch?v=" + tmp_IDs.bytes_list.value[0] + "\n")

file_test_ids.close()
file_test_urls.close()
