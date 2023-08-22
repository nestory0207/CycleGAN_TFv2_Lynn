import os, logging
import tensorflow as tf

logger = logging.getLogger("CycleGAN")


@tf.function
def minmax_norm(x, epsilon=1e-12):
    x = tf.cast(x, tf.float32)
    min_val = tf.reduce_min(x)
    max_val = tf.reduce_max(x)
    norm_x = (x - min_val) / tf.maximum((max_val - min_val), epsilon)
    return norm_x


@tf.function
def reshape(x, shape):
    x = tf.convert_to_tensor(x)
    shape = [x.shape[i] if shape[i] == 0 else shape[i] for i in range(len(shape))]  # TODO(Lynn): is it slow here?
    shape = [tf.shape(x)[i] if shape[i] is None else shape[i] for i in range(len(shape))]
    return tf.reshape(x, shape)


def make_dir(dir_path):    
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
        logger.info("make directory, path: {}".format(dir_path))