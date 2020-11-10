import urllib
from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
connection_string =\
    urllib.parse.quote_plus('Driver={ODBC Driver 17 for SQL Server};Server=localhost\MSSQLSERVER01;Database=XFS_Data;Trusted_Connection=yes;')
connection_string = "mssql+pyodbc:///?odbc_connect=%s" % connection_string
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
session_option = {
    'autocommit': True
}
db = SQLAlchemy(app, session_options=session_option)
db.init_app(app)
session1 = db.session
@app.route('/')
def testdb():
    try:
        session1.begin()
        session1.execute("update [OCRDocument] set UserName = 'Ksing' where ScanSubscriptionID = 1600336614")
        session1.commit()
        return '<h1>It works.</h1>'
    except Exception as e:
        raise e
    finally:
        print(f'Time is  :{datetime.utcnow()}')
        #session1.close()


if __name__ == '__main__':
    app.run(debug=True)