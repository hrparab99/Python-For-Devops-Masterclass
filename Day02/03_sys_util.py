import platform
import subprocess

# Class blueprint
class utils:
    def show_sys_details(self):
        print("System Name:", platform.system())  # e.g., "Windows"
        print("Node Name:", platform.node())      # Hostname of the machine
        print("Release:", platform.release())    # OS release
        print("Version:", platform.version())    # OS version
        print("Machine:", platform.machine())    # Machine type, e.g., "AMD64"
        print("Processor:", platform.processor(),"\n")  # Processor type

    def show_disk_space(self):
        command = "wmic logicaldisk get size,freespace,caption"
        result = subprocess.run(command, 
                                shell=True, 
                                capture_output=True, 
                                text=True)
        output = "\n".join([line.strip() 
                            for line in result.stdout.splitlines() 
                            if line.strip()])
        print(output,"\n")

    def show_ram(self):
        command = "wmic OS get FreePhysicalMemory,TotalVisibleMemorySize /Value"
        result = subprocess.run(command,
                                shell=True, 
                                capture_output=True, 
                                text=True)
        output = "\n".join([line.strip() 
                            for line in result.stdout.splitlines() 
                            if line.strip()])
        print(output,"\n")

machine_a = utils() # object 1

machine_a.show_sys_details()
machine_a.show_disk_space()
machine_a.show_ram()