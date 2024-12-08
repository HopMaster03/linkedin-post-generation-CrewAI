import os
import numpy as np
import streamlit as st
from langtrace_python_sdk import langtrace
from crew import LinkedInPostCrew

from streamlit_pdf_reader import pdf_reader
from dotenv import load_dotenv

load_dotenv() # take environment variables from .env.
langtrace.init(api_key = os.getenv("LANGTRACE_API_KEY"))

st.title("Crew AI LinkedIn Post Generator")

#Form opening
with st.form(key='my-form'):
    organization_name = st.text_input("Enter your Orgnanization or Individuals name: ")
    read_pdf = st.file_uploader("Upload a PDF with Context of the Organization",type=['PDF'])
    organization_context=""
    org_or_person= st.radio(
        "Are you an Organization or an individual?",["Organization","Individual"]
    )      
    organization_username = st.text_input("Pass linkedIn username to get the posts for example: ")
    col1,col2 = st.columns(2)
    with col1:
        emotional_appeal= st.selectbox(
            "What is the emotional appeal for the post: ",
            ("Inspiration", "Empathy", "Surprise", "Pride", "Humour"))
    with col2:
        type_of_post= st.selectbox(
            "Select the type of post: ",
            ("Text only Post", "Event Post", "NewsLetter Post", "Job Post", "Product Post","Thought Leadership Post",
             "Company News Post","Ask me anything Post","Reaction Post","Comparision Post","Behind the Scene Post","Quote Post"))
    emotional_appeal_post = st.text_area("Pass the data of the post which emulates a similar emotional appeal ")
    topic_of_interest= st.text_area("What do you want to talk about?")
    target_audience= st.text_area("Who are your target audience?")
    generate_button = st.form_submit_button("Generate")

    if generate_button:
        if read_pdf:
            organization_context = pdf_reader(read_pdf)
        if org_or_person=="Organization":
            orglink=1
        else:
            orglink=0
        input={
            'organization_name':organization_name,
            'organization_context':organization_context,
            'linkedin_username':organization_username,
            'orglink':orglink,
            'emotional_appeal':emotional_appeal,
            'type_of_post':type_of_post,
            'reference_post':emotional_appeal_post,
            'topic_of_interest':topic_of_interest,
            'target_audience':target_audience,
            }
        result = LinkedInPostCrew().crew().kickoff(inputs=input)
        st.write(result)

        
