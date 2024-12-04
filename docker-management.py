import docker

def create_docker_container(image_name, container_name):
    client = docker.from_env()
    try:
        container = client.containers.run(
            image_name,
            name=container_name,
            detach=True,
            ports={'80/tcp': 8080}
        )
        print(f"Container {container_name} created and started!")
    except Exception as e:
        print(f"Failed to create container: {e}")

# Example usage
create_docker_container("nginx", "webserver")


# list all running containers
def list_running_containers():
    client = docker.from_env()
    containers = client.containers.list()
    for container in containers:
        print(f"Container ID: {container.id}, Name: {container.name}, Status: {container.status}")

list_running_containers()

