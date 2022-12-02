import streamlit as st
import platform
from PIL import Image

st.title("Color to B/W photo converter")

# Allow uploading photo (Preferred for iOS users)
uploaded_image = st.file_uploader("Upload Image")

# print(1, uploaded_image)

# Stop the display of this widget for iOS (Ease of Access)
with st.expander("Start Camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")

# Create a pillow image instance
if camera_image:
    img = Image.open(camera_image)
elif uploaded_image:
    img = Image.open(uploaded_image)
else:
    img = None

message = st.empty()
# print(2, img, type(img) == 'PIL.PngImagePlugin.PngImageFile')

if (img==None):
    message.info("Waiting for a photo...")    
else:
    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

    # Render the grayscale image on a webpage
    st.image(gray_img)
    # print(True)