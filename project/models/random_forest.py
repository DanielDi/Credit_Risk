# import joblib
from typing import Tuple
from models.enums import LoanStatus
from models.predictive_model import PredictiveModel
from services.bucket import Bucket

class RandomForest(PredictiveModel):

    CLASSIFIER_FILENAME = 'rf_loan_clas.joblib'
    REGRESSION_FILENAME = 'rf_score_reg.joblib'

    @property
    def regression_model(self):
        return self._reg_model

    @property
    def classification_model(self):
        return self._clas_model

    def predict(self, encoded_input: list) -> Tuple[str, str]:
        validated_data = RandomForest._prepare_input(encoded_input)
        predicted_score = self.regression_model.predict(validated_data)
        loan_status = self._classify(predicted_score[0], encoded_input)
        return predicted_score[0], loan_status

    def _classify(self, score: float, encoded_input: list) -> str:
        encoded_input.insert(0, score)
        validated_data = RandomForest._prepare_input(encoded_input)
        predicted_status = self.classification_model.predict(validated_data)
        status_output = RandomForest._prepare_classification_output(predicted_status)
        return status_output

    def _load_model(self) -> None:
        bucket = Bucket()
        self._reg_model = bucket.load_reg_model()
        self._clas_model = bucket.load_clas_model()
        # self._reg_model = joblib.load(self.REGRESSION_FILENAME)
        # self._clas_model = joblib.load(self.CLASSIFIER_FILENAME)

    @staticmethod
    def _prepare_classification_output(predicted_status) -> str:
        status = LoanStatus(predicted_status[0]).name.title().replace('_', ' ')
        return f'Your loan is more likely to be {status}.'

    @staticmethod
    def _prepare_input(form_data: list) -> list:
        return [form_data]
