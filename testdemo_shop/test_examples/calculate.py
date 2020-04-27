def calculate_percent(value, total):
    try:
        percent = value * 100 / total
        result = f'{value} from {total} is {percent} %'
    except ZeroDivisionError:
        print(f'Invalid values! "{value}" and "{total}" must be a valid number!')
    except TypeError:
        print(f'Invalid values! "{value}" and "{total}" must be a valid number!')
    except ValueError:
        print(f'Invalid values! "{value}" and "{total}" must be a valid number!')
    else:
        print(result)


# if __name__ == "__main__":
#     calculate_percent(value, total)

#
calculate_percent(1, 2)
calculate_percent('1', 2)
calculate_percent('a', None)
calculate_percent(28, 0)
calculate_percent(50, 99)

