import streamlit as st
from questions import SENSORY,MOTOR,AUTONOMIC,FUNCTIONAL

st.set_page_config(page_title="ASCLEPIUS.AI", page_icon="🧬", layout="centered")


st.title("🧬 ASCLEPIUS")
st.write("")
st.text("clinical tool to estimate the risk of diabetic neuropathy in patients with diabetes")
st.subheader("Kindly respond to the following clinical assessment")


feature_dict = {
    "Sensory":SENSORY,
    "Motor":MOTOR, 
    "Autonomic":AUTONOMIC,
    "Functional":FUNCTIONAL 
    }

question_vector = 0 
is_unanswered = False
total_question = 40
for key,value in feature_dict.items():
    st.write("")
    st.markdown(f"<span style='font-size:25px; font-weight:800'>🩺 {key}</span>", unsafe_allow_html=True)
    for i,q in enumerate(value):
        st.markdown(f"<span style='font-size:18px; font-weight:600'>{i+1}. {q}</span>", unsafe_allow_html=True)
        answer = st.radio("", ["Yes","No"],index=None, key=f"f_{key}_q{i}")
        if answer is None:
            is_unanswered = True
        else:
            if answer == "Yes":
               question_vector+=1 
            total_question-=1

        st.markdown("---")
        


        
if st.button("**Initiate diagnostic evaluation 🔬**"): 
    

    if not is_unanswered:
        st.subheader("🧾 Assessment Result:")
        if question_vector <= 15:
           st.success("**Very Low 🙂 – Very unlikely to develop neuropathy**")
        elif question_vector >= 16 and question_vector <= 30:
           st.success("**Low 🤏 – Low risk, but worth routine monitoring**")
        elif question_vector >=31 and question_vector <= 50:
            st.warning("**Moderate 😐 – Moderate risk, manage blood sugar closely**")
        elif question_vector >=51 and question_vector <= 75:
            st.error("**High ⚠️ – High risk, proactive measures needed**")
        else:
            st.error("**Very High ☠️ – Very likely without urgent intervention**")
    else:
        st.info(f"**Please complete all fields to ensure a clear diagnosis 🥼 {total_question} questions unanswered**")
   