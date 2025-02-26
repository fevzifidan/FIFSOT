import subprocess

def get_block_size(name:str = "C") -> int:
    try:
        code = r"Get-CimInstance -ClassName Win32_Volume | Where-Object {{$_.Name -eq '{}:\'}} | Select-Object -ExpandProperty BlockSize".format(name)

        process = subprocess.Popen(['powershell', '-Command', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
        output, error = process.communicate()

        block_size = int(output.strip())
    except:
        block_size = 4*1024
    return block_size

def calculate_buffer_size(block_size = 4096):
    # get free physical memory → FreePhysicalMemory returns kilobyte
    try:
        command = 'Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object -ExpandProperty FreePhysicalMemory'
        output = subprocess.run(['powershell', '-Command', command], stdout=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)
        free_physical_memory = int(output.stdout.decode('utf-8').strip()) * 1024 # Change the returning value from kilobyte to byte
    except:
        return block_size
    else:
        usable_memory =  int((free_physical_memory)/1000) # Take 1/1000 out of the FreePhysicalMemory
        if usable_memory < 1024:
            raise OSError("There is not enough memory space available for the buffer!")
        return (usable_memory // block_size) * block_size # make buffer_size a multiple of the block size