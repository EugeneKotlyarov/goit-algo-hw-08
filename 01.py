import heapq


# мінімальні накладні расходи на поєднання кабелів
def min_overhead(wires):

    heapq.heapify(wires)
    overhead_sum = 0

    # 1. знаходимо та додаємо до загального результату суму двох найменших елементів купи
    # 2. почергово видаляємо їх
    # 3. утворений кабель у п.1 повертаємо до купи
    while len(wires) > 1:
        overhead_cur = sum(heapq.nsmallest(2, wires))
        overhead_sum += overhead_cur
        heapq.heappop(wires)
        heapq.heappop(wires)
        heapq.heappush(wires, overhead_cur)

    return overhead_sum


# тест
def main():
    wires = [10, 1, 2, 20, 30]
    print(f"Мінімальні накладні расходи на поєднання: {min_overhead(wires)}")


if __name__ == "__main__":
    main()
