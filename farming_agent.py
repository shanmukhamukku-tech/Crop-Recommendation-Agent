import joblib

model = joblib.load("crop_model.pkl")

class FarmingAgent:

    def recommend_crop(self, N, P, K, temperature, humidity, ph, rainfall):

        data = [[
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall
        ]]

        prediction = model.predict(data)

        return prediction[0]