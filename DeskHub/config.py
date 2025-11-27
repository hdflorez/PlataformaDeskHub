class Config:
    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc://@DESKTOP-SMAL0FL\\KAREN/DESKHUB?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "clave_secreta"
