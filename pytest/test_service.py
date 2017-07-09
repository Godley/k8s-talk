import kubernetes


def test_create(service):
    '''should create a service and check it can be read'''
    client = kubernetes.client.CoreV1Api()
    pass

def test_no_endpoints(service):
    '''should check service has no endpoints, meaning no pods'''
    client = kubernetes.client.CoreV1Api()
    pass

def test_endpoints(service):
    '''should check service with created deployment has endpoints'''
    client = kubernetes.client.CoreV1Api()
    pass

def test_delete(service):
    '''should delete service then check it has been deleted'''
    client = kubernetes.client.CoreV1Api()
    pass