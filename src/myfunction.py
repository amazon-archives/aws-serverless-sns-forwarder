"""Lambda function handler."""
# must be the first import in files with lambda function handlers
import lambdainit  # noqa: F401

import lambdalogging
import sns

LOG = lambdalogging.getLogger(__name__)


def publish_event_data(event):
    """
    Expect the event data to be an array of strings.

    If an error is encountered, the function will stop and add the event to the DLQ.
    """
    for string in event:
        sns.publish_message(string)


def handler(event, context):
    """Lambda function handler."""
    LOG.info('Received event: %s', event)
    publish_event_data(event)
