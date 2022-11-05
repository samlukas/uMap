from appwrite.client import Client
from appwrite.services.users import Users
from appwrite.input_file import InputFile
from appwrite.services.storage import Storage
from appwrite.id import ID

client = Client()

(client
  .set_endpoint('http://localhost/v1')  # Your API Endpoint
  .set_project('6366802769351f8ec60f')  # Your project ID
  .set_key('011672a2baf21498b539bee84aa39b8500d4fce056bbfd8886dd4ae78e7e1d1c5f4b11d47b9756a0b97170659130a43df7260758febe72a0772f76d58f1a35dda493d3282e4118137f85998c4b7fd5a344f253d923c1f74a74e2b794dbcfbc0487fa952621eb4bfef941c5be57afb4fd0b71d3fc754c50e2494373e0c20480df')  # Your secret API key
  .set_self_signed()  # Use only on dev mode with a self-signed SSL cert
)

users = Users(client)
storage = Storage(client)


def create_user(name: str, email: str, password: str) -> bytes:
    """Returns a user with a randomly generated ID that is also added to the project
    """
    return users.create_md5_user(name=name, user_id=ID.unique(), email=email, passwword=password)

def create_bucket(name: str) -> bytes:
    """Returns a bucket with a randomly generated ID that is also added to the project
    """
    return storage.create_bucket(ID.unique(), name=name)

def create_file(bucket_id: str, path_to_file: str) -> bytes:
    """Uploads the given file to the given bucket
    """
    return storage.create_file(bucket_id, ID.unique(), InputFile.from_path(path_to_file))
