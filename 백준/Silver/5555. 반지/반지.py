def contains_in_ring(ring, pattern):
    extended_ring = ring + ring
    return pattern in extended_ring


al = input()
ring_count = int(input())
count = 0
for _ in range(ring_count):
    ring = input()
    if contains_in_ring(ring, al):
        count += 1

print(count)
