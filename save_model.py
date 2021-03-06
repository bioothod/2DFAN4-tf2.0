#!/usr/bin/python3

import os;
import numpy as np;
import tensorflow as tf;
from Model import _2DFAN4;

if __name__ == "__main__":
    
    model = _2DFAN4([256,256,3]);
    optimizer = tf.keras.optimizers.Adam(1e-4);
    checkpoint = tf.train.Checkpoint(model = model, optimizer = optimizer, optimizer_step = optimizer.iterations);
    checkpoint.restore(tf.train.latest_checkpoint('checkpoints_2DFAN4'));
    if False == os.path.exists('models'): os.mkdir('models');
    model.save(os.path.join('models','model.h5'));

