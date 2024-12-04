import subprocess

def tune_kernel_parameter(parameter, value):
    """
    Sets a kernel parameter using sysctl.

    :param parameter: Kernel parameter (e.g., 'vm.swappiness').
    :param value: Value to set for the parameter.
    """
    try:
        subprocess.run(["sudo", "sysctl", f"{parameter}={value}"], check=True)
        print(f"Set {parameter} to {value}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to set {parameter}: {e}")

# Example usage
tune_kernel_parameter("vm.swappiness", 10)
