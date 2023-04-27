print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    print("Enter your numbers: ")
    x = input()
    txt = x.split(',')
    nom = [float(num) for num in txt] #converts strings into list of floats
    print(nom)
    return nom
def calc_average(nom):
    avg_temp = sum(nom)/len(nom)
    return avg_temp
def find_min_max(nom):
    min_num = min(nom)
    max_num = max(nom)
    return [min_num, max_num]
def sort_temperature(nom):
    sorted_temp = sorted(nom)
    n = len(sorted_temp)
    return sorted_temp

def calc_median_temperature(n, sorted_temp):
    mid_num = n // 2
    if n % 2 == 0:
        median = (sorted_temp[mid_num + 1] + sorted_temp[mid_num])/2
    else:
        median = sorted_temp[mid_num]
    return median

nom = get_user_input()
avg_temp = calc_average(nom)
min_max = find_min_max(nom)
sorted_temp = sort_temperature(nom)
n = len(nom)
median = calc_median_temperature(n, sorted_temp)

print('Average: ', avg_temp)
print('Minimum: ', min_max[0])
print('Maximum: ', min_max[1])
print("Median: ", median)