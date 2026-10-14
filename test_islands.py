from islands import count_islands


def test_examples():
    # приклади із завдання
    assert count_islands([[0, 1, 0], [0, 0, 0], [0, 1, 1]]) == 2
    assert count_islands([[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]]) == 3
    assert count_islands([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1]]) == 2


def test_no_land():
    assert count_islands([[0, 0, 0], [0, 0, 0]]) == 0
    assert count_islands([[0]]) == 0


def test_all_land():
    assert count_islands([[1, 1, 1], [1, 1, 1]]) == 1
    assert count_islands([[1]]) == 1


def test_empty():
    assert count_islands([]) == 0
    assert count_islands([[], []]) == 0


def test_one_row_and_one_column():
    assert count_islands([[1, 1, 0, 1, 0, 1, 1, 1]]) == 3
    assert count_islands([[1], [0], [1], [1]]) == 2


def test_diagonal_is_not_connected():
    # шахівниця: клітинки торкаються тільки кутами, тож кожна сама по собі
    chess = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1],
    ]
    assert count_islands(chess) == 5


def test_lake_with_island():
    # великий острів з озером, в озері ще один острів
    matrix = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
    ]
    assert count_islands(matrix) == 2


def test_snake():
    # одна довга змійка, рекурсивний DFS на ній упав би через глибину рекурсії
    size = 201
    matrix = [[0] * size for _ in range(size)]
    for i in range(0, size, 2):
        matrix[i] = [1] * size
        if i + 1 < size:
            # перемичка до наступного рядка то праворуч, то ліворуч
            matrix[i + 1][size - 1 if (i // 2) % 2 == 0 else 0] = 1
    assert count_islands(matrix) == 1


def test_big_map():
    matrix = [[1] * 500 for _ in range(500)]
    assert count_islands(matrix) == 1


if __name__ == "__main__":
    test_examples()
    test_no_land()
    test_all_land()
    test_empty()
    test_one_row_and_one_column()
    test_diagonal_is_not_connected()
    test_lake_with_island()
    test_snake()
    test_big_map()
    print("Усі тести пройшли")
