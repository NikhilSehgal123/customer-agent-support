import os
import openai
import streamlit as st
import dotenv

dotenv.load_dotenv()

prompt = """
You are a customer support agent and your role is to categorise the incoming request into one of the following categories:
- Password Reset
- Mobile Phone Issue
- Hardware Fault
- Software Fault
- Application Fault
- Access Issue
- Onboarding Issue
- Calendar Access Request
- Service Request
- Onsite Support Request
- Remote Support Request
- Data Deletion

Incoming Request: {}
Response:
"""

prompt_respond = """
You are a customer support agent and are responding to a request from a customer. The customer has requested the following. Your job is to respond with an appropriate resolution based on the category and the message.
Please ask the customer to provide more information if you are unsure of the request until the request is clear.

Incoming Request Category: {}
Incoming Request Message: {}
Response:
"""

# openai.api_key = os.getenv("OPENAI_API_KEY")

# Load the API key from the .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":

    st.title('Customer Support Agent')
  
    # Ask the user to input a request in a streamlit text box
    input_request = st.text_input('Enter a request:')

    if st.button('Submit'):
        st.write('You submitted:', input_request)

        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt.format(input_request),
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

        # Write the response to the streamlit app
        st.write('Here is the categorisation:')
        st.write(response.choices[0].text)
        
        category = response.choices[0].text

        generated_response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt_respond.format(category, input_request),
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

        # Generate a resolution to the request
        st.write('Here is the resolution:')
        st.write(generated_response.choices[0].text)
