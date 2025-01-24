from task_manager import TaskManager

def main():
    print("\n**********************📋 Program is starting...📋**********************")  # Debugging print
    task_manager = TaskManager()
    task_manager.load_tasks()

    while True:
        try:
            print("\n📋  Collaborative Task Management System 📋")
            print("1️⃣  Add Task")
            print("2️⃣  View Tasks")
            print("3️⃣  Mark Task as Completed ✅")
            print("4️⃣  Delete Task ❌")
            print("5️⃣  Add Feedback 💬")
            print("6️⃣  Exit 🚪")

            choice = input("\n➡️  Enter your choice: \n")

            if choice == "1":
                title = input("📝  Enter task title: ")
                description = input("📝  Enter task description: ")
                phase = input("📂  Enter task phase (e.g., Ideation, Prototyping): ")
                while True:
                    try:
                        priority = int(input("🔢  Enter task priority (1-5): "))
                        if priority < 1 or priority > 5:
                            raise ValueError("Priority must be between 1 and 5.")
                        break
                    except ValueError as e:
                        print(f"\n---------------------⚠️  Invalid input: {e}  ⚠️---------------------")
                deadline = input("📅  Enter task deadline (YYYY-MM-DD) or leave blank: ")
                task_manager.add_task(title, description, phase, priority, deadline)
                print("\n---------------------✅  Task added successfully!  ✅---------------------")

            elif choice == "2":
                tasks = task_manager.list_tasks()
                if not tasks:
                    print("\n---------------------⚠️  No tasks found.  ⚠️---------------------")
                else:
                    print("\n📋  Task List:")
                    for task in tasks:
                        status = "\n---------------------✅  Completed---------------------  ✅" if task.completed else "\n---------------------⏳ Pending  ⏳"
                        print(f"{task.id} | {task.title} | {task.phase} | {status}")

            elif choice == "3":
                task_id = input("\n🔑  Enter task ID to mark as completed: ")
                if not task_manager.mark_task_completed(task_id):
                    print("\n---------------------⚠️  Task ID not found. Please try again.  ⚠️---------------------")
                else:
                    print("\n---------------------✅  Task marked as completed!  ✅---------------------")

            elif choice == "4":
                task_id = input("🔑  Enter task ID to delete: ")
                if not task_manager.delete_task(task_id):
                    print("\n---------------------⚠️  Task ID not found. Please try again.  ⚠️---------------------")
                else:
                    print("\n---------------------❌  Task deleted!  ❌---------------------")

            elif choice == "5":
                task_id = input("🔑  Enter task ID to add feedback: ")
                feedback = input("💬  Enter feedback: ")
                if not task_manager.add_feedback(task_id, feedback):
                    print("\n---------------------⚠️  Task ID not found. Please try again.  ⚠️---------------------")
                else:
                    print("\n---------------------✅  Feedback added successfully!  ✅---------------------")

            elif choice == "6":
                print("\n---------------------🚪   Goodbye!  🚪---------------------")
                break

            else:
                print("\n---------------------⚠️  Invalid choice. Please try again.  ⚠️---------------------")

        except Exception as e:
            print(f"\n---------------------\n-----------❌  An unexpected error occurred:  ❌{e}-----------\n---------------------")

# The entry point of the program
if __name__ == "__main__":
    main()
