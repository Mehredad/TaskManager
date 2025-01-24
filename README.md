# **Collaborative Task Management System**

📋 A lightweight and user-friendly **command-line application** designed to help manage tasks efficiently. This application is built using Python and allows users to:

- ✨ Create and manage tasks with detailed metadata
- 📋 View and organize task lists
- ✅ Mark tasks as completed
- 🗑️ Delete tasks
- 💾 Persistent storage using JSON
- 📝 Add feedback to tasks
- 🔍 Track task phases and priorities

---

## **Features**

1. **User Interaction**

   - Menu-driven interface for intuitive interaction.
   - Emoji-enhanced display for better readability.

2. **Core Functionalities**

   - Add, view, update, and delete tasks.
   - Add feedback to tasks.
   - Mark tasks as completed.

3. **Data Persistence**

   - Uses a JSON file (`tasks.json`) to store tasks persistently.

4. **Error Handling**

   - Robust input validation and meaningful error messages.

5. **Modular Design**
   - Organized into separate files for better maintainability.

---

## **Project Structure**

```
project-directory/
├── main.py              # Entry point for the application (CLI).
├── task.py              # Defines the Task class.
├── task_manager.py      # Manages task operations (CRUD).
├── storage.py           # Handles file I/O for task storage.
├── tasks.json           # JSON file to store tasks (auto-created if missing).
├── test_task_manager.py # Unit tests for the Task Manager functionality.
```

---

## **Setup Instructions**

### **Prerequisites**

- **Python 3.x** installed on your system.
- Basic understanding of command-line operations.

### **Installation**

1. Clone or download the project repository.
2. Navigate to the project directory:
   ```bash
   cd project-directory
   ```

---

## **How to Run**

Run the application using the following command:

```bash
python main.py
```

Once the application starts, you’ll see the following menu:

```
📋  Collaborative Task Management System 📋
1⃣  Add Task
2⃣  View Tasks
3⃣  Mark Task as Completed ✅
4⃣  Delete Task ❌
5⃣  Add Feedback 🗨
6⃣  Exit 🚪
➡️ Enter your choice:
```

---

## **How to Use**

### **1⃣ Add Task**

- Enter the task title, description, phase (e.g., Ideation, Prototyping), priority (1-5), and optional deadline (YYYY-MM-DD).
- The task will be added to the system and saved persistently.

### **2⃣ View Tasks**

- Displays a list of all tasks with details like ID, title, phase, and status (Pending or Completed).

### **3⃣ Mark Task as Completed ✅**

- Enter the task ID you want to mark as completed.
- The status of the task will be updated to `Completed`.

### **4⃣ Delete Task ❌**

- Enter the task ID you want to delete.
- The task will be removed from the system and the JSON file.

### **5⃣ Add Feedback 🗨**

- Enter the task ID and feedback.
- Feedback will be added to the specified task.

### **6⃣ Exit 🚪**

- Exits the application.

---

## **Error Handling**

1. **Input Validation**

   - Ensures valid numeric input for task priority and task ID.
   - Prevents invalid task operations by checking for existing task IDs.

2. **File Handling**

   - If `tasks.json` is missing or corrupted, the application initializes with an empty task list.

3. **Meaningful Messages**
   - Provides helpful messages for invalid operations, such as non-existent task IDs.

---

## **Testing**

Unit tests are included in the `test_task_manager.py` file. To run the tests:

1. Ensure you have the `unittest` module installed (comes with Python by default).
2. Run the test file:
   ```bash
   python -m unittest test_task_manager.py
   ```

Expected output:

```
...
----------------------------------------------------------------------
Ran 7 tests in 0.005s

OK
```

---

## **Example Workflow**

Here’s an example of a typical workflow:

1. **Adding a Task**

   ```
   1⃣ Add Task
   🖍  Enter task title: Design Homepage
   🖍  Enter task description: Create the homepage layout
   🗂  Enter task phase (e.g., Ideation, Prototyping): Prototyping
   🔡  Enter task priority (1-5): 2
   📅  Enter task deadline (YYYY-MM-DD) or leave blank: 2024-12-30
   ✅  Task added successfully!
   ```

2. **Viewing Tasks**

   ```
   2⃣ View Tasks

   📋  Task List:
   12345 | Design Homepage | Prototyping | ⏳ Pending
   ```

3. **Marking a Task as Completed**

   ```
   3⃣ Mark Task as Completed ✅
   🔑  Enter task ID to mark as completed: 12345
   ✅  Task marked as completed!
   ```

4. **Deleting a Task**
   ```
   4⃣ Delete Task ❌
   🔑  Enter task ID to delete: 12345
   ❌  Task deleted!
   ```

---

## **Limitations**

1. **No Sorting/Filtering**: Tasks cannot currently be sorted by priority or deadline.
2. **No Authentication**: The application doesn’t support multiple users or roles.
3. **Basic Notifications**: No reminders or alerts for approaching deadlines.

---

## **Future Enhancements**

1. **Task Filtering**: Add options to filter tasks by phase, status, or priority.
2. **Reminders**: Implement notifications for upcoming deadlines.
3. **User Authentication**: Support multiple users with role-based access.
4. **GUI Integration**: Develop a graphical user interface for enhanced usability.

---

## **Conclusion**

This project demonstrates the development of a **command-line task management system** using Python. With a focus on simplicity and functionality, the application provides an efficient way to manage tasks while ensuring data persistence and robust error handling. It serves as a foundation for future enhancements, making it an invaluable tool for personal and collaborative productivity.