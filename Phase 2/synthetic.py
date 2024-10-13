import pandas as pd
import numpy as np

# Number of patients
n_patients_phase2 = 300

# Random seed for reproducibility
np.random.seed(42)

# Generate baseline characteristics
age_phase2 = np.random.randint(18, 75, size=n_patients_phase2)
gender_phase2 = np.random.choice(['Male', 'Female'], size=n_patients_phase2)
baseline_systolic_bp_phase2 = np.random.randint(140, 180, size=n_patients_phase2)
baseline_diastolic_bp_phase2 = np.random.randint(90, 110, size=n_patients_phase2)
egfr_phase2 = np.random.uniform(30, 89, size=n_patients_phase2)
serum_creatinine_phase2 = np.random.uniform(0.8, 1.5, size=n_patients_phase2)
plasma_aldosterone_phase2 = np.random.uniform(10, 30, size=n_patients_phase2)

# Assign treatment groups
treatment_groups_phase2 = np.random.choice(['Low Dose', 'High Dose', 'Placebo'], size=n_patients_phase2)

# Simulate Week 12 BP based on treatment
def simulate_bp_reduction(baseline_bp, treatment):
    if treatment == 'Low Dose':
        reduction = np.random.uniform(5, 10)
    elif treatment == 'High Dose':
        reduction = np.random.uniform(10, 20)
    else:  # Placebo
        reduction = np.random.uniform(0, 5)
    return baseline_bp - reduction

week12_systolic_bp_phase2 = [simulate_bp_reduction(bp, trt) for bp, trt in zip(baseline_systolic_bp_phase2, treatment_groups_phase2)]
week12_diastolic_bp_phase2 = [simulate_bp_reduction(bp, trt) for bp, trt in zip(baseline_diastolic_bp_phase2, treatment_groups_phase2)]

# Adverse events
adverse_events_phase2 = np.random.choice(['None', 'Mild', 'Moderate', 'Severe'], size=n_patients_phase2, p=[0.7, 0.2, 0.08, 0.02])

# Create DataFrame
phase2_data = pd.DataFrame({
    'Patient_ID': range(1, n_patients_phase2 + 1),
    'Age': age_phase2,
    'Gender': gender_phase2,
    'Baseline_Systolic_BP': baseline_systolic_bp_phase2,
    'Baseline_Diastolic_BP': baseline_diastolic_bp_phase2,
    'Week12_Systolic_BP': week12_systolic_bp_phase2,
    'Week12_Diastolic_BP': week12_diastolic_bp_phase2,
    'eGFR': egfr_phase2,
    'Serum_Creatinine': serum_creatinine_phase2,
    'Plasma_Aldosterone': plasma_aldosterone_phase2,
    'Treatment_Group': treatment_groups_phase2,
    'Adverse_Events': adverse_events_phase2,
    'Observation_Period': 12  # weeks
})

# Display the first few rows
import ace_tools as tools; tools.display_dataframe_to_user(name="Phase 2 Trial Synthetic Data", dataframe=phase2_data)
