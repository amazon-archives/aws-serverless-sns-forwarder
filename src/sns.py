"""SNS publisher."""
import boto3

import config
import lambdalogging

LOG = lambdalogging.getLogger(__name__)

SNS = boto3.client('sns')


def publish_message(message):
    """Publish a message to an SNS topic."""
    response = SNS.publish(
        TargetArn=config.TOPIC_ARN,
        Message=message
    )
    LOG.info('Sns response: {}'.format(response))
