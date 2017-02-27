#! encoding: UTF-8

import os
import glob
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# example: http://us.data.yt8m.org/1/video_level/train/train--.tfrecord
basic_url = "http://asia.data.yt8m.org/1/video_level/train/"

#train_feats_savepath = "C:\Users\oneflow\Downloads\YouTube_8M\data\video_level\train_feats"
train_feats_savepath = "C:\Users\oneflow\Downloads"
downloaded_names = glob.glob(train_feats_savepath + "\*.tfrecord")

train_names = open("./data_train_names.txt").read().splitlines()

# set chrome driver Options
options = webdriver.ChromeOptions()

# The second setting methods
prefs = {"download.default_directory" : train_feats_savepath}
options.add_experimental_option("prefs", prefs)

# path to chrome driver
chromedriver = "C:\Users\oneflow\Downloads\YouTube_8M\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

for idx, name in enumerate(train_names):
    if name in downloaded_names:
        continue
    else:
        start_time = time.time()
        driver.get(basic_url + name)
        print "{}  {}  Time cost: {}".format(idx, name, time.time()-start_time)
