import uuid


def generate_random_string() -> str:
    return str(uuid.uuid4()).replace("-", "")
