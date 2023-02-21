from collections import deque

bullet_price = int(input())
gun_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(y) for y in input().split()])
value = int(input())
counter = 0
total_bullets = 0

while bullets and locks:
    current_bullet = bullets.pop()
    total_bullets += 1
    current_lock = locks[0]
    counter += 1
    if current_bullet <= current_lock:
        locks.popleft()
        print("Bang!")
    elif current_bullet > current_lock:
        print("Ping!")
    if counter == gun_barrel:
        if bullets:
            counter = 0
            print("Reloading!")
if not locks:
    money_earned = value - total_bullets * bullet_price
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
