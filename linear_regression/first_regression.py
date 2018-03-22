import matplotlib.pyplot as plt
import csv


def read_csv(path):
    """ Read from *.csv file and parse the values to floating point numbers """
    with open(path, 'r') as csv_file:
        data = list(csv.reader(csv_file, delimiter=",", quoting=csv.QUOTE_NONNUMERIC))

    return data


def _update_hipotesis(hipotesis, train_data, learning_rate):
    w_0 = hipotesis[0]
    w_1 = hipotesis[1]
    data_length = len(train_data)

    for row in train_data:
        diff_0 = (hipotesis[0] + hipotesis[1] * row[0]) - row[1]
        diff_1 = ((hipotesis[0] + hipotesis[1] * row[0]) - row[1]) * row[0]

        w_0 = w_0 - (2 * learning_rate * diff_0) / data_length
        w_1 = w_1 - (2 * learning_rate * diff_1) / data_length

    return w_0, w_1


def create_hipotesis(initial_hipotesis, train_data, learning_rate, num_iterations):
    hipotesis = initial_hipotesis
    for i in range(0, num_iterations):
        hipotesis = _update_hipotesis(hipotesis, train_data, learning_rate)

    return hipotesis


def calc_error(train_data, hipotesis):
    """ Calculates an error of a hipotesis """
    error = 0.0
    for row in train_data:
        error = error + (row[1] - (hipotesis[0] + hipotesis[1] * row[0])) ** 2

    return error / float(len(train_data))


def plot_graph(hipotesis, train_data, test_data):
    # create lists from 'x' and 'y' coordinates
    x_train, y_train = list(zip(*train_data))
    x_test, y_test = list(zip(*test_data))

    # plot the train ant the test set
    plt.scatter(x_train, y_train, alpha=0.4, s=6, label="train data")
    plt.scatter(x_test, y_test, alpha=0.8, s=6, c="orange", label="test data")

    # plot the hipotesis and other useful information
    plt.plot([0, 100], [hipotesis[0] + hipotesis[1] * 0, hipotesis[0] + hipotesis[1] * 100], color="red",
             label="hipotesis")
    plt.xlabel("X - data")
    plt.ylabel("Y - data")
    plt.legend()

    plt.show()


train_data = read_csv("./res/train.csv")
test_data = read_csv("./res/test.csv")
initial_hipotesis = (0, 0)
learning_rate = 0.0001
num_iterations = 1000

hipotesis = create_hipotesis(initial_hipotesis, train_data, learning_rate, num_iterations)
print("Hipotesis: Y = {}*X + {}, error: {}".format(hipotesis[1], hipotesis[0], calc_error(train_data, hipotesis)))

# test_hipotesis = create_hipotesis(initial_hipotesis, test_data, learning_rate, num_iterations)
# print(test_hipotesis)

print("Train data error: {}".format(calc_error(train_data, hipotesis)))
print("Test data error: {}".format(calc_error(test_data, hipotesis)))

plot_graph(hipotesis, train_data, test_data)