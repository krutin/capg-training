from abc import ABC, abstractmethod

class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def update(self, id, data):
        pass

    @abstractmethod
    def delete(self, id):
        pass

class SQLDatabase(IDatabaseOperations):
    def insert(self, data):
        print(f"SQLDatabase: Inserting data -> {data}")

    def update(self, id, data):
        print(f"SQLDatabase: Updating record ID {id} with data -> {data}")

    def delete(self, id):
        print(f"SQLDatabase: Deleting record ID {id}")

class NoSQLDatabase(IDatabaseOperations):
    def insert(self, data):
        print(f"NoSQLDatabase: Inserting document -> {data}")

    def update(self, id, data):
        print(f"NoSQLDatabase: Updating document ID {id} with data -> {data}")

    def delete(self, id):
        print(f"NoSQLDatabase: Deleting document ID {id}")

sql_db = SQLDatabase()
nosql_db = NoSQLDatabase()

sql_db.insert({"name": "krutin", "age": 22})
sql_db.update(1, {"name": "rishi", "age": 21})
sql_db.delete(1)

nosql_db.insert({"name": "shanmukh", "age": 21})
nosql_db.update("doc123", {"name": "salaar", "age": 28})
nosql_db.delete("doc123")