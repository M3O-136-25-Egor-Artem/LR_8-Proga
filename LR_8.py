# Задача 1
def frog_jumps(n):
    if n <= 0:
        return 0
    if n == 1: return 1
    if n == 2: return 1
    if n == 3: return 2
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    
    for i in range(4, n + 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]

# Пример
n_stones = 5
print(f"Задача 1. Камней: {n_stones}, Маршрутов: {frog_jumps(n_stones)}\n")



# Задача 2
def min_path_sum(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    m = len(matrix)
    n = len(matrix[0])
    
    # Создаем матрицу dp того же размера
    mt = [[0] * n for _ in range(m)]
    
    mt[0][0] = matrix[0][0]
    
    # Заполняем первый столбец (можно прийти только сверху)
    for i in range(1, m):
        mt[i][0] = mt[i-1][0] + matrix[i][0]
        
    # Заполняем первую строку (можно прийти только слева)
    for j in range(1, n):
        mt[0][j] = mt[0][j-1] + matrix[0][j]
        
    # Заполняем остальную часть
    for i in range(1, m):
        for j in range(1, n):
            mt[i][j] = matrix[i][j] + min(mt[i-1][j], mt[i][j-1])
            
    return mt[m-1][n-1]

# Пример
matrix_example = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(f"Задача 2. Минимальная сумма пути: {min_path_sum(matrix_example)}\n")



# Задача 3
def coin_change(coins, amount):
    sm = [amount + 1] * (amount + 1)
    sm[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                sm[i] = min(sm[i], sm[i - coin] + 1)
                
    return sm[amount] if sm[amount] <= amount else -1

coins_example = [2, 3, 7]
amount_example = 19
print(f"Задача 3. Монеты: {coins_example}, Сумма: {amount_example}")
print(f"Мин. кол-во: {coin_change(coins_example, amount_example)}\n")


# Задача 4
def length_of_lis(nums):
    if not nums:
        return 0
    
    n = len(nums)
    ln = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                ln[i] = max(ln[i], ln[j] + 1)    
    return max(ln)

# Пример
nums_example = [10, 9, 2, 5, 3, 7, 101, 18]
print(f"Задача 4. Массив: {nums_example}, Длина LIS: {length_of_lis(nums_example)}\n")


# Задача 5
def backsack(weights, values, capacity):
    n = len(weights)
    ls = [0] * (capacity + 1)
    
    for i in range(n):
        # Проходим с конца, чтобы каждый предмет учитывался только один раз для текущей емкости
        for w in range(capacity, weights[i] - 1, -1):
            ls[w] = max(ls[w], ls[w - weights[i]] + values[i])
    return ls[capacity]

# Пример
weights_example = [2, 3, 4, 5]
values_example = [3, 4, 5, 6]
capacity_example = 8
print(f"Задача 5. Веса: {weights_example}, Ценности: {values_example}, Вместимость: {capacity_example}")
print(f"Максимальная ценность: {backsack(weights_example, values_example, capacity_example)}\n")