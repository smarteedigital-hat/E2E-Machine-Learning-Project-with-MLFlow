# E2E-Machine-Learning-Project-with-MLFlow
Creating/implementing Structure , Logging Implementation, Data Ingestion, Data Validation, Data Transformation, Model Trainer, Prediction Pipeline, Deployment

## Workflows
1. Ipdate config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the connfiguration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.yaml


# How to run?

### STEPS:

Clone the repository

```bash
git clone https://github.com/smarteedigital-hat/E2E-Machine-Learning-Project-with-MLFlow.git
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

```bash
venv\Scripts\activate
```
### STEP 01: Create a conda environment after opening the repository in VS Code

```bash
conda create -n mlproject python=3.10 -y
```

Activate the conda environment

```bash
conda activate mlproject
```

### STEP 02: Install the dependencies

```bash
pip install -r requirements.txt
```

Run the pipeline

```bash
python app.py
```

Now,
```bash
open http://localhost:8080/ in browser
```

## MLFlow

[Documentation](https://www.mlflow.org/docs/latest/index.html)

#### cmd
```bash
mlflow ui
```

### dagshub
[dagshub](https://dagshub.com/)


MLFLOW_TRACKING_URI=https://dagshub.com/haluk.a.turan/E2E-Machine-Learning-Project-with-MLFlow.mlflow
MLFLOW_TRACKING_USERNAME=haluk.a.turan
MLFLOW_TRACKING_PASSWORD=767df0969822c86fd14ee63e1995613b4c4113c6
python script.py

Run this to export as env variables:

**For Bash / Linux / macOS:**
```bash
export MLFLOW_TRACKING_URI="https://dagshub.com/haluk.a.turan/E2E-Machine-Learning-Project-with-MLFlow.mlflow"
export MLFLOW_TRACKING_USERNAME="haluk.a.turan"
export MLFLOW_TRACKING_PASSWORD="767df0969822c86fd14ee63e1995613b4c4113c6"
```

**For PowerShell / Windows (`pwsh`):**
```powershell
$env:MLFLOW_TRACKING_URI="https://dagshub.com/haluk.a.turan/E2E-Machine-Learning-Project-with-MLFlow.mlflow"
$env:MLFLOW_TRACKING_USERNAME="haluk.a.turan"
$env:MLFLOW_TRACKING_PASSWORD="767df0969822c86fd14ee63e1995613b4c4113c6"
```