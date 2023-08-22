import tensorflow as tf


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

def parse_loss_dict(loss_dict):
    for k, v in loss_dict.items():
        if v.shape == tf.shape([1]):
            v = tf.squeeze(v)
        print(f'{k}: {v.numpy():.5f}')