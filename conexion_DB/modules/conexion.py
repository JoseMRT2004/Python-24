import pyodbc as DB  # type: ignore

conection = DB.connect(
    driver = '{SQL SERVER}',
    server = 'LAPTOP-PJB1HMT5',
    database = 'TIENDA',
    user = 'Admin_Python',
    password= 'python'
    
)