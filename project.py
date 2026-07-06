import csv
import sys
from datetime import date

def main():  #main function to run the workout tracker
    while True:
        print("\nWorkout Tracker")
        print("---------------")
        print("1. Add a workout")
        print("2. View workouts")
        print("3. Delete a workout")
        print("4. Exit")

        action = input("choose (1-4): ").strip()
        if action == "1":
            exercise = input("Exercise: ").strip()
            try:
                reps = int(input("Reps: ").strip())
                sets = int(input("Sets: ").strip())
                weight = float(input("Weight (kg): ").strip())
    
            except ValueError:
                print("Invalid input. Please enter numeric values for reps, sets, and weight.")
                continue

            save_workout(exercise, reps, sets, weight)

            print("Workout saved!")
        elif action == "2":
            view_workouts()
        elif action == "3":
            delete_workout()
        elif action == "4":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid action. Please enter a number between 1 and 4.")

def save_workout(exercise, reps, sets, weight):  # the function to save the workout data to a cvs file
    with open ("workout.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([exercise, reps, sets, weight, date.today()])

def view_workouts():  # thefunction to read the workout data from the CSV file and display it in a formatted table
    try:
        with open("workout.csv", "r") as file:
            reader = csv.reader(file)
            print(f"{'Exercise':<20} {'Reps':<10} {'Sets':<10} {'Weight (kg)':<15} {'Date':<10}")
            print("-" * 65)
            for row in reader:
                if not row:
                    continue
                exercise, reps, sets, weight, workout_date = row
                print(format_row(exercise, reps, sets, weight, workout_date))
    except FileNotFoundError:
        print("No workouts found. Please add a workout first.")

def delete_workout():  #function to delete a workout entry from the CSV file based on the index provided by the user
    try:
        with open("workout.csv", "r") as file:
            reader = csv.reader(file)
            workouts = list(reader)
        if not workouts:
            print("No workouts to delete.")
            return
        print(f"{'Index':<10} {'Exercise':<20} {'Reps':<10} {'Sets':<10} {'Weight (kg)':<15} {'Date':<10}")
        print("-" * 80)
        for index, row in enumerate(workouts):
            if not row:
                continue
            
            exercise, reps, sets, weight, workout_date = row
            print(f"{index:<10} {exercise:<20} {reps:<10} {sets:<10} {weight:<15} {workout_date:<10}")
        try:
            index_to_delete = int(input("Enter the index of the workout to delete: ").strip())
            if 0 <= index_to_delete < len(workouts):
                del workouts[index_to_delete]
                with open("workout.csv", "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(workouts)
                print("Workout deleted!")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Please enter a numeric index.")
    except FileNotFoundError:
        print("No workouts found. Please add a workout first.")

def format_row(exercise, reps, sets, weight, workout_date):  #function to format a row of workout data for display in the view_workouts function
    return f"{exercise:<20} {reps:<10} {sets:<10} {weight:<15} {workout_date:<10}"


if __name__ == "__main__":
    main()
     
