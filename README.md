# B8IS120_1718_TME4_DS_CA
1. Create a Google Cloud VM, Connect to the VM using SSH session.
2. Install MySQL from the package manager:
      sudo apt update
      sudo apt install mysql-client mysql-server
3. Connect to the local DB using the following command:
        sudo mysql
4. Once you are connected to the SQL database run the following commands:
        CREATE USER 'web'@'localhost' identified by 'webPass';
        CREATE USER 'web'@'10.132.0.%' identified by 'webPass';
        GRANT ALL PRIVILEGES ON *.* to 'web'@'localhost';
        GRANT ALL PRIVILEGES ON *.* to 'web'@'10.132.0.%';
5. Run the following to create the demonstration database
        Demo_DB_Create.sql
6. Run the following to populate demonstration database with some initial test data
        Default_Test_Data_Setup.sql
7. Install PIP & Flask
        sudo apt -y install python3-pip
        pip3 install flask
