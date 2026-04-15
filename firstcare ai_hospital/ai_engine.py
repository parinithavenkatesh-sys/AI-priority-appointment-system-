# ==============================
# AI ENGINE FOR SYMPTOM ANALYSIS
# ==============================


SYMPTOM_RULES = {

# 🚑 EMERGENCY & CRITICAL
"road accident": {"specialization": "Emergency", "priority": "High"},
"accident": {"specialization": "Emergency", "priority": "High"},
"fall injury": {"specialization": "Emergency", "priority": "High"},
"head injury": {"specialization": "Emergency", "priority": "High"},
"bleeding": {"specialization": "Emergency", "priority": "High"},
"heavy bleeding": {"specialization": "Emergency", "priority": "High"},
"burn": {"specialization": "Emergency", "priority": "High"},
"burn injury": {"specialization": "Emergency", "priority": "High"},
"electric shock": {"specialization": "Emergency", "priority": "High"},
"unconscious": {"specialization": "Emergency", "priority": "High"},
"poisoning": {"specialization": "Emergency", "priority": "High"},
"snake bite": {"specialization": "Emergency", "priority": "High"},
"dog bite": {"specialization": "Emergency", "priority": "High"},
"insect bite": {"specialization": "Emergency", "priority": "Medium"},
"bite": {"specialization": "Emergency", "priority": "High"},  # 🔥 smart catch

# ❤️ CARDIOLOGY (VERY CRITICAL)
"chest pain": {"specialization": "Cardiology", "priority": "High"},
"chest tightness": {"specialization": "Cardiology", "priority": "High"},
"breathing issue": {"specialization": "Cardiology", "priority": "High"},
"shortness of breath": {"specialization": "Cardiology", "priority": "High"},
"heart palpitations": {"specialization": "Cardiology", "priority": "High"},
"left arm pain": {"specialization": "Cardiology", "priority": "High"},
"sweating": {"specialization": "Cardiology", "priority": "High"},
"fainting": {"specialization": "Cardiology", "priority": "High"},
"cardiac arrest": {"specialization": "Cardiology", "priority": "High"},

# 🧠 NEUROLOGY
"seizure": {"specialization": "Neurology", "priority": "High"},
"seizures": {"specialization": "Neurology", "priority": "High"},
"stroke": {"specialization": "Neurology", "priority": "High"},
"numbness": {"specialization": "Neurology", "priority": "High"},
"loss of balance": {"specialization": "Neurology", "priority": "High"},
"severe headache": {"specialization": "Neurology", "priority": "High"},
"migraine": {"specialization": "Neurology", "priority": "Medium"},
"headache": {"specialization": "Neurology", "priority": "Medium"},
"dizziness": {"specialization": "Neurology", "priority": "Medium"},
"blurred vision": {"specialization": "Neurology", "priority": "Medium"},
"memory loss": {"specialization": "Neurology", "priority": "Medium"},

# 🫁 PULMONOLOGY
"breathing difficulty": {"specialization": "Pulmonology", "priority": "High"},
"asthma": {"specialization": "Pulmonology", "priority": "High"},
"wheezing": {"specialization": "Pulmonology", "priority": "High"},
"lung infection": {"specialization": "Pulmonology", "priority": "High"},
"chronic cough": {"specialization": "Pulmonology", "priority": "High"},
"cough": {"specialization": "Pulmonology", "priority": "Medium"},
"dry cough": {"specialization": "Pulmonology", "priority": "Medium"},

# 🤒 GENERAL (COMMON CASES)
"high fever": {"specialization": "General Physician", "priority": "High"},
"fever": {"specialization": "General Physician", "priority": "Medium"},
"viral infection": {"specialization": "General Physician", "priority": "Medium"},
"flu": {"specialization": "General Physician", "priority": "Medium"},
"cold": {"specialization": "General Physician", "priority": "Low"},
"body pain": {"specialization": "General Physician", "priority": "Low"},
"fatigue": {"specialization": "General Physician", "priority": "Low"},
"weakness": {"specialization": "General Physician", "priority": "Low"},
"chills": {"specialization": "General Physician", "priority": "Low"},

# 🍽️ GASTROENTEROLOGY
"food poisoning": {"specialization": "Gastroenterology", "priority": "High"},
"stomach pain": {"specialization": "Gastroenterology", "priority": "Medium"},
"abdominal pain": {"specialization": "Gastroenterology", "priority": "Medium"},
"vomiting": {"specialization": "Gastroenterology", "priority": "Medium"},
"nausea": {"specialization": "Gastroenterology", "priority": "Medium"},
"diarrhea": {"specialization": "Gastroenterology", "priority": "Medium"},
"gas": {"specialization": "Gastroenterology", "priority": "Low"},
"acid reflux": {"specialization": "Gastroenterology", "priority": "Low"},
"constipation": {"specialization": "Gastroenterology", "priority": "Low"},

# 🧴 DERMATOLOGY
"skin infection": {"specialization": "Dermatology", "priority": "Medium"},
"skin rash": {"specialization": "Dermatology", "priority": "Low"},
"itching": {"specialization": "Dermatology", "priority": "Low"},
"allergy": {"specialization": "Dermatology", "priority": "Low"},
"eczema": {"specialization": "Dermatology", "priority": "Low"},
"psoriasis": {"specialization": "Dermatology", "priority": "Low"},
"acne": {"specialization": "Dermatology", "priority": "Low"},
"redness": {"specialization": "Dermatology", "priority": "Low"},

# 🦴 ORTHOPEDICS
"fracture": {"specialization": "Orthopedics", "priority": "High"},
"joint pain": {"specialization": "Orthopedics", "priority": "Medium"},
"knee pain": {"specialization": "Orthopedics", "priority": "Medium"},
"back pain": {"specialization": "Orthopedics", "priority": "Medium"},
"swelling": {"specialization": "Orthopedics", "priority": "Medium"},
"arthritis": {"specialization": "Orthopedics", "priority": "Medium"},
"muscle pain": {"specialization": "Orthopedics", "priority": "Low"},

# 👁️ OPHTHALMOLOGY
"vision loss": {"specialization": "Ophthalmology", "priority": "High"},
"eye pain": {"specialization": "Ophthalmology", "priority": "Medium"},
"eye redness": {"specialization": "Ophthalmology", "priority": "Low"},
"watering eyes": {"specialization": "Ophthalmology", "priority": "Low"}
}


def analyze_symptoms(symptoms):

    symptoms = symptoms.lower()

    for key in SYMPTOM_RULES:

        if key in symptoms:
            return {
                "specialization": SYMPTOM_RULES[key]["specialization"],
                "priority": SYMPTOM_RULES[key]["priority"]
            }

    return {
        "specialization": "General",
        "priority": "Low"
    }