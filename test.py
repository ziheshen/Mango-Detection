try:
 
    from enum import Enum
    from io import BytesIO, StringIO
    from typing import Union
 
    import pandas as pd
    import streamlit as st
except Exception as e:
    print(e)
 
STYLE = """
<style>
img {
    max-width: 100%;
}
</style>
"""
 
 
class FileUpload(object):
 
    def __init__(self):
        self.fileTypes = ["csv", "png", "jpg"]
 
    def run(self):
        """
        Upload File on Streamlit Code
        :return:
        """
        st.info(__doc__)
        st.markdown(STYLE, unsafe_allow_html=True)
        with st.form("my-form", clear_on_submit=True):
            files = st.file_uploader("Upload file", type=self.fileTypes, accept_multiple_files = True )
            submitted = st.form_submit_button("UPLOAD!")

            if submitted and files is not None:
                st.write("UPLOADED!")
            #files = st.file_uploader("Upload file", type=self.fileTypes, accept_multiple_files = True )
        show_file = st.empty()
        if not files:
            show_file.info("Please upload a file of type: " + ", ".join(["csv", "png", "jpg"]))
            return
        #content = file.getvalue()
        show_file.image(files)
        '''
            if isinstance(file, BytesIO):
                show_file.image(file)
            else:
                data = pd.read_csv(file)
                st.dataframe(data.head(10))
            file.close()
         '''
 
if __name__ ==  "__main__":
    helper = FileUpload()
    helper.run()
