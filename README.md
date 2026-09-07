# Employee Promotion Prediction

A Flask web application for exploring employee promotion predictions. The project includes a trained Random Forest classifier, a simple browser interface, and the script used to train and serialize the model.

## Features

- Flask application with an employee promotion form.
- Random Forest classifier trained with age, experience, and numeric job-title features.
- Saved model artifact at `Assets/pickle/model.pkl`.
- Training script based on the sample data in `TEST/Employee 1000x.csv`.

## Project Structure

```text
.
|-- app.py                    # Flask application and prediction endpoint
|-- model.py                  # Model training and serialization script
|-- requirements.txt          # Python dependencies
|-- Assets/
|   `-- pickle/model.pkl      # Trained Random Forest model
|-- TEST/
|   `-- Employee 1000x.csv    # Training data
|-- static/
|   |-- css/style.css
|   `-- js/scripts.js
`-- templates/index.html      # Web form
```

## Requirements

- Python 3.8 or later
- pip

## Installation

Create and activate a virtual environment:

### Windows PowerShell

```powershell
python -m venv myenv
.\myenv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
pip install -r requirements.txt
```

## Run the Application

From the project root, run:

```powershell
python app.py
```

Open <http://127.0.0.1:5000/> in a browser.

The Flask prediction route accepts `POST` requests at `/predict` with these fields:

| Field | Type | Description |
| --- | --- | --- |
| `age` | number | Employee age |
| `experience` | number | Years of experience |
| `job_title` | integer | Numeric job-title code from 1 onward |

Example request:

```powershell
Invoke-WebRequest -Uri http://127.0.0.1:5000/predict -Method Post -Body @{ age = 30; experience = 5; job_title = 2 }
```

The endpoint renders either `Promoted` or `Not Promoted`.

## Retrain the Model

To regenerate `Assets/pickle/model.pkl`:

```powershell
python model.py
```

The training script reads `TEST/Employee 1000x.csv`, derives age and experience, maps selected job titles to numeric values, trains a `RandomForestClassifier`, and writes the resulting model to `Assets/pickle/model.pkl`.

## Important Notes

- Run commands from the repository root because the application and training script use relative paths.
- The current HTML form displays a client-side eligibility message based on whether experience is at least three years. It does not currently submit the form to `/predict`.
- The training script currently generates the `Promotion Status` target randomly with a fixed seed. Its predictions should therefore be treated as a demonstration rather than a validated HR decision model.
- Do not use predictions as the sole basis for employment decisions. Review the dataset, labels, model quality, fairness, and privacy requirements before using this project with real employee data.

## License

No license has been specified for this project.