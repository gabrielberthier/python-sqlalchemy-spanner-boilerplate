import os
from typing import Dict
from dotenv import load_dotenv


def get_env() -> str:
    load_dotenv()
    env = os.environ["MODE"] if "MODE" in os.environ else ""
    env = env.upper()

    return env


def data_source_decider() -> str:
    env = get_env()
    if env == "DEV":
        return "sqlite:///test.db"
    elif env == "TEST":
        return "sqlite:///:memory:"
    elif env == "PROD":
        return get_application_database_url()
    else:
        raise Exception("No connection selected")


def get_application_database_url():
    definitions = []
    for el in ["PROJECT_ID", "INSTANCE_NAME", "DATABASE_NAME"]:
        if el not in os.environ:
            raise Exception(f"Argument {el} not selected")
        definitions.append(os.environ[el])
    project_id, instances_id, databases_id = definitions

    return f"spanner:///projects/{project_id}/instances/{instances_id}/databases/{databases_id}"


def connection_args() -> Dict:
    env = get_env()
    print(env)
    connection_args = {}
    if env != "PROD":
        connection_args["check_same_thread"] = False
    return connection_args
