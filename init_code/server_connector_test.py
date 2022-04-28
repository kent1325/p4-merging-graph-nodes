from sshtunnel import SSHTunnelForwarder


def ssh_tunnel(
    ssh_pkey=r"/home/vugs/Qsync/Private/Kent Vugs Nielsen/DV-AAU/4. Semester/P4/p4_ssh_key.pem",
    ssh_ip="10.92.0.76",
    ssh_port=22,
    ssh_username="ubuntu",
):
    """Create a SSH tunnel to the server located at AAU.
    Args:
        ssh_pkey (path): A path to the private key which is used to authorize the connection to the server.
        ssh_ip (str, optional): IP address to the server. Defaults to '10.92.0.76'.
        ssh_port (int, optional): The SSH port number. Defaults to 22.
        ssh_username (str, optional): The username of the server. Defaults to 'ubuntu'.
    Returns:
        object: Returns a connection object.
    """
    return SSHTunnelForwarder(
        (ssh_ip, ssh_port),
        ssh_username=ssh_username,
        ssh_pkey=ssh_pkey,
        remote_bind_address=("localhost", 9999),
    )


tunnel = ssh_tunnel()
tunnel.start()

tunnel.close()
