# Streamlit app for code script
import streamlit as st

from subs import CodeIt


class SL_App:

    def __init__(self, _code_it: CodeIt):
        self.code_it = _code_it

    def run(self):
        st.set_page_config(page_title="Secret Message Writer", page_icon="ico.png")

        st.title("Secret Message Writer")
        st.markdown("## Information")
        st.markdown("Click the boxes to enter your information. This page codes and decodes any message you would like it to. Dont forget to follow the instructions above the boxes. :wink: We hope you enjoy this website.")

        st.markdown("## Set up the cypher method.")

        # index_value = st.text_input("Enter an offset value for the substitution:")

        # phrase_value = st.text_input("Enter an alphabet scrambling phrase:")

        multi_index = st.text_input("enter a secret scrambling phrase (long phrases will be very hard to break):")

        new_alphabet = st.text_input("enter your code alphabet ( Needs upercase, lowercase and numbers and don't forget the space e.g. abc[SPACE]defghi...zABCD...Z1234...0)")


        ##### SIDEBAR
        st.sidebar.markdown("## Instructions")
        st.sidebar.markdown("If you have a scrambling phrase and an alphabet it will only use the scrambling phrase so remember to delete that when you want to use an alphabet :thumbsup:")
        st.sidebar.markdown("The scrambling phrase can be anything from 'I' to the longest sentence in the world.")
        st.sidebar.markdown("The app alphabet is 'a..zA..Z0..9[SPACE]' so make sure yours is really different to that.")
        st.sidebar.markdown("If you want to decode something make sure the tickbox is not ticked otherwise it will recode it.")
        st.sidebar.markdown("Remember no one can decode your message without the phrase or alphabet so please don't forget it!")
        st.sidebar.markdown("Please note that we will be adding more to the webside so when there is something new please remember to check the instructions.")


        st.markdown("## Enter your message and encode/decode.")

        user_message = st.text_area("Enter your message:", height=500)

        code_flag = st.checkbox("Check box to code message, uncheck to decode.", value=True)

        coded_message = ""

        if st.button("Code/Decode message"):
            #index_value = index_value.strip()
            #if len(index_value) > 0:
                #try:
                    #self.code_it.create_coded_from_shift(int(index_value))

                    #coded_message = self.code_it.code_message(user_message,
                                              #code_flag)

                    #st.markdown("## New message created:")
                    ##st.write(coded_message)
                    #st.text_area("Message:", height=500, value=coded_message)
                #except ValueError:
                    #st.write("Please enter a valid index number only!")

            #elif len(phrase_value.strip()) > 0:

                #self.code_it.create_coded_from_phrase(phrase_value)

                #coded_message = self.code_it.code_message(user_message,
                                                          #code_flag)

                #st.markdown("## New message created:")
                #st.text_area("Message:", height=500, value=coded_message)

            #elif len(multi_index.strip()) > 0:
            if len(multi_index.strip()) > 0:

                coded_message = self.code_it.code_multi_index_message(
                    user_message, multi_index, code_flag)

                st.markdown("## New message created:")
                st.text_area("Message:", height=500, value=coded_message)

            elif len(new_alphabet.strip()) > 0:

                self.code_it.create_coded_from_user_alphabet(new_alphabet)
                coded_message = self.code_it.code_message(user_message,
                                                          code_flag)

                st.markdown("## New message created:")
                st.text_area("Message:", height=500, value=coded_message)



if __name__ == "__main__":
    app = SL_App(CodeIt())
    app.run()

# frznjakylegisdpotbmqwxuvhcFRZNJAKYLEG ISDPOTBMQWXUVHC6807953142
