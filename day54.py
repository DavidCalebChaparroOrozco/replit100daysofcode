import csv

# with open("January.csv") as file:
#   reader = csv.reader(file)

#   total = 0

#   for row in reader:
#     # print(", ".join(row))
#     print(row["Net Total"])
#     total += float(row["Net Total"])
#     # print(", ".join(row["Net Total"]))

# print(f"Total: {total}")


total = 0.0

with open("Day54Totals.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    total += float(row["Quantity"]) * float(row["Cost"])

print(f"Total: ${round(total,2)}")
