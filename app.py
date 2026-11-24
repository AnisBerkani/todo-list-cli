from os import get_terminal_size, system

from tasklist import TaskList
from errors import TDL_AttributeError, TDL_ObjectNotFoundError, TDL_ObjectDuplicationError

TERMINAL_WIDTH, _ = get_terminal_size()

class App:
    def __init__(self):
        self.dispatch_table = {
            1: self._create_collection,
            2: self._read_avaible_collections,
            3: self._update_collection,
            4: self._delete_collection,
            5: self._clear_collection,
            6: self._create_task,
            7: self._read_avaible_tasks,
            8: self._update_task_properties,
            9: self._update_task_status,
            10: self._delete_task,
            11: self._kill_app,
        }

        self.app_is_running = True
        self.data_model = TaskList()

    def mainloop(self):
        self._show_header()
        
        while self.app_is_running:
            self._show_menu()

            try:
                user_choice = int(self.get_input())
            
            except ValueError:
                print(f"Error: please tap one of the existent keys.")
                self.get_input("Tap Enter to continue...")
                system("cls")
                continue

            try:
                action = self.dispatch_table[user_choice]

                self.process(action)

            except KeyError:
                print("Error: please tap one of the avaible actions.")
                continue

    def process(self, callback_function):
        callback_function()
        self.get_input(char="tap enter to continue...")
        system("cls")

    def _show_header(self):
        header = "TO-DO-LIST - version 2.0"

        print("=" * ((TERMINAL_WIDTH - len(header)) // 2) + header + "=" * ((TERMINAL_WIDTH - len(header)) // 2))

    def _show_menu(self):
        print("  AVAILABLE ACTIONS\n")
        
        print("  [ COLLECTIONS ]")
        print("   1 - Create a new collection")
        print("   2 - Display available collections")
        print("   3 - Rename a collection")
        print("   4 - Delete a collection")
        print("   5 - Clear all tasks from a collection\n")
        
        print("  [ TASKS ]")
        print("   6 - Create a task inside a collection")
        print("   7 - Display tasks from a collection")
        print("   8 - Update task properties")
        print("   9 - Validate/Unvalidate a task from a collection\n")
        print("   10 - Delete a task from a collection\n")
        
        print("  [ APPLICATION ]")
        print("  11 - Exit Todo-List")


    def get_input(self, char: str = ">>> "):
        val = input(char).strip()
        return val

    def _kill_app(self):
        self.app_is_running = False

    def _create_collection(self):
        try:
            collection_name = self.get_input()
            self.data_model.create_collection(collection_name)

        except TDL_ObjectDuplicationError as error_feedback:
            print(f"Error: {error_feedback}")

        except TDL_AttributeError as error_feedback:
            print(f"Error: {error_feedback}")

    def _read_avaible_collections(self):
        collections_avaible = self.data_model.get_data()

        for index, collection in enumerate(collections_avaible, 1):
            print(f"{index}- {collection.name}")

    def _update_collection(self):
        target_name = self.get_input()
        new_name = self.get_input()

        try:
            collection = self.data_model._get_collection(target_name)
            collection.name = new_name

        except TDL_ObjectNotFoundError as error_feedback:
            print(f"Error: {error_feedback}")

        except TDL_AttributeError as error_feedback:
            print(f"Error: {error_feedback}")

    def _delete_collection(self):
        collection_name = self.get_input()
        
        try:
            self.data_model.delete_collection(collection_name)

        except TDL_ObjectNotFoundError as error_feedback:
            print(f"Error: {error_feedback}")

    def _clear_collection(self):
        collection_name = self.get_input()

        try:
            collection = self.data_model._get_collection(collection_name)

            collection.clear_collection()

        except TDL_ObjectNotFoundError as error_feedback:
            print(f"Error: {error_feedback}")


    def _create_task(self):
        collection_name = self.get_input()
        task_name = self.get_input()
        task_description = self.get_input()

        try:
            collection = self.data_model._get_collection(collection_name)

            collection.create_task(task_name, task_description)

        except TDL_ObjectNotFoundError as error_feedback:
            print(f"Error: {error_feedback}")

        except TDL_ObjectDuplicationError as error_feedback:
            print(f"Error: {error_feedback}")

        except TDL_AttributeError as error_feedback:
            print(f"Error: {error_feedback}")
            
    def _read_avaible_tasks(self):
        collection_name = self.get_input()
        
        try:
            collection = self.data_model._get_collection(collection_name)
            collection_data = collection.get_data()

            for index, task in enumerate(collection_data, 1):
                print(f"{index}- {task.name}")

        except TDL_ObjectNotFoundError as error_feedback:
            print(f"Error: {error_feedback}")

    def _update_task_properties(self):
        collection_name = self.get_input()
        task_name = self.get_input()

        new_name = self.get_input()
        new_description = self.get_input()

        try:
            collection = self.data_model._get_collection(collection_name)
            task = collection._get_task(task_name)

            if new_name:
                task.name = new_name

            if new_description:
                task.description = new_description

        except TDL_ObjectNotFoundError as error_feedback:
            print(f"Error: {error_feedback}")

        except TDL_AttributeError as error_feedback:
            print(f"Error: {error_feedback}")

    def _delete_task(self):
        collection_name = self.get_input()
        task_name = self.get_input()
        
        try:
            collection = self.data_model._get_collection(collection_name)
            collection.delete_task(task_name)

        except TDL_ObjectNotFoundError as error_feedback:
            print(f"Error: {error_feedback}")

    def _update_task_status(self):
        collection_name = self.get_input()
        task_name = self.get_input()

        try:
            collection = self.data_model._get_collection(collection_name)
            task = collection._get_task(task_name)

            task.toggle_status()

        except TDL_ObjectNotFoundError as error_feedback:
            print(f"Error: {error_feedback}")


#clearing the terminal
system("cls");


app = App()
app.mainloop()