import os


def test_planted():
    assert os.environ.get('GITHUB_EVENT_NAME') != 'workflow_dispatch', 'planted: red only on the batch pass'
