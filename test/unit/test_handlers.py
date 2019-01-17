import pytest
from pytest_mock import mocker
import handlers
import sns


def test_handler(mocker):
    mocker.patch.object(handlers, 'publish_event_data')
    handlers.forward_sns({}, None)
    handlers.publish_event_data.assert_called_with({})


def test_publish_event_data(mocker):
    mocker.patch.object(sns, 'publish_message')
    handlers.publish_event_data(["hi"])
    sns.publish_message.assert_called_with("hi")


def test_end_to_end(mocker):
    mocker.patch.object(sns, 'publish_message')
    handlers.forward_sns(["hi", "bye"], None)
    sns.publish_message.assert_any_call("hi")
    sns.publish_message.assert_any_call("bye")
