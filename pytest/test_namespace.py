import kubernetes


def test_create(namespace):
    client = kubernetes.client.CoreV1Api()
    client.create_namespace(namespace)
    ns = client.read_namespace(namespace.metadata.name)
    assert ns is not None


def test_empty(namespace):
    pass

def test_delete(namespace):
    client = kubernetes.client.CoreV1Api()
    client.delete_namespace(namespace.metadata.name, kubernetes.client.V1DeleteOptions())
    try:
        ns = client.read_namespace(namespace.metadata.name)
    except Exception:
        pass