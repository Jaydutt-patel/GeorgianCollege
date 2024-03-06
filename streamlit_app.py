import streamlit as st
from multimodal_search import MultimodalSearch

# Set wide layout
st.set_page_config(layout="wide")

# Function to set the background image and additional styles
def set_background_and_styles():
    # CSS to inject contained in a triple-quote string
    st.markdown(
        """
        <style>
        /* Set the background image */
        .stApp {
            background-image: url("https://t3.ftcdn.net/jpg/02/10/85/26/360_F_210852662_KWN4O1tjxIQt8axc2r82afdSwRSLVy7g.jpg");
            background-size: cover;
        }
        
        /* Additional styles for a fancier layout */
        /* Customize your button */
        .stButton>button {
            border: 2px solid #4CAF50;
            background-color: #4CAF50;
            color: white;
            padding: 10px 24px;
            cursor: pointer;
            border-radius: 8px;
        }
        
        /* Hover effects for the button */
        .stButton>button:hover {
            background-color: #45a049;
        }
        
        /* Customize markdown headers */
        h1 {
            color: #ffffff !important; /* Change your desired color */
        }
        
        /* Customize warning message */
        .stAlert {
            background-color: #ffcccb; /* Light red background */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def main():
    # Set background and custom styles
    set_background_and_styles()
    
    # Custom page title
    st.markdown("<h1 style='text-align: center; color: green;'>Fashion Search Engine</h1>", unsafe_allow_html=True)

    multimodal_search = MultimodalSearch()

    query = st.text_input("Enter your query:", "")
    if st.button("Search"):
        if len(query) > 0:
            results = multimodal_search.search(query)
            st.warning("Your query was "+query)
            st.subheader("Search Results:")
            col1, col2, col3 = st.columns([1,1,1])
            with col1:
                st.write(f"Score: {round(results[0].score*100, 2)}%")
                st.image(results[0].content, use_column_width=True)
            with col2:
                st.write(f"Score: {round(results[1].score*100, 2)}%")
                st.image(results[1].content, use_column_width=True)
            with col3:
                st.write(f"Score: {round(results[2].score*100, 2)}%")
                st.image(results[2].content, use_column_width=True)
        else:
            st.warning("Please enter a query.")

if __name__ == "__main__":
    main()