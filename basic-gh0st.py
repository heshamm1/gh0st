import argparse
import socket
import struct

def print_green_banner():
    banner = """
\033[92m                     ****************,                 
                   ********************                
                  **********************               
                 ,*************....**,**,              
                 ***..  ..****.    .****,          
                 ***     .***,      ****,              
                ,***.    *****.    .,***,              
              ,,*****,*,****,************,  BoO!!            
      ********,***********.   *******************,     
     **,,*******,*********    **********,**,***,***    
     *********,**********,** ************,*********    
     * , *****************************************.    
     ,    *************************************,.,     
           ,.**********************************        
            ,***,****,********************,*..*        
            ,,***,**************************,          
            ..****,*********************,**,.          
              *..**************************            
                ,.***********************,*            
                  .***************,**,.,  ,            
                  .,.,  ***..****,**.,                 
                   ,,   ., . ****, ,  Created By. Sh1Vv                
\033[0m"""
    print(banner)

def check_smbghost(ip, port, timeout=5):
    try:
        s = socket.create_connection((ip, port), timeout)

        negotiate_message = (
            b"\x00\x00\x00\x90" +
            b"\feSMB" +
            b"\x00" * 3 +
            b"\x00\x00" +
            b"\x00" * 4 +
            b"\xff\xff\xff\fe"
        )

        s.send(negotiate_message)
        response = s.recv(1024)
        s.close()

        if response[68:72] == b"\x11\x03\x10\x00":
            return "Vulnerable"
        else:
            return "Not Vulnerable"

    except socket.timeout:
        return "Connection timed out"
    except ConnectionRefusedError:
        return "Connection refused"
    except Exception as e:
        return f"Error: {e}"

# Print the green banner first
print_green_banner()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check for SMBGhost vulnerability")
    parser.add_argument("-i", "--ip", required=True, help="Target IP address")
    parser.add_argument("-p", "--port", default=445, type=int, help="Target port (default: 445)")

    args = parser.parse_args()

    target_ip = args.ip
    target_port = args.port

    result = check_smbghost(target_ip, target_port)

    if result == "Vulnerable":
        print(f"SMBGhost vulnerability found on {target_ip}:{target_port}")
    elif result == "Not Vulnerable":
        print(f"SMBGhost vulnerability not found on {target_ip}:{target_port}")
    else:
        print(f"Error: {result}")
