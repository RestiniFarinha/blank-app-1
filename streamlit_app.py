import streamlit as st

# Homepage function for selecting the phase of management
def homepage():
    st.title("MUHC Breast Cancer Treatment Guidelines")
    st.write("Please select the phase of patient management:")

    # User selects one of the phases
    phase = st.selectbox("Which phase are you in?", ["Select", "Radiology", "Surgery", "Radiotherapy", "DCIS"])

    # Button to proceed after selection
    if st.button("Proceed"):
        # Redirect based on the selection
        if phase == "Radiology":
            st.session_state['page'] = 'radiology'
        elif phase == "Surgery":
            st.session_state['page'] = 'surgery'
        elif phase == "Radiotherapy":
            st.session_state['page'] = 'radiotherapy'
        elif phase == "DCIS":
            st.session_state['page'] = 'dcis'
        else:
            st.warning("Please select a valid phase.")

# Radiology phase
def radiology_page():
    st.header("Welcome to the Radiology Phase")
    st.write("Please select the protocol you are working on:")

    protocol = st.selectbox(
        "Select the protocol:",
        ["Select", "Microcalcifications BiRADS 4 or 5", "Lesion visible on U/S BiRADS 4 or 5", "Palpable breast lesion BiRADS 5"]
    )

    if protocol == "Microcalcifications BiRADS 4 or 5":
        show_microcalcifications_protocol()
    elif protocol == "Lesion visible on U/S BiRADS 4 or 5":
        show_us_lesion_protocol()
    elif protocol == "Palpable breast lesion BiRADS 5":
        show_palpable_lesion_protocol()

# Surgery phase
def surgery_page():
    st.header("Welcome to the Surgery Phase")
    st.write("Please select the surgery type you are working on:")

    surgery_type = st.selectbox(
        "Select the surgery type:",
        ["Select", "Breast conserving surgery", "Upfront mastectomy"]
    )

    if surgery_type == "Breast conserving surgery":
        show_breast_conserving_surgery()
    elif surgery_type == "Upfront mastectomy":
        show_upfront_mastectomy()

# Radiotherapy phase
def radiotherapy_page():
    st.header("Welcome to the Radiotherapy Phase")
    st.write("Please select the radiotherapy protocol you are working on:")

    radiotherapy_protocol = st.selectbox(
        "Select the radiotherapy protocol:",
        ["Select", "Radiotherapy for the breast", "Radiotherapy for the chest wall", "Radiotherapy for the regional nodes post-SLNB", "Radiotherapy for the DCIS"]
    )

    if radiotherapy_protocol == "Radiotherapy for the breast":
        show_radiotherapy_breast()
    elif radiotherapy_protocol == "Radiotherapy for the chest wall":
        show_radiotherapy_chest_wall()
    elif radiotherapy_protocol == "Radiotherapy for the regional nodes post-SLNB":
        show_radiotherapy_nodes_slnb()
    elif radiotherapy_protocol == "Radiotherapy for the regional nodes post-ALND":
        show_radiotherapy_alnd()

# Radiology Protocols
def show_microcalcifications_protocol():
    st.subheader("Microcalcifications BiRADS 4 or 5 Protocol")
    
    histologic_diagnosis = st.selectbox(
        "Select the histologic diagnosis:",
        ["Benign lesion", "Atypical lobular hyperplasia", "ADH or malignant lesion"]
    )
    
    concordance = None
    if histologic_diagnosis == "Benign lesion":
        concordance = st.selectbox(
            "Is there radiologic-pathologic concordance?",
            ["Yes", "No"]
        )
    
    if st.button("Get Management Recommendation"):
        recommendation = get_microcalcifications_recommendation(histologic_diagnosis, concordance)
        st.write(f"**Management Recommendation:** {recommendation}")
        st.markdown('[Click here to view the full guideline for Microcalcifications BiRADS 4 or 5](https://raw.githubusercontent.com/RestiniFarinha/blank-app-1/main/radiologic_approach_subclinical_lesions.PNG)')

def show_us_lesion_protocol():
    st.subheader("Lesion visible on U/S BiRADS 4 or 5 Protocol")
    
    histologic_diagnosis = st.selectbox(
        "Select the histologic diagnosis:",
        ["Benign lesion", "Atypical or malignant lesion"]
    )

    if st.button("Get Management Recommendation"):
        recommendation = get_us_lesion_recommendation(histologic_diagnosis)
        st.write(f"**Management Recommendation:** {recommendation}")
        st.markdown('[Click here to view the full guideline for Lesion visible on U/S BiRADS 4 or 5](:https://raw.githubusercontent.com/RestiniFarinha/blank-app-1/main/radiologic_approach_subclinical_lesions.PNG)')

def show_palpable_lesion_protocol():
    st.subheader("Palpable breast lesion BiRADS 5 Protocol")
    
    histologic_diagnosis = st.selectbox(
        "Select the histologic diagnosis:",
        ["Non diagnostic", "Malignant lesion"]
    )

    neoadjuvant_planned = None
    if histologic_diagnosis == "Malignant lesion":
        neoadjuvant_planned = st.selectbox(
            "Is neoadjuvant treatment planned?",
            ["Yes", "No"]
        )

    if st.button("Get Management Recommendation"):
        recommendation = get_palpable_lesion_recommendation(histologic_diagnosis, neoadjuvant_planned)
        st.write(f"**Management Recommendation:** {recommendation}")
        st.markdown('[Click here to view the full guideline for Palpable breast lesion BiRADS 5](https://raw.githubusercontent.com/RestiniFarinha/blank-app-1/main/radiologic_approach_palpable_breast_lesions_BIRADS_5.PNG)')

# Surgery Protocols
def show_breast_conserving_surgery():
    st.subheader("Breast Conserving Surgery Protocol")

    # Display inclusion and exclusion criteria for feasibility
    st.write("""
        **Inclusion Criteria for Upfront Breast Conserving Surgery Feasibility**:
        - Acceptable tumor-to-breast volume ratio?
        - Acceptable tumor location permitting complete excision with negative margins and good cosmesis?

        **Relative Contraindications**:
        - Local recurrence with previous radiotherapy (RT) and not amenable for further RT.

        **Absolute Contraindications**:
        - T4 disease.
        - Multicentric tumor.
        - Radiotherapy contraindicated.
        - Patient preference for mastectomy over breast-conserving surgery (BCS).
        - Prophylactic surgery planned.
    """)

    # Ask the user if upfront breast-conserving surgery is feasible
    feasibility = st.selectbox(
        "Is upfront breast conserving surgery feasible based on the above criteria?",
        ["Feasible", "Non-feasible"]
    )

    if feasibility == "Feasible":
        eligibility = st.selectbox(
            "Is the patient eligible for neoadjuvant systemic therapy?",
            ["Yes", "No"]
        )
        if st.button("Get Management Recommendation"):
            if eligibility == "No":
                recommendation = "Upfront breast conserving surgery."
            else:
                recommendation = "Neoadjuvant systemic therapy followed by breast conserving surgery."
            st.write(f"**Management Recommendation:** {recommendation}")
            st.markdown('[Click here to view the full guideline for Breast Conserving Surgery](https://raw.githubusercontent.com/RestiniFarinha/blank-app-1/main/upfront_bcs.PNG)')
    else:
        neoadjuvant_eligibility = st.selectbox(
            "Is the patient eligible for neoadjuvant systemic therapy?",
            ["Yes", "No"]
        )
        if st.button("Get Management Recommendation"):
            if neoadjuvant_eligibility == "Yes":
                recommendation = "Neoadjuvant systemic therapy followed by breast conserving surgery."
            else:
                recommendation = "Upfront mastectomy with optional reconstruction."
            st.write(f"**Management Recommendation:** {recommendation}")
            st.markdown('[Click here to view the full guideline for Breast Conserving Surgery](https://raw.githubusercontent.com/RestiniFarinha/blank-app-1/main/upfront_bcs.PNG)')
            
    # Section 2: Breast conserving surgery based on margin status
    st.subheader("Margin Status and Breast Conserving Surgery")
    negative_margins = st.selectbox("Are the margins negative at ink?", ["Yes", "No"])
    
    if negative_margins == "Yes":
        st.write("No further breast surgery required.")
        st.markdown('[Click here to view the full guideline for Breast Conserving Surgery](https://raw.githubusercontent.com/RestiniFarinha/blank-app-1/main/upfront_bcs.PNG)')
    else:
        margin_revision_possible = st.selectbox("Is margin revision by BCS possible?", ["Yes", "No"])
        if margin_revision_possible == "Yes":
            st.write("Recommend margin revision.")
        else:
            st.write("Recommend mastectomy. Consider immediate reconstruction if no RT is planned.")
            st.markdown('[Click here to view the full guideline for Breast Conserving Surgery](https://raw.githubusercontent.com/RestiniFarinha/blank-app-1/main/upfront_bcs.PNG)')

    # Section 3: Axillary surgical management
    st.subheader("Axillary Surgical Management")
    cn_ct4_status = st.selectbox("Is the patient cN+ or cT4?", ["Yes", "No"])
    
    if cn_ct4_status == "Yes":
        st.write("Recommend axillary node dissection.")
    else:
        # Check if the patient meets the criteria to omit axillary surgery
        st.write("Check if the patient meets all of the following criteria:")
        age_criteria = st.selectbox("Is the patient age ≥ 70?", ["Yes", "No"])
        size_criteria = st.selectbox("Is the tumor size ≤ 2 cm?", ["Yes", "No"])
        er_positive = st.selectbox("Is the tumor ER+ with planned endocrine therapy?", ["Yes", "No"])
        
        if age_criteria == "Yes" and size_criteria == "Yes" and er_positive == "Yes":
            st.write("Consider omitting axillary surgery.")
        else:
            st.write("Recommend sentinel lymph node biopsy.")
    
    # Provide link to view axillary surgery guidelines
    st.markdown('[Click here to view the full guideline for Breast Conserving Surgery](https://raw.githubusercontent.com/RestiniFarinha/blank-app-1/main/upfront_bcs.PNG)')
def show_upfront_mastectomy():
    st.subheader("Upfront Mastectomy Protocol")
    
    cN0 = st.selectbox(
        "Is the patient cN0?",
        ["Yes", "No"]
    )
    
    frozen_section_positive = None
    if cN0 == "Yes":
        frozen_section_positive = st.selectbox(
            "Is the frozen section positive?",
            ["Yes", "No"]
        )
    
    if st.button("Get Management Recommendation"):
        if cN0 == "Yes":
            if frozen_section_positive == "Yes":
                recommendation = "Completion axillary dissection or modified radical mastectomy."
            else:
                recommendation = "No further axillary surgery."
        else:
            recommendation = "Modified radical mastectomy."
        st.write(f"**Management Recommendation:** {recommendation}")
        st.markdown('[Click here to view the full guideline for Upfront Mastectomy](https://raw.githubusercontent.com/RestiniFarinha/blank-app-1/main/upfront_mastectomy.PNG)')

# Radiotherapy Protocols
def show_radiotherapy_breast():
    st.subheader("Radiotherapy for the Breast Protocol")
    
    all_criteria_met = st.selectbox(
        "Does the patient meet ALL of the following criteria: Age ≥ 40, Total size ≤ 2 cm, Grade I or II, ER positive, pN0?",
        ["Yes", "No"]
    )
    
    margin_1mm = None
    if all_criteria_met == "Yes":
        margin_1mm = st.selectbox(
            "Is the margin ≤ 1 mm?",
            ["Yes", "No"]
        )
    
    if st.button("Get Management Recommendation"):
        if all_criteria_met == "Yes" and margin_1mm == "No":
            recommendation = "APBI 26 Gy in 5 fractions with SIB to 27 Gy."
        elif all_criteria_met == "Yes" and margin_1mm == "Yes":
            recommendation = "Whole breast RT 26 Gy in 5 fractions."
        else:
            recommendation = "Alternative RT approach based on clinical evaluation."
        st.write(f"**Management Recommendation:** {recommendation}")
        st.markdown('[Click here to view the full guideline for Breast Radiotherapy](https://raw.githubusercontent.com/RestiniFarinha/blank-app-1/main/radiotherapy_management_of_breast_invasive_carcinoma.PNG)')

def show_radiotherapy_chest_wall():
    st.subheader("Radiotherapy for the Chest Wall Protocol")
    
    positive_margins = st.selectbox(
        "Are the margins positive?",
        ["Yes", "No"]
    )
    
    if st.button("Get Management Recommendation"):
        if positive_margins == "Yes":
            recommendation = "Chest wall RT with boost, 15 Gy in 6 fractions."
        else:
            recommendation = "Standard RT for chest wall."
        st.write(f"**Management Recommendation:** {recommendation}")
        st.markdown('[Click here to see the full guideline for Chest Wall Radiotherapy.](https://raw.githubusercontent.com/RestiniFarinha/blank-app-1/main/radiotherapy_management_chest_wall.PNG)')


def show_radiotherapy_nodes_slnb():
    st.subheader("Radiotherapy for Regional Nodes post-SLNB Protocol")
    
    node_status = st.selectbox(
        "Node status after SLNB:",
        ["pN0", "pN1mic", "1-2 positive nodes", "≥ 3 positive nodes"]
    )
    
    if st.button("Get Management Recommendation"):
        if node_status == "pN0":
            recommendation = "Nodal irradiation not indicated."
        elif node_status == "pN1mic":
            recommendation = "Consider supraclavicular RT, 40 Gy in 15 fractions."
        elif node_status == "1-2 positive nodes":
            recommendation = "Supraclavicular, axillary, and IMN RT, 40 Gy in 15 fractions."
        else:
            recommendation = "Axillary node dissection."
        st.write(f"**Management Recommendation:** {recommendation}")
        st.markdown('[Click here to see the full guideline for Management of the Regional Nodes Post-SLNB.](https://raw.githubusercontent.com/RestiniFarinha/blank-app-1/main/radiotherapy_after_SLNB.PNG)')

def show_radiotherapy_alnd():
    st.subheader("Radiotherapy - Management of the Regional Nodes Post-ALND")

    # Final pathology options after ALND
    node_status = st.selectbox(
        "Final pathology after ALND:",
        ["pN0", "pN0(i+)", "pN1mic", "pN1 (macrometastases)", "pN2", "pN3"]
    )

    # Add a button for user to click before getting a recommendation
    if st.button("Get Management Recommendation"):
        if node_status in ["pN0", "pN0(i+)", "pN1mic"]:
            st.write("Check if the patient has two of the following factors:")
            grade_iii = st.selectbox("Grade III?", ["Yes", "No"])
            lvi = st.selectbox("Lymphovascular invasion (LVI)?", ["Yes", "No"])
            age_50 = st.selectbox("Age ≤ 50 years?", ["Yes", "No"])
            size_3_cm = st.selectbox("Size ≥ 3 cm?", ["Yes", "No"])
            triple_negative = st.selectbox("Triple negative disease?", ["Yes", "No"])

            # If two or more of these factors are present
            factors = [grade_iii, lvi, age_50, size_3_cm, triple_negative]
            if factors.count("Yes") >= 2:
                st.write("**Recommendation**: Consider supraclavicular RT, 40 Gy in 5 fractions.")
            else:
                st.write("**Recommendation**: Nodal irradiation not indicated.")
                st.markdown('[Click here to view the full guideline for Management of Regional nodes Post-ALND.](https://raw.githubusercontent.com/RestiniFarinha/blank-app-1/main/radiotherapy_after_ALND.PNG)')

        elif node_status in ["pN1 (macrometastases)", "pN2", "pN3"]:
            st.write("Check if the patient has any of the following factors:")
            ece = st.selectbox("Extensive extranodal extension (ECE)?", ["Yes", "No"])
            lymph_nodes_resected = st.selectbox("Less than 8 lymph nodes resected?", ["Yes", "No"])
            nodes_involved = st.selectbox("> 1/2 of nodes involved?", ["Yes", "No"])

            # If any of these factors are present
            if ece == "Yes" or lymph_nodes_resected == "Yes" or nodes_involved == "Yes":
                st.write("**Recommendation**: Supraclavicular and axillary RT, 40 Gy in 5 fractions.")
            else:
                st.write("Check if the patient has any of the following factors:")
                central_tumor = st.selectbox("Central tumor?", ["Yes", "No"])
                medial_tumor = st.selectbox("Medial tumor?", ["Yes", "No"])
                t3_t4 = st.selectbox("T3-4 tumor?", ["Yes", "No"])
                pn2_pn3 = st.selectbox("pN2 or pN3 status?", ["Yes", "No"])

                # If any of these additional factors are present
                if central_tumor == "Yes" or medial_tumor == "Yes" or t3_t4 == "Yes" or pn2_pn3 == "Yes":
                    st.write("**Recommendation**: Supraclavicular, axillary, and IMN RT, 40 Gy in 5 fractions.")
                else:
                    st.write("**Recommendation**: Supraclavicular RT, 40 Gy in 5 fractions.")

            st.markdown('[Click here to view the full guideline for Management of Regional nodes Post-ALND.](https://raw.githubusercontent.com/RestiniFarinha/blank-app-1/main/radiotherapy_after_ALND.PNG)')


# DCIS Protocol
def section_locoregional_dcis_treatment():
    st.header("Locoregional treatment of pure DCIS with or without microinvasion")
    st.write("This section addresses the locoregional treatment options for DCIS with or without microinvasion.")

    # Inputs
    tumor_size = st.number_input('Tumor Size (cm)', min_value=0.0, max_value=10.0, step=0.1)
    tumor_grade = st.selectbox('Tumor Grade', options=["I", "II", "III"])
    age = st.number_input('Patient Age', min_value=18, max_value=100, step=1)
    positive_margin = st.selectbox('Positive Margin?', options=["Yes", "No"])
    num_margins = st.number_input('Number of Margins ≤ 1 mm', min_value=0, max_value=10, step=1)
    localized_dcis = st.selectbox('Localized/Unicentric DCIS?', options=["Yes", "No"])
    margin_revision_feasible = st.selectbox('Margin Revision Feasible?', options=["Yes", "No"])

    # Output
    if st.button('Determine Treatment'):
        treatment = determine_dcis_treatment(tumor_size, tumor_grade, age, positive_margin, num_margins, localized_dcis, margin_revision_feasible)
        st.write(f"The recommended treatment is: {treatment}")
        st.markdown('[Click here to view the full guideline for Management of DCIS.](https://raw.githubusercontent.com/RestiniFarinha/blank-app-1/main/DCIS.PNG)')

# Function to determine treatment for DCIS
def determine_dcis_treatment(tumor_size, tumor_grade, age, positive_margin, num_margins, localized_dcis, margin_revision_feasible):
    if localized_dcis == "No":
        return "Follow recommendations for invasive breast cancer."

    if positive_margin == "Yes":
        if margin_revision_feasible == "Yes":
            return "Margin revision by BCS."
        else:
            return "Simple mastectomy + sentinel node excision without frozen section +/- immediate reconstruction. Radiotherapy is not indicated for positive DCIS margin."

    if num_margins <= 1:
        if tumor_grade == "III" or tumor_size > 2.5 or age < 40:
            return "Discuss at multidisciplinary tumor rounds."

    if tumor_size <= 2 and tumor_grade in ["I", "II"] and age >= 40:
        if num_margins == 1:
            return "Whole breast RT 26 Gy with SIB 30 Gy in 5 fractions (31 Gy for multiple close margins)."
        if num_margins <= 1 and age >= 40:
            if age >= 60 and tumor_size <= 1 and num_margins >= 3:
                return "APBI 26 Gy in 5 fractions with SIB to 27 Gy. Consider omitting radiotherapy, as recurrence rate is 1% per year."
            elif num_margins == 1 and age >= 40:
                return "Whole breast RT 26 Gy in 5 fractions."
            else:
                return "APBI 26 Gy in 5 fractions with SIB to 27 Gy."
    elif num_margins <= 1:
        return "Whole breast RT 26 Gy with SIB 30 Gy in 5 fractions (31 Gy for multiple close margins)."

    return "Based on the input data, follow radiotherapy treatment as per clinical guidance."

# Recommendation logic functions for radiology
def get_microcalcifications_recommendation(histologic_diagnosis, concordance):
    if histologic_diagnosis == "Benign lesion" and concordance == "Yes":
        return "Reclassified as BiRads 2 or 3. Follow-up according to classification."
    elif histologic_diagnosis == "Benign lesion" and concordance == "No":
        return "Repeat imaging. Rebiopsy +/- surgical excision."
    elif histologic_diagnosis == "Atypical lobular hyperplasia":
        return "Follow-up according to radiologic guidelines."
    elif histologic_diagnosis == "ADH or malignant lesion":
        return "Surgical excision."
    else:
        return "No specific recommendation available based on the inputs provided."

def get_us_lesion_recommendation(histologic_diagnosis):
    if histologic_diagnosis == "Benign lesion":
        return "Reclassified as BiRads 2 or 3. Follow-up according to classification."
    elif histologic_diagnosis == "Atypical or malignant lesion":
        return "Surgical excision."
    else:
        return "No specific recommendation available based on the inputs provided."

def get_palpable_lesion_recommendation(histologic_diagnosis, neoadjuvant_planned):
    if histologic_diagnosis == "Non diagnostic":
        return "Repeat biopsy and/or surgical excision."
    elif histologic_diagnosis == "Malignant lesion":
        if neoadjuvant_planned == "Yes":
            return "Neoadjuvant treatment followed by breast MRI."
        else:
            return "Surgical excision."
    else:
        return "No specific recommendation available based on the inputs provided."

# Main function to control navigation
def main():
    # Initialize session state for the page if not already set
    if 'page' not in st.session_state:
        st.session_state['page'] = 'homepage'

    # Redirect to the selected page
    if st.session_state['page'] == 'homepage':
        homepage()
    elif st.session_state['page'] == 'radiology':
        radiology_page()
    elif st.session_state['page'] == 'surgery':
        surgery_page()
    elif st.session_state['page'] == 'radiotherapy':
        radiotherapy_page()
    elif st.session_state['page'] == 'dcis':
        section_locoregional_dcis_treatment()

if __name__ == "__main__":
    main()
