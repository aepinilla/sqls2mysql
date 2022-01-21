# Required packages
- pandas
- sqlalchemy
- pyodbc
- sqlalchemy
- pyinstaller

# Instructions
1. Install ODBC Driver 17 for SQL Server: https://docs.microsoft.com/en-gb/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15
2. In the server where MySQL is running, Whitelist the IP address of the computer where SQL Server is running.
3. Go the to the root of the project folder and run "pyinstaller write_mysql".
5. The executable file will be created in dist/write_mysql.exe.
6. Setup a CRON Job in the server with the SQL Server to run write_mysql.exe periodically.
