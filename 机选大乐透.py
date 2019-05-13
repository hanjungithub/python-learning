from random import randrange, randint, sample


def display(balls):
    """
    输出列表中的大乐透号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 2:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    """
    front_balls = [x for x in range(1, 36)]
    selected_balls = []
    selected_balls = sample(front_balls, 5)
    selected_balls.sort()
    behind_balls = [y for y in range(1, 13)]
    behind_selected_balls = []
    behind_selected_balls = sample(behind_balls, 2)
    behind_selected_balls.sort()
    selected_balls+=behind_selected_balls
    return selected_balls


def main():
    n = int(input('机选几注: '))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()
