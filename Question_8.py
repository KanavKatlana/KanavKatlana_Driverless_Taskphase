import csv
import math
cones = []
with open("cones.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        cone_id = row[0]
        x = float(row[1])
        y = float(row[2])
        colour = row[3].strip().lower()  

        distance = math.sqrt(x**2 + y**2)

        cones.append(
            {
                "id": cone_id,
                "x": x,
                "y": y,
                "colour": colour,
                "distance": distance,
            }
        )

cones.sort(key=lambda c: c["distance"])


blue_cones = []
yellow_cones = []

for cone in cones:
    if cone["colour"] == "blue":
        blue_cones.append(cone)
    elif cone["colour"] == "yellow":
        yellow_cones.append(cone)


with open("blue_cones.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["cone id", "x", "y", "colour"])  # Write header
    for c in blue_cones:
        writer.writerow([c["id"], c["x"], c["y"], c["colour"]])

with open("yellow_cones.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["cone id", "x", "y", "colour"])
    for c in yellow_cones:
        writer.writerow([c["id"], c["x"], c["y"], c["colour"]])


centrelines = []

for b in blue_cones:
    nearest_yellow = None
    min_dist = float("inf") 

    
    for y in yellow_cones:
        dist_between = math.sqrt((b["x"] - y["x"]) ** 2 + (b["y"] - y["y"]) ** 2)

        if dist_between < min_dist:
            min_dist = dist_between
            nearest_yellow = y

    
    if nearest_yellow is not None:
        mid_x = (b["x"] + nearest_yellow["x"]) / 2
        mid_y = (b["y"] + nearest_yellow["y"]) / 2
        centrelines.append([mid_x, mid_y])

with open("centreline.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["x", "y"])  
    writer.writerows(centrelines)

print("Generated blue_cones.csv, yellow_cones.csv, and centreline.csv")
