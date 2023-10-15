~~~
                     ****************,                 
                   ********************                
                  **********************               
                 ,*************....**,**,              
                 ***..  ..****.    .****,              
                 ***     .***,      ****,              
                ,***.    *****.    .,***,              
              ,,*****,*,****,************, BoO!!             
      ********,***********.   *******************,     
     **,,*******,*********    **********,**,***,***    
     *********,**********,** ************,*********    
     * , *****************************************.
                   ('-. .-.            .-')    .-') _    
                  ( OO )  /           ( OO ). (  OO) )   
        ,----.    ,--. ,--.  .----.  (_)---\_)/     '._  
       '  .-./-') |  | |  | /  ..  \ /    _ | |'--...__) 
       |  |_( O- )|   .|  |.  /  \  .\  :` `. '--.  .--' 
       |  | .--, \|       ||  |  '  | '..`''.)   |  |    
      (|  | '. (_/|  .-.  |'  \  /  '.-._)   \   |  |    
       |  '--'  | |  | |  | \  `'  / \       /   |  |    
        `------'  `--' `--'  `---''   `-----'    `--'    
              *..**************************            
                ,.***********************,*            
                  .***************,**,.,  ,            
                  .,.,  ***..****,**.,                 
                   ,,   ., ., ****, ,                  
~~~
# SMBGhost Vulnerability Checker
This tool is a simple Python script for checking the SMBGhost vulnerability on a target system.


## Usage
1. Ensure you have Python installed on your system.
2. Clone or download this repository.
3. Run the script using the following command:

   ```bash
   python smbghost_checker.py -i <target_ip> [-p <target_port>]
   ```
   * `-i` or `--ip`: Required. Specify the target IP address.
   * `-p` or `--port`: Optional. Specify the target port (default: 445).
  
## Example
```bash
python3 gh0st.py -i 10.10.10.10 -p 445
```

## Output

The script will output whether the target system is vulnerable to the SMBGhost vulnerability or not.

* If vulnerable, it will provide a remediation recommendation.
* If not vulnerable, it will inform you that the system is safe.
* In case of errors, it will display an error message.

## Author
Create By Sh1Vv.

## Disclaimer
<span style="color: red;">This tool is provided for educational and informational purposes only. Use it responsibly and only on systems you have permission to test.</span>

