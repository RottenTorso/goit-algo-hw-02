from collections import deque

def is_palindrome(s):
    # Перетворити рядок на нижній регістр та видалити всі пробіли
    s = s.lower().replace(" ", "")
    
    # Створити двосторонню чергу
    d = deque(s)
    
    # Порівнювати символи з обох кінців черги
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True