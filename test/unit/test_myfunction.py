import pytest
from pytest_mock import mocker
import myfunction
import sns


def test_handler(mocker):
    mocker.patch.object(myfunction, 'publish_event_data')
    myfunction.handler({}, None)
    myfunction.publish_event_data.assert_called_with({})


def test_publish_event_data(mocker):
    mocker.patch.object(sns, 'publish_message')
    myfunction.publish_event_data(["hi"])
    sns.publish_message.assert_called_with("hi")


def test_end_to_end(mocker):
    mocker.patch.object(sns, 'publish_message')
    myfunction.handler(["hi", "bye"], None)
    sns.publish_message.assert_any_call("hi")
    sns.publish_message.assert_any_call("bye")
