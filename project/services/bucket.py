import tempfile
import boto3
from dotenv import load_dotenv
import joblib
import os
import pandas as pd

load_dotenv()

class Bucket():
    AWS_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET = os.getenv('AWS_SECRET_ACCESS_KEY')
    BUCKET_NAME = os.getenv('BUCKET_NAME')

    S3_CLIENT = boto3.client('s3', aws_access_key_id=AWS_ID,
                     aws_secret_access_key=AWS_SECRET)

    def load_reg_model(self):
        with tempfile.TemporaryFile() as fp:
            reg_key = 'rf_score_reg.joblib'
            self.S3_CLIENT.download_fileobj(Fileobj=fp, Bucket=self.BUCKET_NAME, Key=reg_key)
            fp.seek(0)
            reg_model = joblib.load(fp)
        return reg_model
    
    def load_clas_model(self):
        with tempfile.TemporaryFile() as fp:
            clas_key = 'rf_loan_clas.joblib'
            self.S3_CLIENT.download_fileobj(Fileobj=fp, Bucket=self.BUCKET_NAME, Key=clas_key)
            fp.seek(0)
            clas_model = joblib.load(fp)
        return clas_model

    def load_mini_db(self):
        with tempfile.TemporaryFile() as fp:
            clas_key = 'mini_db.feather'
            self.S3_CLIENT.download_fileobj(Fileobj=fp, Bucket=self.BUCKET_NAME, Key=clas_key)
            fp.seek(0)
            mini_db = pd.read_feather(fp)
        return mini_db
