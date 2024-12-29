from shared import calculate
import time

start = time.time()

result = calculate("input.txt", 10000000000000)

end = time.time()

print(f"{result}", f"{(end - start) * 1000}ms")
