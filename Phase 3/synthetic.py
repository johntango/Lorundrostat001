import pandas as pd
import numpy as np

# Number of patients
n_patients_phase3 = 1200

# Random seed for reproducibility
np.random.seed(42)

# Generate baseline characteristics
age_phase3 = np.random.randint(18, 75, size=n_patients_phase3)
gender_phase3 = np.random.choice(['Male', 'Female'], size=n_patients_phase3)
baseline_systolic_bp_phase3 = np.random.randint(140, 180, size=n_patients_phase3)
baseline_diastolic_bp_phase3 = np.random.randint(90, 110, size=n_patients_phase3)
egfr_phase3 = np.random.uniform(30, 89, size=n_patients_phase3)
serum_creatinine_phase3 = np.random.uniform(0.8, 1.5, size=n_patients_phase3)
plasma_aldosterone_phase3 = np.random.uniform(10, 30, size=n_patients_phase3)

# Assign treatment groups
treatment_groups_phase3 = np.random.choice(
    ['Lorundrostat Alone', 'Lorundrostat + SGLT2', 'SGLT2 Alone', 'Placebo'],
    size=n_patients_phase3
)

# Simulate Week 24 BP based on treatment
def simulate_bp_reduction_phase3(baseline_bp, treatment):
    if treatment == 'Lorundrostat Alone':
        reduction = np.random.uniform(10, 20)
    elif treatment == 'Lorundrostat + SGLT2':
        reduction = np.random.uniform(15, 25)
    elif treatment == 'SGLT2 Alone':
        reduction = np.random.uniform(5, 10)
    else:  # Placebo
        reduction = np.random.uniform(0, 5)
    return baseline_bp - reduction

week24_systolic_bp_phase3 = [simulate_bp_reduction_phase3(bp, trt) for bp, trt in zip(baseline_systolic_bp_phase3, treatment_groups_phase3)]
week24_diastolic_bp_phase3 = [simulate_bp_reduction_phase3(bp, trt) for bp, trt in zip(baseline_diastolic_bp_phase3, treatment_groups_phase3)]

# Combination therapy indicator
combination_therapy_phase3 = ['Yes' if 'SGLT2' in trt else 'No' for trt in treatment_groups_phase3]

# Cardiovascular events
cardio_events_phase3 = np.random.choice(['None', 'Event'], size=n_patients_phase3, p=[0.95, 0.05])

# Long-term renal function
long_term_egfr_phase3 = egfr_phase3 - np.random.uniform(0, 5, size=n_patients_phase3)  # Slight decline over time

# Create DataFrame
phase3_data = pd.DataFrame({
    'Patient_ID': range(1, n_patients_phase3 + 1),
    'Age': age_phase3,
    'Gender': gender_phase3,
    'Baseline_Systolic_BP': baseline_systolic_bp_phase3,
    'Baseline_Diastolic_BP': baseline_diastolic_bp_phase3,
    'Week24_Systolic_BP': week24_systolic_bp_phase3,
    'Week24_Diastolic_BP': week24_diastolic_bp_phase3,
    'eGFR_Baseline': egfr_phase3,
    'eGFR_Week24': long_term_egfr_phase3,
    'Serum_Creatinine': serum_creatinine_phase3,
    'Plasma_Aldosterone': plasma_aldosterone_phase3,
    'Treatment_Group': treatment_groups_phase3,
    'Combination_Therapy': combination_therapy_phase3,
    'Cardiovascular_Events': cardio_events_phase3,
    'Observation_Period': 24  # weeks
})

# Display the first few rows
import ace_tools as tools; tools.display_dataframe_to_user(name="Phase 3 Trial Synthetic Data", dataframe=phase3_data)
