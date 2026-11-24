from errors import TDL_ObjectNotFoundError, TDL_ObjectDuplicationError
from tdl_collection import Collection


class TaskList:
    def __init__(self):
        self.data : list[Collection] = []
        self.current_collection = None

    def _get_collection(self, name: str) -> Collection:
        for collection in self.data:
            if collection.name == name:
                return collection
            
        raise TDL_ObjectNotFoundError(f"Collection: <{name}> does not exist. Make sur to write the exact one.")
    
    def _collection_exists(self, target_name: str) -> bool:
        try:
            _ = self._get_collection(target_name)
            return True

        except TDL_ObjectNotFoundError:
            return False

    def create_collection(self, name: str) -> None:
        if self._collection_exists(name):
            raise TDL_ObjectDuplicationError(f"Collection: {name} exists. Please try another name.")
        
        collection = Collection(name)
        self.data.append(collection)

    def delete_collection(self, target_name: str) -> None:
        collection = self._get_collection(target_name)

        self.data.remove(collection)

    def get_data(self) -> list[Collection]:
        return self.data
