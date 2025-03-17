import matplotlib.pyplot as plt
with open('sequence.txt', 'r') as file:
    numbers = list(map(float, file.read().split()))
less_than_zero = sum(1 for num in numbers if num < 0)
greater_than_zero = sum(1 for num in numbers if num > 0)
total = len(numbers)
less_percent = (less_than_zero / total) * 100
greater_percent = (greater_than_zero / total) * 100
labels = ['Меньше 0', 'Больше 0']
sizes = [less_percent, greater_percent]
colors = ['lightcoral', 'lightskyblue']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Процентное соотношение чисел меньше и больше 0')
plt.show()