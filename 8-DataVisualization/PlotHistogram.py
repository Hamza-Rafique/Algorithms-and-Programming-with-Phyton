import matplotlib.pyplot as plt


def plot_histogram_with_matplotlib(input_list):
    plt.hist(input_list)
    plt.show()

    return input_list


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    

print(plot_histogram_with_matplotlib(input_list))