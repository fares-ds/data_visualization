from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")


days = [1, 2, 3, 4, 5, 6, 7, 8, 9]

employee_1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
employee_2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
employee_3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ['employee_1', 'employee_2', 'employee_3']
colors = ['#6d904f', '#fc4f30', '#008fd5']

plt.stackplot(days, employee_1, employee_2, employee_3, colors=colors, labels=labels)
plt.legend(loc=(0.07, 0.05), fontsize='xx-small', shadow=True)

plt.title("My Awesome Stack Plot")
plt.tight_layout()
plt.savefig('matplotlib_p_4_stack_plots.png')
plt.show()
