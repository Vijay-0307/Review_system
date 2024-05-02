import streamlit as st
import pymongo
import datetime
import time

# MongoDB Atlas connection setup
MONGODB_URI = "mongodb+srv://Vijay:7K807VsonNEaZvIH@cluster.dnzmwbn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"
client = pymongo.MongoClient(MONGODB_URI)
db = client["Review_sysytem"]
reviews_collection = db["review"]

# Streamlit title
st.title("Product Reviews")


# Initialize session state for the form reset
if 'form_reset' not in st.session_state:
    st.session_state.form_reset = False

# Review form
with st.form("review_form"):
    user_name = st.text_input("Your Name", key="user_name" if not st.session_state.form_reset else None)
    product_name = st.text_input("Product Name", key="product_name" if not st.session_state.form_reset else None)
    review_text = st.text_area("Review Text", key="review_text" if not st.session_state.form_reset else None)
    rating = st.slider("Rating (1 to 5)", 1, 5, key="rating" if not st.session_state.form_reset else None)
    
    # Submit button
    submit = st.form_submit_button("Submit Review")

    if submit:
        if user_name and product_name and review_text:
            # Create a new review
            review = {
                "user_name": user_name,
                "product_name": product_name,
                "review_text": review_text,
                "rating": rating,
                "timestamp": datetime.datetime.utcnow(),
            }
            # Insert into MongoDB
            reviews_collection.insert_one(review)
            st.success("Review submitted successfully!")

            # Reset the form
            st.session_state.form_reset = True
        else:
            st.warning("Please fill in all fields.")

# If form has been reset, rerun the app
if st.session_state.form_reset:
    st.rerun()  # Reload the app to reset the form

# Fetch and display reviews
def fetch_reviews():
    return list(reviews_collection.find({}).sort("timestamp", pymongo.DESCENDING))

st.subheader("Latest Reviews")

reviews = fetch_reviews()
for review in reviews:
    st.write(f"**{review['product_name']}** by {review['user_name']}")
    st.write(f"Rating: {review['rating']}/5")
    st.write(f"Review: {review['review_text']}")
    st.write(f"Submitted on: {review['timestamp']}")
    st.write("---")