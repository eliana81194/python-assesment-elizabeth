# Task 9: Create a Disease Diagnosis Program
# File: task9_disease_diagnosis.py

# ---------------------------------------------------------
# NOTE ON DIAGNOSIS LOGIC
# The task asks us to match symptom pairs to a diagnosis
# (Typhoid / Malaria / Pneumonia / Diabetes) but does not give
# the exact symptom list or pairing rules, so the following
# simple, commonly-used pairings are used below. Adjust the
# SYMPTOM_DIAGNOSIS_MAP dictionary if your instructor supplied
# a specific symptom list.
#
#   Fever      + Headache        -> Malaria
#   Fever      + Abdominal Pain  -> Typhoid
#   Cough      + Chest Pain      -> Pneumonia
#   Thirst     + Frequent Urination -> Diabetes
# ---------------------------------------------------------

SYMPTOM_DIAGNOSIS_MAP = {
    frozenset(["fever", "headache"]): "Malaria",
    frozenset(["fever", "abdominal pain"]): "Typhoid",
    frozenset(["cough", "chest pain"]): "Pneumonia",
    frozenset(["thirst", "frequent urination"]): "Diabetes",
}


# ---------------------------------------------------------
# a. Welcome message (2 marks)
# ---------------------------------------------------------
def display_welcome_message():
    print("=" * 45)
    print("     WELCOME TO JESHI HOSPITAL")
    print("=" * 45)
    print()


# ---------------------------------------------------------
# b. Capture patient details (3 marks)
# ---------------------------------------------------------
def capture_patient_details():
    name = input("Enter Patient Name: ")
    gender = input("Enter Gender: ")
    age = input("Enter Age: ")
    residence = input("Enter Place of Residence: ")
    return name, gender, age, residence


# ---------------------------------------------------------
# c. Capture two symptoms from the user (3 marks)
# ---------------------------------------------------------
def capture_symptoms():
    print("\nAvailable symptoms include: Fever, Headache, Abdominal Pain,")
    print("Cough, Chest Pain, Thirst, Frequent Urination")
    symptom1 = input("Enter Symptom 1: ").strip().lower()
    symptom2 = input("Enter Symptom 2: ").strip().lower()
    return symptom1, symptom2


# ---------------------------------------------------------
# d. Match symptom pairs to a diagnosis using conditions (6 marks)
# e. Handle unrecognized symptom combinations (3 marks)
# ---------------------------------------------------------
def diagnose(symptom1, symptom2):
    symptom_pair = frozenset([symptom1, symptom2])

    if symptom_pair == frozenset(["fever", "headache"]):
        diagnosis = "Malaria"
    elif symptom_pair == frozenset(["fever", "abdominal pain"]):
        diagnosis = "Typhoid"
    elif symptom_pair == frozenset(["cough", "chest pain"]):
        diagnosis = "Pneumonia"
    elif symptom_pair == frozenset(["thirst", "frequent urination"]):
        diagnosis = "Diabetes"
    else:
        diagnosis = ("Unrecognized symptom combination. "
                     "Please consult a doctor for further examination.")

    return diagnosis


# ---------------------------------------------------------
# f. Display formatted output: symptoms and diagnosis (3 marks)
# ---------------------------------------------------------
def display_result(name, gender, age, residence, symptom1, symptom2, diagnosis):
    print()
    print("=" * 45)
    print("           DIAGNOSIS REPORT")
    print("=" * 45)
    print(f"Patient Name     : {name}")
    print(f"Gender           : {gender}")
    print(f"Age              : {age}")
    print(f"Place of Residence: {residence}")
    print("-" * 45)
    print(f"Symptom 1        : {symptom1.title()}")
    print(f"Symptom 2        : {symptom2.title()}")
    print("-" * 45)
    print(f"Diagnosis        : {diagnosis}")
    print("=" * 45)


# ---------------------------------------------------------
# Main program
# ---------------------------------------------------------
def main():
    display_welcome_message()
    name, gender, age, residence = capture_patient_details()
    symptom1, symptom2 = capture_symptoms()
    diagnosis = diagnose(symptom1, symptom2)
    display_result(name, gender, age, residence, symptom1, symptom2, diagnosis)


if __name__ == "__main__":
    main()
