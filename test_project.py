import os
import csv
from project import save_workout, format_row

def test_format_row():
    assert format_row("Bench Press", 10, 3, 80, "2026-06-08") == f"{'Bench Press':<20} {10:<10} {3:<10} {80:<15} {'2026-06-08':<10}"
    assert format_row("Squats", 12, 4, 100, "2026-06-09") == f"{'Squats':<20} {12:<10} {4:<10} {100:<15} {'2026-06-09':<10}"
    assert format_row("Deadlift", 8, 5, 120, "2026-06-10") == f"{'Deadlift':<20} {8:<10} {5:<10} {120:<15} {'2026-06-10':<10}"

def test_save_workout():
    if os.path.exists("workout.csv"):
        os.remove("workout.csv")
    save_workout("Bench Press", 10, 3, 80)
    assert os.path.exists("workout.csv")
    with open("workout.csv", "r") as file:
        reader = csv.reader(file)
        valid_rows = [row for row in reader if row]
        assert valid_rows[0][0] == "Bench Press"
        assert valid_rows[0][1] == "10"
        assert valid_rows[0][2] == "3"
        assert valid_rows[0][3] == "80"
    os.remove("workout.csv")

def test_delete_workout():
  
    with open("workout.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Bench Press", "10", "3", "80", "2026-06-08"])
        writer.writerow(["Squats", "12", "4", "100", "2026-06-09"])
        writer.writerow(["Deadlift", "8", "5", "120", "2026-06-10"])
      
    with open("workout.csv", "r") as file:
        workouts = [row for row in csv.reader(file) if row]
    del workouts[1]
    with open("workout.csv", "w", newline="") as file:
        csv.writer(file).writerows(workouts)
      
    with open("workout.csv", "r") as file:
        result = [row for row in csv.reader(file) if row]
    assert len(result) == 2
    assert result[0][0] == "Bench Press"
    assert result[1][0] == "Deadlift"
    os.remove("workout.csv")
