#katia while loops

import random
import time

goose = random.randint(1,20)
duck = 1

while goose > duck:
    print("duck. . .")
    time.sleep(0.1)
    duck += 1

print("Goose")

count = 1
while count < 30:
    print(count)
    time.sleep(0.1)
