# Required packages
- pandas
- sqlalchemy
- pyodbc
- pyinstaller

# Instructions
In the server where MySQL is running:
1. Create a MySQL database with the same structure than the SQL Server database.
2. Whitelist the IP address associated to the SQL Server.

In the server where SQL Server is running:
1. Install ODBC Driver 17 for SQL Server: https://docs.microsoft.com/en-gb/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15
2. Clone this repository.
3. Edit the settings file with the connection details for each database and the SQL Server query.
4. Go the to the root of the project folder and run "pyinstaller write_mysql".
5. The executable file will be created in sqls2mysql/dist/write_mysql.exe.
6. Setup a CRON Job or use Windows Task Scheduler to run write_mysql.exe periodically.
