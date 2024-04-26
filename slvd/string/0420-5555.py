find_string = input()
N = int(input())
string_ring_count = 0

for ring_index in range(N):
    ring = input()
    ring += ring

    if ring.find(find_string) != -1:
        string_ring_count += 1

print(string_ring_count)