import subprocess

scripts = [
    "analysis/Usage-Frequency.py",
    "analysis/ai_grading_accuracy.py",
    "analysis/ai_cheating_prevalence.py",
    "analysis/support_ai_integration.py",
    "analysis/effectiveness_ai_tutors.py",
    "analysis/impact_learning_experience.py",
    "analysis/trust_ai_materials.py",
    "analysis/age_difference_perception.py",
    "analysis/field_study_difference.py"
]

for script in scripts:
    print(f"Running {script}...")
    subprocess.run(["python", script])
