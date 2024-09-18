import matplotlib.pyplot as plt

def plot_line_chart_with_matplotlib(input_list):
    plt.plot(input_list)
    plt.show()

    return input_list


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(plot_line_chart_with_matplotlib(input_list))