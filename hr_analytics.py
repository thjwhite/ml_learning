import pandas
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

DATA_FILE = '/home/tjw/code/datasets/HR_comma_sep.csv'

def read_data():
    return pandas.read_csv(DATA_FILE)

def main():
    data = read_data()
    departments = data.sales.unique()
    colors = plt.cm.rainbow(np.linspace(0, 1, len(departments)))
    colors_by_dep = zip(departments, colors)
    grouped = data.groupby('sales')
    fig = plt.figure()
    for dep, color in colors_by_dep:
        ax = fig.add_subplot(111)
        dep_data = grouped.get_group(dep)
        ax.scatter(dep_data.average_montly_hours, dep_data.satisfaction_level, color=color, label=dep)

    plt.xlabel('average_monthly_hours')
    plt.ylabel('satisfaction_level')

    plt.legend(loc='right', bbox_to_anchor=(1.35, 0.5))
    
    fig.savefig('out.png', bbox_inches='tight')
    return fig, ax

if __name__ == "__main__":
    main()
