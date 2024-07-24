import streamlit as st

from pic2pix import convert

st.title('Pic2Pix Front End')

uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg", "gif"])

# Taken from pic2pix.py to create a default palette
PALETTE = [
    [31, 36, 10],
    [57, 87, 28],
    [165, 140, 39],
    [239, 172, 40],
    [239, 216, 161],
    [171, 92, 28],
    [24, 63, 57],
    [239, 105, 47],
    [239, 183, 117],
    [165, 98, 67],
    [119, 52, 33],
    [114, 65, 19],
    [42, 29, 13],
    [57, 42, 28],
    [104, 76, 60],
    [146, 126, 106],
    [39, 100, 104],
    [239, 58, 12],
    [60, 159, 156],
    [155, 26, 10],
    [54, 23, 12],
    [85, 15, 10],
    [48, 15, 10]
]

if uploaded_file is not None:
    img = convert(uploaded_file, PALETTE)
    

    if img is not None:
        if st.button("Download Image"):
            st.download_button(
                label="Download",
                data=img,
                file_name="sprite.png",
                mime="image/png"
            )
        st.image(img, use_column_width=True)
