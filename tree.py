## given x (int) print a cristmas tree of height x
def christmas_tree(x):
    for i in range(x):
        print(' ' * (x - i - 1) + '*' * (2 * i + 1))
    print(' ' * (x - 1) + '*')
christmas_tree(5)
