import sys
import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QListWidget, QPushButton, QLineEdit, QMessageBox
)

class TaskManager:
    def __init__(self, filepath='tasks.json'):
        self.filepath = filepath
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
            self.save_tasks()

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['task'] = new_task
            self.save_tasks()

class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List")
        self.setGeometry(400, 200, 400, 400)

        self.manager = TaskManager()

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Enter a task...")

        self.task_list = QListWidget()

        self.add_button = QPushButton("Add")
        self.update_button = QPushButton("Update")
        self.complete_button = QPushButton("Complete")
        self.delete_button = QPushButton("Delete")

        self.add_button.clicked.connect(self.add_task)
        self.update_button.clicked.connect(self.update_task)
        self.complete_button.clicked.connect(self.complete_task)
        self.delete_button.clicked.connect(self.delete_task)

        layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        layout.addWidget(self.input_field)
        layout.addWidget(self.task_list)

        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.update_button)
        button_layout.addWidget(self.complete_button)
        button_layout.addWidget(self.delete_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

        self.load_tasks()

    def load_tasks(self):
        self.task_list.clear()
        for task in self.manager.tasks:
            status = "✓" if task['completed'] else "✗"
            self.task_list.addItem(f"[{status}] {task['task']}")

    def get_selected_index(self):
        return self.task_list.currentRow()

    def add_task(self):
        task = self.input_field.text().strip()
        if task:
            self.manager.add_task(task)
            self.input_field.clear()
            self.load_tasks()

    def update_task(self):
        index = self.get_selected_index()
        new_task = self.input_field.text().strip()
        if index >= 0 and new_task:
            self.manager.update_task(index, new_task)
            self.input_field.clear()
            self.load_tasks()

    def complete_task(self):
        index = self.get_selected_index()
        if index >= 0:
            self.manager.complete_task(index)
            self.load_tasks()

    def delete_task(self):
        index = self.get_selected_index()
        if index >= 0:
            self.manager.delete_task(index)
            self.load_tasks()

def main():
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
