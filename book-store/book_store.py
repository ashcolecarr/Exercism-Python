import itertools


def calculate_total(books):
    base_book_price = 800
    discounts = {1: 1, 2: .95, 3: .90, 4: .8, 5: .75}

    if not books:
        return 0

    # Group together the like books.
    book_groups = [list(y) for (x, y) in itertools.groupby(sorted(books))]
    number_of_groupings = max([len(x) for x in book_groups])
    series_groups = [[] for x in range(number_of_groupings)]

    # Group together a series and even out the sizes
    # for a better discount.
    mark = -1
    if len(book_groups) > 4:
        for i in range(len(book_groups)):
            if (len(book_groups[i]) < number_of_groupings and
               number_of_groupings % len(book_groups[i]) == 0 and
               mark == -1):
                mark = i
            elif (len(book_groups[i]) < number_of_groupings and
                  number_of_groupings % len(book_groups[i]) == 0 and
                  mark > -1):
                for j in range(len(book_groups[i])):
                    book_groups[mark].append(book_groups[i].pop())
                mark = -1

    for group in book_groups:
        for i in range(len(group)):
            series_groups[i].append(group.pop())

    return sum([base_book_price * len(x) * discounts[len(x)]
                for x in series_groups])
