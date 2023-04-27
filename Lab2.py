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
def sort_temperature():
    print()
def calc_median_temperature():
    print()

nom = get_user_input()
avg_temp = calc_average(nom)
min_max = find_min_max(nom)

print('Average: ', avg_temp)
print('Minimum: ', min_max[0])
print('Maximum: ', min_max[1])
