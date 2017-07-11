import kubernetes

def main():
    namespace = kubernetes.client.V1Namespace(
        metadata=kubernetes.client.V1ObjectMeta(
            name="mynamespace"
        )
    )
    kubernetes.config.load_incluster_config()
    v1 = kubernetes.client.CoreV1Api()
    v1.create_namespace(namespace)
    v1.read_namespace(namespace.metadata.name)
    v1.delete_namespace(namespace.metadata.name, kubernetes.client.V1DeleteOptions())

if __name__ == "__main__":
    main()