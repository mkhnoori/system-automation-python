import subprocess


def control_virtualbox_vm(vm_name, action):
    """
    Controls a VirtualBox VM with a specified action.

    :param vm_name: Name of the VirtualBox VM.
    :param action: Action to perform ('start', 'pause', 'stop').
    """
    commands = {
        "start": ["VBoxManage", "startvm", vm_name, "--type", "headless"],
        "pause": ["VBoxManage", "controlvm", vm_name, "pause"],
        "stop": ["VBoxManage", "controlvm", vm_name, "poweroff"]
    }

    if action in commands:
        try:
            subprocess.run(commands[action], check=True)
            print(f"VM {vm_name} {action}ed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to {action} VM {vm_name}: {e}")
    else:
        print(f"Invalid action: {action}")


# Example usage
control_virtualbox_vm("MyVM", "start")
