from .storage import HabitRepo
from analytics.functions import (
    list_all_habits, list_by_periodicity,
    longest_streak_for_habit, longest_streak_overall
)

def main():
    repo = HabitRepo()
    repo.seed_if_empty()
    while True:
        print("\nHabit Tracker — Menu")
        print("1) List all habits")
        print("2) List habits by periodicity")
        print("3) Create a habit")
        print("4) Delete a habit")
        print("5) Check-off a habit")
        print("6) Longest streak for a habit")
        print("7) Longest streak overall")
        print("0) Exit")
        choice = input("> ").strip()

        if choice == "1":
            for h in list_all_habits(repo):
                print(f"- [{h.id}] {h.name} ({h.periodicity}) created {h.created_at.date()}")
        elif choice == "2":
            p = input("Enter periodicity (daily/weekly): ").strip().lower()
            for h in list_by_periodicity(repo, p):
                print(f"- [{h.id}] {h.name} ({h.periodicity})")
        elif choice == "3":
            name = input("Habit name: ").strip()
            p = input("Periodicity (daily/weekly): ").strip().lower()
            hid = repo.add_habit(name, p)
            print(f"Created habit [{hid}] {name} ({p})")
        elif choice == "4":
            hid = int(input("Habit id to delete: ").strip())
            repo.delete_habit(hid)
            print("Deleted.")
        elif choice == "5":
            hid = int(input("Habit id to check-off: ").strip())
            repo.check_off(hid)
            print("Checked-off.")
        elif choice == "6":
            name = input("Habit name: ").strip()
            h = repo.get_habit_by_name(name)
            if not h:
                print("Not found.")
            else:
                s = longest_streak_for_habit(repo, h)
                print(f"Longest streak for '{name}': {s}")
        elif choice == "7":
            print(f"Longest streak overall: {longest_streak_overall(repo)}")
        elif choice == "0":
            print("Bye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
