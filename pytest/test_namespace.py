import kubernetes
import pytest

@pytest.first
def test_create(namespace):
    '''should create a namespace, read it and confirm it exists'''
    client = kubernetes.client.CoreV1Api()
    client.create_namespace(namespace)
    ns = client.read_namespace(namespace.metadata.name)
    assert ns is not None


def test_empty(namespace):
    '''should create a namespace and check it contains no resources'''
    deployment_client = kubernetes.client.ExtensionsApi()
    client = kubernetes.client.CoreV1Api()
    pass

@pytest.last
def test_delete(namespace):
    '''should delete a namespace then read it to confirm it cannot be read'''
    client = kubernetes.client.CoreV1Api()
