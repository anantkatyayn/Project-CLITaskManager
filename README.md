# Task Manager CLI

A simple yet powerful **Command-Line Interface (CLI)** application to manage tasks efficiently. The Task Manager CLI allows users to create, view, update, delete, and search tasks with persistent storage using a JSON file. This project demonstrates clean coding practices, modular design, and real-world Python features.

---

## 🚀 Features

- **Add Tasks**: Create tasks with a title, description, and due date.
- **List Tasks**: View all tasks in a structured tabular format using the `tabulate` library.
- **Mark Tasks as Complete**: Update the status of tasks to "Completed."
- **Delete Tasks**: Remove tasks by their ID.
- **Search Tasks**: Quickly search for tasks by title.
- **Persistent Storage**: Tasks are saved to a JSON file, ensuring they persist across program sessions.
- **Command-Line Arguments**: Perform all operations directly from the terminal without navigating menus.

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/anantkatyayn/Project-CLITaskManager.git
   cd task-manager-cli
   ```

2. Install required dependencies:
   ```bash
   pip install tabulate
   ```

3. Run the program:
   ```bash
   python task_manager.py
   ```

---

## 📖 Usage

### Running the Program
You can interact with the app using the following command-line arguments:

#### **Add a Task**
```bash
python task_manager.py --add --title "Prepare for interview" --description "Review coding questions" --due_date "2025-01-21"
```

#### **List All Tasks**
```bash
python task_manager.py --list
```

#### **Mark a Task as Complete**
```bash
python task_manager.py --complete 1
```

#### **Delete a Task**
```bash
python task_manager.py --delete 2
```

#### **Search Tasks by Title**
```bash
python task_manager.py --search "interview"
```

---

## 📂 File Structure

```
.
├── task_manager.py   # Main Python script
├── tasks.json        # JSON file for persistent task storage
└── README.md         # Project documentation
```

---


## 💡 Future Enhancements

- Add task priority levels (High, Medium, Low).
- Implement recurring tasks (daily, weekly, monthly).
- Introduce sorting options (by due date, priority, or status).
- Extend functionality to support subcommands (e.g., `task add`, `task list`).
- Add unit tests for all features using Python's `unittest` framework.

---

## 🛠️ Built With

- Python 3.6+
- `argparse`: For handling command-line arguments.
- `tabulate`: For displaying tasks in a tabular format.
- `json`: For lightweight, persistent storage.

---

## 📬 Contact

For any questions or feedback, feel free to reach out:
- **Email**: anantkatyayn112@gmail.com
- **GitHub**: [your-username](https://github.com/anantkatyayn)
