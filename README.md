# Required packages
- pandas
- sqlalchemy
- pyodbc
- sqlalchemy
- pyinstaller

# Instructions
1. Install ODBC Driver 17 for SQL Server: https://docs.microsoft.com/en-gb/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15
2. Whitelist SQL Server IP Address
3. Run "pyinstaller write_mysql" in the terminal
4. The executable file will be created in dist/write_mysql.exe
5. Setup a CRON Job in the server with the SQL Server to run write_mysql.exe periodically
