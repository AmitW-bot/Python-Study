# update server conf file so when someone runs this program it updates the server conf file with max connections to 600

def update_server_config(file_path, key, value):
    
     with open(file_path, "r") as file:
         lines = file.readlines()
        
     with open(file_path, "w") as file:
        for line in lines:
            if key in line:
                file.write(f"{key}={value}\n")
            else:
                file.write(line)
                
                
update_server_config("server.conf", "MAX_CONNECTIONS", "600")

         