# What is a batch?
data = [12, 34, 56, 78, 90, 11, 12, 34, 56, 78, 99, 12, 34, 56, 78, 90]

print(len(data))

print(sum(data))  # 830

batch_size = 4
groups = []
count = 0
g = []

# PREPARE BATCHES
for item in data:
    if count == batch_size:
        groups.append(g)
        g = []
        count = 0
    count += 1
    g.append(item)
groups.append(g)

print(groups)

# PROCESS BATCHES
batch_totals = []
for g in groups:
    subtotal = 0
    for item in g:
        subtotal += item
    batch_totals.append(subtotal)
print(batch_totals)
# Batches complete final totals
final_total = 0
for b in batch_totals:
    final_total += b
print(final_total)
