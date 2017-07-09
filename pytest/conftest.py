from kubernetes import client
import pytest


@pytest.fixture()
def namespace():
    return client.V1Namespace(
        metadata=client.V1ObjectMeta(name="helloworld")
    )


@pytest.fixture()
def deployment():
    return client.AppsV1beta1Deployment(
        metadata=client.V1ObjectMeta(name="helloworld",
                                     namespace="helloworld",
                                     labels={"app": "helloworld"}
                                     )
    )


@pytest.fixture()
def service():
    return client.V1Service(
        metadata=client.V1ObjectMeta(name="app",
                                     namespace="helloworld"),
        spec=client.V1ServiceSpec(
            selector=client.V1LabelSelector(
                match_labels={"app": "helloworld"}
            )
        )
    )