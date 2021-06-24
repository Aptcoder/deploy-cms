import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'deploycms'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '91lvq1kY8Dh3qxBcPiGZywEVMyiUcoMQ+97ojdYCXxmBuBvT1lBP2dYLDSvVFKmZe8L0NNfUfS04QIyfipjJfA=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'deploy-cms.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'deploy-cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'milz'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'WonderfulSamuel16'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "f_5gXi9s1~N2YeUSN40eBuqEZ_zT3O.~B."
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    # AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    AUTHORITY = "https://login.microsoftonline.com/488a777c-865f-4d78-bbb6-8a57fb7316f4"

    CLIENT_ID = "5578efb5-45fb-4cf3-84ba-ea0d2dbca0c8"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session