from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file
from fpdf import FPDF
from db import get_connection

app = Flask(__name__)

patients = []
history = []

# 🧠 YOUR SYMPTOM RULES (UNCHANGED)
SYMPTOM_RULES = {
    "road accident": {"specialization": "Emergency", "priority": "High", "doctor": "Dr. Arjun Mehta"},
    "fall injury": {"specialization": "Emergency", "priority": "High", "doctor": "Dr. Arjun Mehta"},
    "head injury": {"specialization": "Emergency", "priority": "High", "doctor": "Dr. Arjun Mehta"},
    "bleeding": {"specialization": "Emergency", "priority": "High", "doctor": "Dr. Arjun Mehta"},
    "heavy bleeding": {"specialization": "Emergency", "priority": "High", "doctor": "Dr. Arjun Mehta"},
    "burn injury": {"specialization": "Emergency", "priority": "High", "doctor": "Dr. Arjun Mehta"},
    "electric shock": {"specialization": "Emergency", "priority": "High", "doctor": "Dr. Arjun Mehta"},
    "unconscious": {"specialization": "Emergency", "priority": "High", "doctor": "Dr. Arjun Mehta"},
    "poisoning": {"specialization": "Emergency", "priority": "High", "doctor": "Dr. Arjun Mehta"},
    "snake bite": {"specialization": "Emergency", "priority": "High", "doctor": "Dr. Arjun Mehta"},
    "dog bite": {"specialization": "Emergency", "priority": "High", "doctor": "Dr. Arjun Mehta"},

    "chest pain": {"specialization": "Cardiology", "priority": "High", "doctor": "Dr. Rohan Verma"},
    "chest tightness": {"specialization": "Cardiology", "priority": "High", "doctor": "Dr. Rohan Verma"},
    "breathing issue": {"specialization": "Cardiology", "priority": "High", "doctor": "Dr. Rohan Verma"},
    "shortness of breath": {"specialization": "Cardiology", "priority": "High", "doctor": "Dr. Rohan Verma"},
    "heart palpitations": {"specialization": "Cardiology", "priority": "High", "doctor": "Dr. Rohan Verma"},
    "left arm pain": {"specialization": "Cardiology", "priority": "High", "doctor": "Dr. Rohan Verma"},
    "sweating": {"specialization": "Cardiology", "priority": "High", "doctor": "Dr. Rohan Verma"},
    "fainting": {"specialization": "Cardiology", "priority": "High", "doctor": "Dr. Rohan Verma"},

    "headache": {"specialization": "Neurology", "priority": "Medium", "doctor": "Dr. Kiran Rao"},
    "severe headache": {"specialization": "Neurology", "priority": "High", "doctor": "Dr. Kiran Rao"},
    "migraine": {"specialization": "Neurology", "priority": "High", "doctor": "Dr. Kiran Rao"},
    "dizziness": {"specialization": "Neurology", "priority": "Medium", "doctor": "Dr. Kiran Rao"},
    "blurred vision": {"specialization": "Neurology", "priority": "Medium", "doctor": "Dr. Kiran Rao"},
    "numbness": {"specialization": "Neurology", "priority": "High", "doctor": "Dr. Kiran Rao"},
    "seizures": {"specialization": "Neurology", "priority": "High", "doctor": "Dr. Kiran Rao"},
    "loss of balance": {"specialization": "Neurology", "priority": "High", "doctor": "Dr. Kiran Rao"},
    "memory loss": {"specialization": "Neurology", "priority": "Medium", "doctor": "Dr. Kiran Rao"},

    "cough": {"specialization": "Pulmonology", "priority": "Medium", "doctor": "Dr. Sneha Iyer"},
    "dry cough": {"specialization": "Pulmonology", "priority": "Medium", "doctor": "Dr. Sneha Iyer"},
    "chronic cough": {"specialization": "Pulmonology", "priority": "High", "doctor": "Dr. Sneha Iyer"},
    "wheezing": {"specialization": "Pulmonology", "priority": "High", "doctor": "Dr. Sneha Iyer"},
    "asthma": {"specialization": "Pulmonology", "priority": "High", "doctor": "Dr. Sneha Iyer"},
    "breathing difficulty": {"specialization": "Pulmonology", "priority": "High", "doctor": "Dr. Sneha Iyer"},
    "lung infection": {"specialization": "Pulmonology", "priority": "High", "doctor": "Dr. Sneha Iyer"},

    "fever": {"specialization": "General", "priority": "Medium", "doctor": "Dr. Priya Sharma"},
    "high fever": {"specialization": "General", "priority": "High", "doctor": "Dr. Priya Sharma"},
    "cold": {"specialization": "General", "priority": "Low", "doctor": "Dr. Priya Sharma"},
    "body pain": {"specialization": "General", "priority": "Low", "doctor": "Dr. Priya Sharma"},
    "fatigue": {"specialization": "General", "priority": "Low", "doctor": "Dr. Priya Sharma"},
    "weakness": {"specialization": "General", "priority": "Low", "doctor": "Dr. Priya Sharma"},
    "chills": {"specialization": "General", "priority": "Low", "doctor": "Dr. Priya Sharma"},
    "viral infection": {"specialization": "General", "priority": "Medium", "doctor": "Dr. Priya Sharma"},
    "flu": {"specialization": "General", "priority": "Medium", "doctor": "Dr. Priya Sharma"},

    "stomach pain": {"specialization": "Gastroenterology", "priority": "Medium", "doctor": "Dr. Rahul Das"},
    "abdominal pain": {"specialization": "Gastroenterology", "priority": "Medium", "doctor": "Dr. Rahul Das"},
    "vomiting": {"specialization": "Gastroenterology", "priority": "Medium", "doctor": "Dr. Rahul Das"},
    "nausea": {"specialization": "Gastroenterology", "priority": "Medium", "doctor": "Dr. Rahul Das"},
    "diarrhea": {"specialization": "Gastroenterology", "priority": "Medium", "doctor": "Dr. Rahul Das"},
    "gas": {"specialization": "Gastroenterology", "priority": "Low", "doctor": "Dr. Rahul Das"},
    "acid reflux": {"specialization": "Gastroenterology", "priority": "Low", "doctor": "Dr. Rahul Das"},
    "constipation": {"specialization": "Gastroenterology", "priority": "Low", "doctor": "Dr. Rahul Das"},
    "food poisoning": {"specialization": "Gastroenterology", "priority": "High", "doctor": "Dr. Rahul Das"},

    "skin rash": {"specialization": "Dermatology", "priority": "Low", "doctor": "Dr. Ananya Das"},
    "itching": {"specialization": "Dermatology", "priority": "Low", "doctor": "Dr. Ananya Das"},
    "allergy": {"specialization": "Dermatology", "priority": "Low", "doctor": "Dr. Ananya Das"},
    "eczema": {"specialization": "Dermatology", "priority": "Low", "doctor": "Dr. Ananya Das"},
    "psoriasis": {"specialization": "Dermatology", "priority": "Low", "doctor": "Dr. Ananya Das"},
    "acne": {"specialization": "Dermatology", "priority": "Low", "doctor": "Dr. Ananya Das"},
    "redness": {"specialization": "Dermatology", "priority": "Low", "doctor": "Dr. Ananya Das"},
    "skin infection": {"specialization": "Dermatology", "priority": "Medium", "doctor": "Dr. Ananya Das"},

    "joint pain": {"specialization": "Orthopedics", "priority": "Medium", "doctor": "Dr. Vikram Reddy"},
    "knee pain": {"specialization": "Orthopedics", "priority": "Medium", "doctor": "Dr. Vikram Reddy"},
    "back pain": {"specialization": "Orthopedics", "priority": "Medium", "doctor": "Dr. Vikram Reddy"},
    "fracture": {"specialization": "Orthopedics", "priority": "High", "doctor": "Dr. Vikram Reddy"},
    "swelling": {"specialization": "Orthopedics", "priority": "Medium", "doctor": "Dr. Vikram Reddy"},
    "muscle pain": {"specialization": "Orthopedics", "priority": "Low", "doctor": "Dr. Vikram Reddy"},
    "arthritis": {"specialization": "Orthopedics", "priority": "Medium", "doctor": "Dr. Vikram Reddy"},

    "eye pain": {"specialization": "Ophthalmology", "priority": "Medium", "doctor": "Dr. Meera Nair"},
    "eye redness": {"specialization": "Ophthalmology", "priority": "Low", "doctor": "Dr. Meera Nair"},
    "watering eyes": {"specialization": "Ophthalmology", "priority": "Low", "doctor": "Dr. Meera Nair"},
    "vision loss": {"specialization": "Ophthalmology", "priority": "High", "doctor": "Dr. Meera Nair"}
}

# AI FUNCTIONS (UNCHANGED)
def ai_priority(symptoms, age):
    symptoms = symptoms.lower()
    priority = "Low"
    doctor = "General"

    for key in SYMPTOM_RULES:
        if key in symptoms:
            rule = SYMPTOM_RULES[key]
            priority = rule["priority"]
            doctor = rule["doctor"]
            break

    if age > 60 and priority != "High":
        priority = "High"

    return priority, doctor


def ai_suggestion(symptoms):
    symptoms = symptoms.lower()

    if any(x in symptoms for x in ["accident","bleeding","burn","poisoning","snake","unconscious"]):
        return "🚨 Emergency: Stabilize patient, control bleeding, IV fluids, immediate monitoring."
    elif any(x in symptoms for x in ["chest pain","breathing","palpitations"]):
        return "❤️ Cardiac alert: Perform ECG, monitor BP, give aspirin if required."
    elif any(x in symptoms for x in ["headache","seizures","numbness","dizziness"]):
        return "🧠 Neurological check: CT/MRI if severe."
    elif any(x in symptoms for x in ["cough","asthma","breathing difficulty"]):
        return "🫁 Check oxygen levels, nebulization."
    elif any(x in symptoms for x in ["fever","cold"]):
        return "🌡️ Paracetamol, hydration."
    else:
        return "🩺 General diagnosis required."


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/booking", methods=["GET", "POST"])
def booking():
    if request.method == "POST":
        data = request.get_json()

        if not data.get("payment_done"):
            return jsonify({"status": "error", "message": "Payment not completed ❌"})

        priority, doctor = ai_priority(data["symptoms"], int(data["age"]))
        suggestion = ai_suggestion(data["symptoms"])

        conn = get_connection()
        conn.execute("""
        INSERT INTO patients (name, age, symptoms, priority, doctor, suggestion, prescription, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data["name"], data["age"], data["symptoms"],
            priority, doctor, suggestion, "", "Waiting"
        ))

        conn.commit()
        conn.close()

        return jsonify({"status": "success"})

    return render_template("booking.html")


@app.route("/doctor-login", methods=["GET", "POST"])
def doctor_login():
    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip().lower()
        password = request.form.get("password", "").strip()
        if username == "doctor" and password == "1234":
            return redirect(url_for("doctor_dashboard"))
        error = "Invalid username or password ❌"
    return render_template("doctor_login.html", error=error)


@app.route("/doctor")
def doctor_dashboard():
    conn = get_connection()
    patients = conn.execute("SELECT * FROM patients").fetchall()
    conn.close()
    return render_template("doctor_dashboard.html", patients=patients)


@app.route("/add_prescription/<int:id>", methods=["POST"])
def add_prescription(id):
    prescription = request.form["prescription"]

    conn = get_connection()
    conn.execute("""
        UPDATE patients
        SET prescription = ?, status = 'Completed'
        WHERE id = ?
    """, (prescription, id))

    conn.commit()
    conn.close()

    return redirect(url_for("doctor_dashboard"))

@app.route("/download/<int:id>")
def download_pdf(id):
    conn = get_connection()
    patient = conn.execute("SELECT * FROM patients WHERE id = ?", (id,)).fetchone()
    conn.close()

    if not patient:
        return "Patient not found ❌"

    pdf = FPDF()
    pdf.add_page()

    # 🏥 LOGO
    pdf.image("logo.png", x=10, y=8, w=30)

    # 🏥 HOSPITAL NAME
    pdf.set_font("Arial", "B", 18)
    pdf.cell(200, 10, "FirstCare AI Hospital", ln=True, align="C")

    pdf.ln(10)

    # 📄 PATIENT DETAILS
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 10, f"Patient Name: {patient['name']}", ln=True)
    pdf.cell(200, 10, f"Age: {patient['age']}", ln=True)
    pdf.cell(200, 10, f"Symptoms: {patient['symptoms']}", ln=True)
    pdf.cell(200, 10, f"Doctor: {patient['doctor']}", ln=True)
    pdf.cell(200, 10, f"Priority: {patient['priority']}", ln=True)

    pdf.ln(10)

    # 💊 PRESCRIPTION BOX
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, "Prescription:", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, patient['prescription'])

    pdf.ln(20)

    # ✍️ SIGNATURE
    pdf.cell(200, 10, "__________________________", ln=True, align="R")
    pdf.cell(200, 10, f"{patient['doctor']}", ln=True, align="R")
    pdf.cell(200, 10, "Authorized Doctor Signature", ln=True, align="R")

    file_path = f"prescription_{id}.pdf"
    pdf.output(file_path)

    return send_file(file_path, as_attachment=True)


@app.route("/history")
def history_page():
    return render_template("history.html", history=history)


if __name__ == "__main__":
    app.run(debug=True)

@app.route("/clear")
def clear_data():
    conn = get_connection()
    conn.execute("DELETE FROM patients")
    conn.commit()
    conn.close()
    return "All data cleared"