import tensorflow as tf

class YUV2RGB_GPU():
    def __init__(self, w=1920, h=1080): 
        config = tf.ConfigProto(gpu_options=tf.GPUOptions(per_process_gpu_memory_fraction=0.03))
        self.y = tf.placeholder(shape=(1, h, w), dtype=tf.float32)
        self.u = tf.placeholder(shape=(1, h, w), dtype=tf.float32) 
        self.v = tf.placeholder(shape=(1, h, w), dtype=tf.float32)
        r = self.y+1.371*(self.v-128)
        g = self.y+0.338* (self.u-128)-0.698*(self.v-128)
        b = self.y+1.732*(self.u-128)
        result = tf.stack([b, g, r], axis=-1)
        self.result = tf.clip_by_value(result, 0, 255)
        self.sess = tf.Session(config=config)

    def convert(self, y, u, v):
        results = self.sess.run(self.result, feed_dict={self.y:y, self.u: u, self.v: v})
        return results.astype(np.uint8)
