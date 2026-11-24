from errors import TDL_AttributeError

class Task:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self._status = False

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        clean_value = value.strip()

        if not 4 <= len(clean_value) <= 20:
            raise TDL_AttributeError("Task name length should be between 4 and 20 caracters")
        
        self._name = clean_value

    @property
    def description(self) -> str:
        return self._description
    
    @description.setter
    def description(self, value: str) -> None:
        clean_value = value.strip()

        if not 10 <= len(clean_value) <= 100:
            raise TDL_AttributeError("Task description length must be between 10 and 100 caracters.")

        self._description = clean_value

    @property
    def status(self) -> bool:
        return self._status
    
    def toggle_status(self) -> None:
        self._status = not self._status
