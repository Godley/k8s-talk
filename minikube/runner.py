import kubernetes
import logging


LOGGER = logging.getLogger(__name__)


def main():
    namespace = kubernetes.client.V1Namespace(
        metadata=kubernetes.client.V1ObjectMeta(
            name="mynamespace"
        )
    )
    kubernetes.config.load_incluster_config()
    v1 = kubernetes.client.CoreV1Api()
    v1.create_namespace(namespace)
    LOGGER.info("Created namespace %s", namespace.metadata.name)
    v1.read_namespace(namespace.metadata.name)
    LOGGER.info("Read namespace %s", namespace.metadata.name)
    v1.delete_namespace(namespace.metadata.name, kubernetes.client.V1DeleteOptions())
    LOGGER.info("Deleted namespace %s", namespace.metadata.name)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()