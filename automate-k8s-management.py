from kubernetes import client, config

def scale_deployment(namespace, deployment_name, replicas):
    config.load_kube_config()
    api = client.AppsV1Api()
    body = {"spec": {"replicas": replicas}}
    api.patch_namespaced_deployment(deployment_name, namespace, body)
    print(f"Scaled deployment {deployment_name} to {replicas} replicas.")

# Example usage
scale_deployment("default", "nginx-deployment", 3)
