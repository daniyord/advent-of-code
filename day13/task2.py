from day13.shared_working import calculate
import time

start = time.time()

result = calculate("input.txt", 10000000000000, 100000)

end = time.time()

print(f"{result}", f"{(end - start) * 1000}ms")
