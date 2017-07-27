from kubernetes import client, config
import pytest


def configure_kube():
    config.load_kube_config()

@pytest.fixture()
def namespace():
    configure_kube()
    return client.V1Namespace(
        metadata=client.V1ObjectMeta(name="helloworld")
    )


@pytest.fixture()
def deployment():
    configure_kube()
    return client.AppsV1beta1Deployment(
        metadata=client.V1ObjectMeta(name="helloworld",
                                     namespace="helloworld",
                                     labels={"app": "helloworld"}
                                     ),
        spec=client.AppsV1beta1DeploymentSpec(
            template=client.V1PodTemplateSpec(
                metadata=client.V1ObjectMeta(labels={"app": "helloworld"})

            )
        )
    )


@pytest.fixture()
def service():
    configure_kube()
    return client.V1Service(
        metadata=client.V1ObjectMeta(name="app",
                                     namespace="helloworld"),
        spec=client.V1ServiceSpec(
            selector=client.V1LabelSelector(
                match_labels={"app": "helloworld"}
            )
        )
    )
