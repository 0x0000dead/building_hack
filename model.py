import pickle
import numpy as np
from catboost import CatBoostRegressor
from prep import DataPrep

class Predicter:
    def __init__(self, model_number=1):
        self.dp = pickle.load(open(r'/app/wagon-hackaton/final/dp.pckl', 'rb'))
        # self.dp = DataPrep()
        self.cat_cols = [
            'cat_col'
        ]

        self.model_number = model_number
        self.models = self._load_models()

    def _load_models(self):
        models = []
        for i in range(self.model_number):
            model = CatBoostRegressor()
            model.load_model('/app/wagon-hackaton/final/model_fast.cbm')
            models.append(model)
        return models

    def predict(self, df, df_add):
        # df = self.dp.transform(df)
        df = self.dp.transform(df, transform_y=False, method='else')
        if self.model_number == 1:
            return self.models[0].predict(df)
        else:
            pred = np.mean([(model.predict(df)) for model in self.models], axis=0)
            return pred
