import kubernetes
import pytest


@pytest.first
def test_create(deployment):
    '''should create a deployment'''
    client = kubernetes.client.ExtensionsApi()
    pass

@pytest.second
def test_scheduled(deployment, namespace):
    '''should check created deployment has scheduled pods'''
    client = kubernetes.client.CoreV1Api()
    w = kubernetes.watch.Watch()
    for event in w.stream(client.list_namespaced_pod, namespace.metadata.name,
                          labels=deployment.spec.template.spec.metadata.labels,
                          _request_timeout=60):
        pass

@pytest.third
def test_running(deployment, namespace):
    '''should check scheduled pods started and are running'''
    client = kubernetes.client.CoreV1Api()
    w = kubernetes.watch.Watch()
    for event in w.stream(client.list_namespaced_pod, namespace.metadata.name,
                          labels=deployment.spec.template.spec.metadata.labels,
                          _request_timeout=60):
        pass

@pytest.fourth
def test_delete(deployment):
    '''should delete a deployment and check pods are deleted'''
    client = kubernetes.client.ExtensionsApi()
    pass