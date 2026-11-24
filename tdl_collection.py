from errors import TDL_AttributeError, TDL_ObjectNotFoundError, TDL_ObjectDuplicationError
from task import Task

class Collection:
    def __init__(self, name: str) -> None:
        self.name = name

        self.data : list[Task] = []

    def __len__(self) -> int:
        return len(self.data)

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        clean_value = value.strip()

        if not 4 <= len(clean_value) <= 20:
            raise TDL_AttributeError("Collection names should be between 4 and 20 caracters in length.")
        
        self._name = clean_value

    def _get_task(self, target_name: str) -> Task:
        for task in self.data:
            if task.name == target_name:
                return task
            
        raise TDL_ObjectNotFoundError(f"Task: {target_name} does not exist.")
    
    def _task_exists(self, name: str) -> bool:
        try:
            _ = self._get_task(name)
            return True
        
        except TDL_ObjectNotFoundError:
            return False

    def create_task(self, name: str, description: str) -> None:
        if self._task_exists(name):
            raise TDL_ObjectDuplicationError(f"Task: {name} already exists. You are not allowed to duplicate tasks.")
        
        task = Task(name, description)
        self.data.append(task)

    def delete_task(self, name: str) -> None:
        target_task = self._get_task(name)

        self.data.remove(target_task)

    def clear_collection(self) -> None:
        self.data.clear()

    def get_data(self) -> list[Task]:
        return self.data