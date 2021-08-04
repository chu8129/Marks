import tensorflow

tensorflow.compat.v1.disable_eager_execution()

import datetime
import numpy
import matplotlib.pylab as plt
from functools import reduce

import sys

flag = sys.argv[1]

sys.stdout.write("flag:%s" % flag)
sys.stdout.flush()

copy_times = 1
model_file = "model.ckpt"
_x_data = [0.006, 0.007, 0.008, 0.009, 0.01, 0.011, 0.012, 0.017, 0.01] * 10
x_data = numpy.reshape(_x_data, (len(_x_data), 1))
_y_data = [0.169, 0.133, 0.122, 0.16, 0.147, 0.135, 0.136, 0.198, 0.16] * 10
y_data = numpy.reshape(_y_data, (len(_x_data), 1))

if flag == "train":
    sys.stdout.write("train...")
    sys.stdout.flush()

    x = tensorflow.compat.v1.placeholder(tensorflow.float32, [None, 1], name="x")
    y = tensorflow.compat.v1.placeholder(tensorflow.float32, [None, 1], name="y")

    hidden_size = 20

    Weight_L1 = tensorflow.Variable(
        tensorflow.keras.initializers.RandomNormal(mean=0.0, stddev=1.0)(shape=(1, hidden_size)), name="w"
    )
    biases_L1 = tensorflow.Variable(tensorflow.zeros([1, hidden_size]), name="b")
    to_one_L1 = tensorflow.Variable(tensorflow.zeros([hidden_size, 1]), name="to_one")
    a = tensorflow.Variable(tensorflow.ones([1, 1]), name="a")

    prediction = tensorflow.math.pow(
        tensorflow.math.sigmoid(tensorflow.matmul(tensorflow.matmul(x, Weight_L1) + biases_L1, to_one_L1)),
        a,
        name="restore",
    )

    loss = tensorflow.reduce_mean(tensorflow.square(y - prediction))
    train_step = tensorflow.compat.v1.train.GradientDescentOptimizer(0.001).minimize(loss)

    saver = tensorflow.compat.v1.train.Saver()

    with tensorflow.compat.v1.Session() as sess:
        init = tensorflow.compat.v1.global_variables_initializer()
        sess.run(init)
        ec = 0
        loss_record = [1000, 20000]
        while 1:
            ec += 1
            sess.run(train_step, feed_dict={x: x_data, y: y_data})

            prediction_value = sess.run(prediction, feed_dict={x: x_data})
            loss_val = sum(
                [
                    abs(prediction_value[index][0] - y_data[index][0]) / y_data[index][0]
                    for index in range(len(prediction_value))
                ]
            ) / len(y_data)
            if ec % 1000 == 0:
                print(datetime.datetime.now())
                print("times:%s, loss:%s" % (ec, loss_val))
                if len(loss_record) == 3:
                    del loss_record[0]
                loss_record.append(loss_val)
                saver.save(sess, model_file)
            if loss_val < 0.05 or len(set(loss_record)) == 1:
                break


else:
    with tensorflow.compat.v1.Session() as sess:
        saver = tensorflow.compat.v1.train.import_meta_graph(model_file + ".meta")
        saver.restore(sess, tensorflow.train.latest_checkpoint("./"))
        graph = tensorflow.compat.v1.get_default_graph()
        x = graph.get_tensor_by_name("x:0")
        y = graph.get_tensor_by_name("y:0")
        restore = graph.get_tensor_by_name("restore:0")

        x_test = [index * 1.0 / 10000 for index in range(10000)]
        prediction_value = sess.run(restore, feed_dict={x: numpy.reshape(x_test, (len(x_test), 1))})
        plt.plot(
            x_test,
            prediction_value,
            "r,",
        )
        plt.scatter(
            _x_data + [0],
            _y_data + [0],
        )
        plt.show()
