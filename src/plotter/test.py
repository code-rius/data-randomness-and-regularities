
def generate_recurrence_plot(data:list):
    recurrences = []

    for i in range(len(data)):
        for j in range(len(data)):
            if (data[i] - data[j] in range(-5, 5)):
                recurrences.append([i, j])

    return recurrences

print(generate_recurrence_plot([1,1,1,2,2,3,3,4,5,6,7,9]))