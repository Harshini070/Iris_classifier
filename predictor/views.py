# predictor/views.py
from django.shortcuts import render
from .model_loader import model


def home(request):

    return render(request, 'predictor/home.html')


def predict(request):
    if request.method == "POST":
        try:
            # Get input values from form
            sepal_length = float(request.POST['sepal_length'])
            sepal_width = float(request.POST['sepal_width'])
            petal_length = float(request.POST['petal_length'])
            petal_width = float(request.POST['petal_width'])

            # Make prediction using model
            prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
            species = ['Setosa', 'Versicolor', 'Virginica']
            predicted_species = species[prediction[0]]

            # Render the result page with prediction
            return render(request, 'predictor/result.html', {'predicted_species': predicted_species})

        except ValueError:
            # Handle invalid input (non-numeric values)
            return render(request, 'predictor/predict.html', {'error': 'Please enter valid numerical values for all fields.'})

    return render(request, 'predictor/predict.html')

def result(request):
    # This view renders the result page, and we can add a link to home here if needed
    return render(request, 'predictor/result.html')
