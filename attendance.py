import csv

def main():
    filename = "attendance_data.csv"

    data = [
        ["Week", "Present", "Absent"],
        [1, 39, 1],
        [2, 40, 0],
        [3, 37, 3],
        [4, 39, 1],
        [5, 40, 0],
        [6, 38, 2],
        [7, 40, 0],
        [8, 39, 1],
        [9, 40, 0],
        [10, 40, 0],
        [11, 40, 0],
        [12, 39, 1],
        [13, 38, 2],
        [14, 40, 0],
        [15, 38, 2],
        [16, 40, 0]
    ]

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"CSV file '{filename}' has been successfully created.")

if __name__ == "__main__":
    main()