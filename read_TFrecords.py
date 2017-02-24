#! encoding: UTF-8

#import os
import glob
import tensorflow as tf

file_names = glob.glob("./*.tfrecord")

video_ids = []
video_labels = []
video_mean_RGB = []
video_mean_AUDIO = []
for serialized_example in tf.python_io.tf_record_iterator(file_names[0]):
    example = tf.train.Example()
    example.ParseFromString(serialized_example)

    # video_id
    tmp_IDs = example.features.feature["video_id"]
    #for each_video_id in tmp_IDs.bytes_list.value:
    #    video_ids.append(each_video_id)
    video_ids.append(tmp_IDs.bytes_list.value[0])

    # labels
    tmp_Labels = example.features.feature["labels"]
    video_labels.append(tmp_Labels.int64_list.value)

    # mean_rgb
    tmp_mean_RGB = example.features.feature["mean_rgb"]
    video_mean_RGB.append(tmp_mean_RGB.float_list.value)

    # mean_audio
    tmp_mean_AUDIO = example.features.feature["mean_audio"]
    video_mean_AUDIO.append(tmp_mean_AUDIO.float_list)


print len(video_ids)
print len(video_labels)
print len(video_mean_RGB)
print len(video_mean_AUDIO)

