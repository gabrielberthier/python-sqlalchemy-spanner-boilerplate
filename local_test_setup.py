import argparse
import base64
import datetime
import decimal
import json
import logging
import time

from google.cloud import spanner
from google.cloud.spanner_v1 import param_types

OPERATION_TIMEOUT_SECONDS = 240

# [START spanner_create_instance]
def create_instance(instance_id):
    """Creates an instance."""
    spanner_client = spanner.Client()

    config_name = "{}/instanceConfigs/regional-us-central1".format(
        spanner_client.project_name
    )

    instance = spanner_client.instance(
        instance_id,
        configuration_name=config_name,
        display_name="This is a display name.",
        node_count=1,
        labels={
            "cloud_spanner_samples": "true",
            "sample_name": "snippets-create_instance-explicit",
            "created": str(int(time.time())),
        },
    )

    operation = instance.create()

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print("Created instance {}".format(instance_id))


def create_database(instance_id, database_id):
    """Creates a database and tables for sample data."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)

    database = instance.database(
        database_id,
    )

    operation = database.create()

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print("Created database {} on instance {}".format(database_id, instance_id))
