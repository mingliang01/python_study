./fs -l 0.0.0.0:8888

device=frida.get_device_manager().add_remote_device('IP:Port').attach()