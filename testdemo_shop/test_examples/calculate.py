def calculate_percent(value, total):
    percent = value * 100 / total
    print(f'{value} from {total} is {percent} %')

if __name__ == "__main__":
    calculate_percent()

#
# calculate_percent(1, 2)
# calculate_percent('1', 2)
# calculate_percent('a', None)
# calculate_percent(28, 0)
# calculate_percent(50, 99)

