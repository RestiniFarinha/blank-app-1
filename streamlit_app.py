import streamlit as st

# Homepage function for selecting the phase of management
def homepage():
    st.title("MUHC Breast Cancer Treatment Guidelines")
    st.write("Please select the phase of patient management:")

    # User selects one of the phases
    phase = st.selectbox("Which phase are you in?", ["Select", "Radiology", "Surgery", "Radiotherapy"])

    # Button to proceed after selection
    if st.button("Proceed"):
        # Redirect based on the selection
        if phase == "Radiology":
            st.session_state['page'] = 'radiology'
        elif phase == "Surgery":
            st.session_state['page'] = 'surgery'
        elif phase == "Radiotherapy":
            st.session_state['page'] = 'radiotherapy'
        else:
            st.warning("Please select a valid phase.")

# Radiology phase
def radiology_page():
    st.header("Welcome to the Radiology Phase")
    st.write("Please select the protocol you are working on:")

    # User selects the protocol
    protocol = st.selectbox(
        "Select the protocol:",
        ["Select", "Microcalcifications BiRADS 4 or 5", "Lesion visible on U/S BiRADS 4 or 5", "Palpable breast lesion BiRADS 5"]
    )

    # Show additional input fields based on protocol selection
    if protocol == "Microcalcifications BiRADS 4 or 5":
        show_microcalcifications_protocol()
    elif protocol == "Lesion visible on U/S BiRADS 4 or 5":
        show_us_lesion_protocol()
    elif protocol == "Palpable breast lesion BiRADS 5":
        show_palpable_lesion_protocol()

# Microcalcifications protocol inputs and recommendation
def show_microcalcifications_protocol():
    st.subheader("Microcalcifications BiRADS 4 or 5 Protocol")
    
    # Inputs related to Microcalcifications protocol
    histologic_diagnosis = st.selectbox(
        "Select the histologic diagnosis:",
        ["Benign lesion", "Atypical lobular hyperplasia", "ADH or malignant lesion"]
    )

    # Check radiologic-pathologic concordance for benign lesions
    concordance = None
    if histologic_diagnosis == "Benign lesion":
        concordance = st.selectbox(
            "Is there radiologic-pathologic concordance?",
            ["Yes", "No"]
        )

    # Button to get management recommendation
    if st.button("Get Management Recommendation"):
        recommendation = get_microcalcifications_recommendation(histologic_diagnosis, concordance)
        st.write(f"**Management Recommendation:** {recommendation}")
        
        # Provide a link to open the guideline image in a new tab
        st.write("**Note**: You can view the full guideline for Microcalcifications BiRADS 4 or 5 by [clicking here](https://raw.githubusercontent.com/RestiniFarinha/blank-app-1/main/Radiologic approach: Palpable breast lesions BiRADS 5).")

# Lesion visible on U/S protocol inputs and recommendation
def show_us_lesion_protocol():
    st.subheader("Lesion visible on U/S BiRADS 4 or 5 Protocol")
    
    # Inputs related to U/S Lesion protocol
    histologic_diagnosis = st.selectbox(
        "Select the histologic diagnosis:",
        ["Benign lesion", "Atypical or malignant lesion"]
    )

    # Button to get management recommendation
    if st.button("Get Management Recommendation"):
        recommendation = get_us_lesion_recommendation(histologic_diagnosis)
        st.write(f"**Management Recommendation:** {recommendation}")
        
        # Provide a link to open the same guideline image in a new tab
        st.write("**Note**: You can view the full guideline for Lesion visible on U/S BiRADS 4 or 5 by [clicking here](https://raw.githubusercontent.com/RestiniFarinha/blank-app-1/main/Radiologic approach: Palpable breast lesions BiRADS 5).")

# Palpable breast lesion protocol inputs and recommendation
def show_palpable_lesion_protocol():
    st.subheader("Palpable breast lesion BiRADS 5 Protocol")
    
    # Inputs related to Palpable Lesion protocol
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

    # Button to get management recommendation
    if st.button("Get Management Recommendation"):
        recommendation = get_palpable_lesion_recommendation(histologic_diagnosis, neoadjuvant_planned)
        st.write(f"**Management Recommendation:** {recommendation}")
        
        # Provide a link to open a different guideline image in a new tab
        st.write("**Note**: You can view the full guideline for Palpable breast lesion BiRADS 5 by [clicking here](https://raw.githubusercontent.com/RestiniFarinha/blank-app-1/main/Radiologic approach: Subclinical lesions).")

# Functions to get the recommendations based on user inputs
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
        st.write("Surgery Page")  # Placeholder for surgery page
    elif st.session_state['page'] == 'radiotherapy':
        st.write("Radiotherapy Page")  # Placeholder for radiotherapy page

if __name__ == "__main__":
    main()

########################################################################################

import streamlit as st

# Homepage function for selecting the phase of management
def homepage():
    st.title("MUHC Breast Cancer Treatment Guidelines")
    st.write("Please select the phase of patient management:")

    # User selects one of the phases
    phase = st.selectbox("Which phase are you in?", ["Select", "Radiology", "Surgery", "Radiotherapy"])

    # Button to proceed after selection
    if st.button("Proceed"):
        # Redirect based on the selection
        if phase == "Radiology":
            st.session_state['page'] = 'radiology'
        elif phase == "Surgery":
            st.session_state['page'] = 'surgery'
        elif phase == "Radiotherapy":
            st.session_state['page'] = 'radiotherapy'
        else:
            st.warning("Please select a valid phase.")

# Radiology phase remains unchanged
# Surgery phase

import streamlit as st

# Homepage function for selecting the phase of management
def homepage():
    st.title("MUHC Breast Cancer Treatment Guidelines")
    st.write("Please select the phase of patient management:")

    # User selects one of the phases
    phase = st.selectbox("Which phase are you in?", ["Select", "Radiology", "Surgery", "Radiotherapy"])

    # Button to proceed after selection
    if st.button("Proceed"):
        # Redirect based on the selection
        if phase == "Radiology":
            st.session_state['page'] = 'radiology'
        elif phase == "Surgery":
            st.session_state['page'] = 'surgery'
        elif phase == "Radiotherapy":
            st.session_state['page'] = 'radiotherapy'
        else:
            st.warning("Please select a valid phase.")

# Surgery phase
def surgery_page():
    st.header("Welcome to the Surgery Phase")
    st.write("Please select the surgery protocol you are working on:")

    protocol = st.selectbox(
        "Select the surgery protocol:",
        ["Select", "Eligible for Neoadjuvant Therapy", "Breast Conservative Surgery", "Mastectomy"]
    )

    if protocol == "Eligible for Neoadjuvant Therapy":
        show_neoadjuvant_protocol()
    elif protocol == "Breast Conservative Surgery":
        show_breast_conservative_protocol()
    elif protocol == "Mastectomy":
        show_mastectomy_protocol()

# Neoadjuvant protocol inputs and recommendation (remains unchanged)

# Breast Conservative Surgery protocol
def show_breast_conservative_protocol():
    st.subheader("Breast Conservative Surgery Protocol")
    
    # User selects the status of the margins
    margins_status = st.selectbox("Are the margins negative?", ["Yes", "No"])

    # Only ask for margin revision if margins are negative
    margin_revision = None
    if margins_status == "No":
        margin_revision = st.selectbox("Is margin revision by BCS possible?", ["Yes", "No"])

    # Button to get management recommendation
    if st.button("Get Management Recommendation"):
        recommendation = get_breast_conservative_recommendation(margins_status, margin_revision)
        st.write(f"**Management Recommendation:** {recommendation}")

# Function to get the recommendation for breast-conserving surgery
def get_breast_conservative_recommendation(margins_status, margin_revision):
    if margins_status == "Yes":
        return "No further breast surgery required."
    elif margins_status == "No":
        if margin_revision == "Yes":
            return "Recommend margin revision."
        else:
            return "Mastectomy recommended."
    else:
        return "No specific recommendation available."

# Mastectomy protocol inputs and recommendation (remains unchanged)

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
        st.write("Radiotherapy Page")  # Placeholder for radiotherapy page

if __name__ == "__main__":
    main()
