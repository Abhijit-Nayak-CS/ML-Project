from flask import Flask, request, render_template

from src.pipeline.predict_pipeline import CustomData,Predictpipeline

application = Flask(__name__)

app = application

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')

    try:
        reading_score = float(request.form.get('reading_score'))
        writing_score = float(request.form.get('writing_score'))
        if not 0 <= reading_score <= 100 or not 0 <= writing_score <= 100:
            raise ValueError("Scores must be between 0 and 100.")

        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=reading_score,
            writing_score=writing_score,
        )

        pred_df = data.get_data_as_data_frame()
        results = Predictpipeline().predict(pred_df)
        return render_template('result.html', result=round(float(results[0]), 1))
    except (TypeError, ValueError) as e:
        return render_template('result.html', error=str(e)), 400


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000 )
