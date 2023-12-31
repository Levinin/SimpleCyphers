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
        st.markdown("This page uses an alphabet of lower case + upper case + digits + space + newline. It gives you a few ways to create your code alphabet. If you choose to input a full code alphabet of your own, make sure you input all of lower case,  upper case, digits, space and newline. Note, this will take the first encryption method it finds a setting for, it can't read your mind :wink:")

        st.markdown("## Set up the encoding method.")

        index_value = st.text_input("Enter an offset value for the substitution:")

        phrase_value = st.text_input("Enter an alphabet scrambling phrase:")

        multi_index = st.text_input("Enter a multi-alphabet offset phrase (long phrases will be very hard to break):")

        st.markdown("## Enter your message and encode/decode.")

        user_message = st.text_area("Enter your message:", height=500)

        code_flag = st.checkbox("Check box to code message, uncheck to decode.", value=True)

        coded_message = ""

        if st.button("Code/Decode message"):
            index_value = index_value.strip()
            if len(index_value) > 0:
                try:
                    self.code_it.create_coded_from_shift(int(index_value))

                    coded_message = self.code_it.code_message(user_message,
                                              code_flag)

                    st.markdown("## New message created:")
                    #st.write(coded_message)
                    st.text_area("Message:", height=500, value=coded_message)
                except ValueError:
                    st.write("Please enter a valid index number only!")

            elif len(phrase_value.strip()) > 0:

                self.code_it.create_coded_from_phrase(phrase_value)

                coded_message = self.code_it.code_message(user_message,
                                                          code_flag)

                st.markdown("## New message created:")
                st.text_area("Message:", height=500, value=coded_message)

            elif len(multi_index.strip()) > 0:

                coded_message = self.code_it.code_multi_index_message(
                    user_message, multi_index, code_flag)

                st.markdown("## New message created:")
                st.text_area("Message:", height=500, value=coded_message)


if __name__ == "__main__":
    app = SL_App(CodeIt())
    app.run()

