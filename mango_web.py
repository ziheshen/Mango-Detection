try:
 
    import torch
    from enum import Enum
    from io import BytesIO, StringIO
    from typing import Union
    from PIL import Image
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

st.write("""
# Mango Dtection App
This app can detect the photo of upploaded **Mango**!
""")


model = torch.hub.load('ultralytics/yolov5', 'custom', path='runs/train/exp8/weights/best.pt')

class FileUpload(object):
 
    def __init__(self):
        self.fileTypes = ["csv", "png", "jpg"]
 
    def run(self, df):
        """
        Upload File on Streamlit Code
        :return:
        """
        #model = torch.hub.load('ultralytics/yolov5', 'custom', path='runs/train/exp8/weights/best.pt')
        #st.info(__doc__)
        st.markdown(STYLE, unsafe_allow_html=True)
        with st.form("my-form", clear_on_submit=True):
            files = st.file_uploader("Upload file", type=self.fileTypes, accept_multiple_files = True )
            submitted = st.form_submit_button("UPLOAD!")

            if submitted and files is not None:
                st.write("UPLOADED!")

        #files = st.file_uploader("", type=self.fileTypes, accept_multiple_files = True )
        show_file = st.empty()
        if not files:
            show_file.info("Please upload a file of type: " + ", ".join(["csv", "png", "jpg"]))
            return
        #content = file.getvalue()
        #show_file.image(file, caption = '0')
        '''if isinstance(file, BytesIO):
            
            show_file.image(file)
        else:
            print("123")
            data = pd.read_csv(file)
            st.dataframe(data.head(10))
        '''

        indices = [ i+1 for i in range(len(files)) ]
        st.image(files, width=300, caption=indices)
        
        
        #print(files.name)
        for f in files:
            print( f.name )
            img = f.name
            
            model.iou = df.at[0, 'IOU']
            model.conf = df.at[0, 'Conf']
            results = model(img)
            results.show()
            
        #print(df)

def user_input_features():
    IOU = st.sidebar.slider('IOU', 0.0, 1.0, 0.5)
    Conf = st.sidebar.slider('Confidence', 0.0, 1.0, 0.3)
    
    data = {'IOU': IOU,
            'Conf': Conf}
    features = pd.DataFrame(data, index=[0])
    return features


 
if __name__ ==  "__main__":
    
    st.sidebar.header('User InputThreshold')
    df = user_input_features()
    
    st.subheader('User InputThreshold')
    st.write(df)
    
    helper = FileUpload()
    helper.run(df)
    #print(files,"\n\n\n",df);

    #print(files)
