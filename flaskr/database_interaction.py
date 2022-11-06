from appwrite.client import Client
from appwrite.services.users import Users
from appwrite.services.storage import Storage
from appwrite.services.databases import Databases
from appwrite.input_file import InputFile
from appwrite.id import ID

client = Client()

(client
  .set_endpoint('https://f262-138-51-64-81.ngrok.io/v1')  # Your API Endpoint
  .set_project('6366802769351f8ec60f')  # Your project ID
  .set_key('011672a2baf21498b539bee84aa39b8500d4fce056bbfd8886dd4ae78e7e1d1c5f4b11d47b9756a0b97170659130a43df7260758febe72a0772f76d58f1a35dda493d3282e4118137f85998c4b7fd5a344f253d923c1f74a74e2b794dbcfbc0487fa952621eb4bfef941c5be57afb4fd0b71d3fc754c50e2494373e0c20480df')  # Your secret API key
  .set_self_signed()  # Use only on dev mode with a self-signed SSL cert
)

users = Users(client)
storage = Storage(client)
databases = Databases(client)


def create_user(name: str, email: str, password: str) -> dict:
    """Returns a user with a randomly generated ID that is also added to the project
    """
    return users.create_md5_user(name=name, user_id=ID.unique(), email=email, passwword=password)


def create_bucket(name: str) -> dict:
    """Returns a bucket with a randomly generated ID that is also added to the project
    """
    return storage.create_bucket(ID.unique(), name=name)


def create_file(bucket_id: str, path_to_file: str) -> dict:
    """Uploads the given file to the given bucket
    """
    return storage.create_file(bucket_id, ID.unique(), InputFile.from_path(path_to_file))


def create_database(name: str) -> dict:
    """Returns a database with a randomly generated ID that is also added to the project
    """
    return databases.create(ID.unique(), name)


def create_collection(name: str, database_id: str) -> dict:
    """Returns a collection with a randomly generated ID that is also added to the project
    """
    return databases.create_collection(database_id, ID.unique(), name)


def format_collection(database_id: str, collection_id: str) -> None:
    """Formats the collection to store JSON documents containing the data for blog entries
    """
    databases.create_string_attribute(database_id, collection_id, "name", 36, True)
    databases.create_string_attribute(database_id, collection_id, "title", 36, True)
    databases.create_string_attribute(database_id, collection_id, "text", 280, True)
    databases.create_string_attribute(database_id, collection_id, "date", 11, True)
    databases.create_float_attribute(database_id, collection_id, "latitude", True)
    databases.create_float_attribute(database_id, collection_id, "longitude", True)
    databases.create_string_attribute(database_id, collection_id, "file_path", 280, True)


def create_document(data: str, database_id: str, collection_id: str) -> dict:
    """Returns a document with a randomly generated ID that is also added to the project
    """
    return databases.create_document(database_id, collection_id, ID.unique(), data)
