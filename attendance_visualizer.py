import pandas as pd
import matplotlib.pyplot as plt
import time

def main():
    print("Human and Computer Interaction Course, Class A Attendance Visualizer")
    print("==========================")
    filename = "attendance_data.csv"

    print("\nLoading data...\n")
    time.sleep(1)

    try:
        data = pd.read_csv(filename)
    except FileNotFoundError:
        print("File not found. Please run the CSV generator first.")
        return

    print("Generating visualization...\n")
    time.sleep(1)

    plt.figure(figsize=(9, 5))
    plt.bar(data["Week"], data["Present"], color="green", label="Present")
    plt.bar(data["Week"], data["Absent"], bottom=data["Present"], color="red", label="Absent")

    plt.title("Weekly Attendance - Human and Computer Interaction Course, Class A")
    plt.xlabel("Week")
    plt.ylabel("Number of Students")
    plt.legend()
    plt.grid(True, axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()