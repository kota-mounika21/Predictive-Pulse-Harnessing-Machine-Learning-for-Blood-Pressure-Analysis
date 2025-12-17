<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hypertension Detection | Professional Health Assessment</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
    
    <style>
        /* --- 1. CSS VARIABLES (From your snippet) --- */
        :root {
            --primary-medical: #0052CC;
            --secondary-medical: #E8F4FD;
            --success-medical: #10B981;
            --warning-medical: #F59E0B;
            --danger-medical: #EF4444;
            --info-medical: #3B82F6;
            --neutral-gray: #64748B;
            --light-bg: #F8FAFC;
            --white: #FFFFFF;
            --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        }

        /* --- 2. GLOBAL RESET --- */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #f0f4ff 0%, #e0e7ff 100%);
            min-height: 100vh;
            color: #1e293b;
            padding-bottom: 50px;
        }

        /* --- 3. HEADER --- */
        .medical-header {
            background: linear-gradient(135deg, var(--primary-medical) 0%, #1b783a 100%);
            color: white;
            padding: 2rem 0;
            box-shadow: var(--shadow-lg);
            margin-bottom: 2rem;
            text-align: center;
        }
        
        .medical-header h1 {
            font-family: 'Playfair Display', serif;
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }
        
        .medical-header p {
            opacity: 0.9;
            font-size: 1.1rem;
        }

        /* --- 4. CONTAINER & LAYOUT --- */
        .container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .card {
            background: var(--white);
            border-radius: 16px;
            box-shadow: var(--shadow-md);
            padding: 2rem;
            margin-bottom: 2rem;
            border-top: 5px solid var(--primary-medical);
        }

        /* --- 5. FORM GRID SYSTEM --- */
        .form-section-title {
            color: var(--primary-medical);
            font-size: 1.25rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 10px;
            border-bottom: 2px solid var(--secondary-medical);
            padding-bottom: 10px;
        }

        .form-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }

        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
            color: #334155;
            font-size: 0.9rem;
        }

        .form-control {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            font-size: 1rem;
            transition: all 0.3s ease;
            background-color: #f8fafc;
        }

        .form-control:focus {
            outline: none;
            border-color: var(--primary-medical);
            box-shadow: 0 0 0 3px rgba(0, 82, 204, 0.1);
            background-color: white;
        }

        /* --- 6. BUTTONS --- */
        .btn-medical {
            background: var(--primary-medical);
            color: white;
            padding: 1rem 2rem;
            border: none;
            border-radius: 8px;
            font-size: 1.1rem;
            font-weight: 600;
            cursor: pointer;
            width: 100%;
            transition: transform 0.2s, box-shadow 0.2s;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10px;
        }

        .btn-medical:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
            background: #137213;
        }

        /* --- 7. ALERTS & RESULTS --- */
        .alert {
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 1.5rem;
            font-weight: 500;
        }
        .alert-error { background: #fee2e2; color: #991b1b; border: 1px solid #fecaca; }
        .alert-info { background: #e0f2fe; color: #0e7554; border: 1px solid #7dd478; }

        /* Results Section Styling */
        #result-section {
            scroll-margin-top: 2rem;
        }
        
        .result-header {
            text-align: center;
            padding: 2rem;
            border-radius: 12px;
            color: white;
            margin-bottom: 2rem;
        }

        .recommendation-list {
            list-style: none;
        }
        
        .recommendation-list li {
            position: relative;
            padding-left: 30px;
            margin-bottom: 12px;
            font-size: 1.05rem;
            color: #334155;
        }
        
        .recommendation-list li::before {
            content: "✓";
            position: absolute;
            left: 0;
            color: var(--success-medical);
            font-weight: bold;
        }

    </style>
</head>
<body>

    <header class="medical-header">
        <div class="container">
            <h1>CardioGuard AI</h1>
            <p>Advanced Hypertension Risk Assessment System</p>
        </div>
    </header>

    <div class="container">
        
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">
                        <i class="fas fa-info-circle"></i> {{ message }}
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        {% if prediction_text %}
        <div id="result-section" class="card">
            <div class="result-header" style="background-color: {{ result_color }};">
                <h3>Assessment Complete</h3>
                <h1 style="font-size: 2.5rem; margin: 10px 0;">{{ prediction_text }}</h1>
                <p><i class="fas fa-chart-line"></i> AI Confidence Score: <strong>{{ confidence }}%</strong></p>
            </div>

            <div class="form-grid">
                <div style="grid-column: span 2;">
                    <h3 class="form-section-title"><i class="fas fa-user-md"></i> Clinical Interpretation</h3>
                    <p style="font-size: 1.1rem; margin-bottom: 1.5rem;">
                        <strong>Status:</strong> {{ recommendation.priority }}<br>
                        {{ recommendation.description }}
                    </p>
                    
                    <h4 style="margin-bottom: 1rem; color: #334155;">Recommended Actions:</h4>
                    <ul class="recommendation-list">
                        {% for action in recommendation.actions %}
                            <li>{{ action }}</li>
                        {% endfor %}
                    </ul>
                </div>
            </div>
            
            <div style="text-align: center;">
                <a href="/" class="btn-medical" style="background-color: var(--neutral-gray); display: inline-flex; width: auto;">
                    <i class="fas fa-redo"></i> Perform New Assessment
                </a>
            </div>
        </div>
        {% endif %}


        <div class="card">
            <form action="/predict" method="POST">
                
                <h3 class="form-section-title">Patient Demographics</h3>
                <div class="form-grid">
                    <div class="form-group">
                        <label>Gender</label>
                        <select name="Gender" class="form-control" required>
                            <option value="" disabled selected>Select Gender</option>
                            <option value="Male" {% if form_data and form_data['Gender'] == 'Male' %}selected{% endif %}>Male</option>
                            <option value="Female" {% if form_data and form_data['Gender'] == 'Female' %}selected{% endif %}>Female</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Age Group</label>
                        <select name="Age" class="form-control" required>
                            <option value="" disabled selected>Select Age Group</option>
                            <option value="18-34" {% if form_data and form_data['Age'] == '18-34' %}selected{% endif %}>18-34 Years</option>
                            <option value="35-50" {% if form_data and form_data['Age'] == '35-50' %}selected{% endif %}>35-50 Years</option>
                            <option value="51-64" {% if form_data and form_data['Age'] == '51-64' %}selected{% endif %}>51-64 Years</option>
                            <option value="65+" {% if form_data and form_data['Age'] == '65+' %}selected{% endif %}>65+ Years</option>
                        </select>
                    </div>
                </div>

                <h3 class="form-section-title"> Medical History</h3>
                <div class="form-grid">
                    <div class="form-group">
                        <label>Family History of Hypertension?</label>
                        <select name="History" class="form-control" required>
                            <option value="Yes" {% if form_data and form_data['History'] == 'Yes' %}selected{% endif %}>Yes</option>
                            <option value="No" {% if form_data and form_data['History'] == 'No' %}selected{% endif %}>No</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Currently a Patient?</label>
                        <select name="Patient" class="form-control" required>
                            <option value="Yes" {% if form_data and form_data['Patient'] == 'Yes' %}selected{% endif %}>Yes</option>
                            <option value="No" {% if form_data and form_data['Patient'] == 'No' %}selected{% endif %}>No</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Currently Taking Medication?</label>
                        <select name="TakeMedication" class="form-control" required>
                            <option value="Yes" {% if form_data and form_data['TakeMedication'] == 'Yes' %}selected{% endif %}>Yes</option>
                            <option value="No" {% if form_data and form_data['TakeMedication'] == 'No' %}selected{% endif %}>No</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Time Since Diagnosis</label>
                        <select name="Whendiagnoused" class="form-control" required>
                            <option value="<1 Year" {% if form_data and form_data['Whendiagnoused'] == '<1 Year' %}selected{% endif %}>Less than 1 Year</option>
                            <option value="1-5 Years" {% if form_data and form_data['Whendiagnoused'] == '1-5 Years' %}selected{% endif %}>1 - 5 Years</option>
                            <option value=">5 Years" {% if form_data and form_data['Whendiagnoused'] == '>5 Years' %}selected{% endif %}>More than 5 Years</option>
                        </select>
                    </div>
                </div>

                <h3 class="form-section-title"> Clinical Symptoms</h3>
                <div class="form-grid">
                    <div class="form-group">
                        <label>Symptom Severity</label>
                        <select name="Severity" class="form-control" required>
                            <option value="Mild" {% if form_data and form_data['Severity'] == 'Mild' %}selected{% endif %}>Mild</option>
                            <option value="Moderate" {% if form_data and form_data['Severity'] == 'Moderate' %}selected{% endif %}>Moderate</option>
                            <option value="Severe" {% if form_data and form_data['Severity'] == 'Severe' %}selected{% endif %}>Severe</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Shortness of Breath?</label>
                        <select name="BreathShortness" class="form-control" required>
                            <option value="No">No</option>
                            <option value="Yes">Yes</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Visual Changes?</label>
                        <select name="VisualChanges" class="form-control" required>
                            <option value="No">No</option>
                            <option value="Yes">Yes</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Nose Bleeding?</label>
                        <select name="NoseBleeding" class="form-control" required>
                            <option value="No">No</option>
                            <option value="Yes">Yes</option>
                        </select>
                    </div>
                </div>

                <h3 class="form-section-title"> Vitals & Lifestyle</h3>
                <div class="form-grid">
                    <div class="form-group">
                        <label>Systolic BP (Upper Range)</label>
                        <select name="Systolic" class="form-control" required>
                            <option value="100 - 110">100 - 110 mmHg</option>
                            <option value="111 - 120">111 - 120 mmHg</option>
                            <option value="121 - 130">121 - 130 mmHg</option>
                            <option value="130+">130+ mmHg</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Diastolic BP (Lower Range)</label>
                        <select name="Diastolic" class="form-control" required>
                            <option value="70 - 80">70 - 80 mmHg</option>
                            <option value="81 - 90">81 - 90 mmHg</option>
                            <option value="91 - 100">91 - 100 mmHg</option>
                            <option value="100+">100+ mmHg</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Follows Controlled Diet?</label>
                        <select name="ControlledDiet" class="form-control" required>
                            <option value="Yes">Yes</option>
                            <option value="No">No</option>
                        </select>
                    </div>
                </div>

                <button type="submit" class="btn-medical">
                    <i class="fas fa-stethoscope"></i> Analyze Patient Data
                </button>

            </form>
        </div>
    </div>

    {% if prediction_text %}
    <script>
        document.getElementById('result-section').scrollIntoView({ behavior: 'smooth' });
    </script>
    {% endif %}

</body>
</html>
