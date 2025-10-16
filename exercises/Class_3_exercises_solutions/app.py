import streamlit as st
import pandas as pd
from library import Library
from book import Book
import matplotlib.pyplot as plt
# '''
# Exercise 8
# Display the library collection dynamically in Streamlit and visualize how many times each book has been requested.

# 1. Create a new file in your project folder named app.py
# 2. Open app.py and import Streamlit and your Library and Book classes
# 3. Create a Library instance and add a few books to it (you can hardcode them or reuse the ones from your main script).
# 4. Convert your book collection into a Pandas DataFrame
# 5. Display the table
# 6. Add a simple bar chart to visualize how many times each book has been requested
# 7. Add a short introductory message at the top with "This dashboard shows how often each book has been requested."
# 8. Run your app.
# '''

st.set_page_config(page_title="Library Insights", page_icon="📚", layout="centered")

# st.title("Library Insights")
# st.write("This dashboard shows how often each book has been requested.")

# # Create a library instance and add books
# library = Library()
# library.add_book(Book("Python Programming", "John Doe", "1234567890", 3))
# library.add_book(Book("Advanced Python", "Jane Smith", "0987654321", 2))
# library.add_book(Book("Machine Learning Guide", "Sarah Lee", "5678901234", 5))
# library.add_book(Book("Data Science Essentials", "Alan Turing", "1122334455", 1))

# # Convert books to DataFrame
# df = pd.DataFrame([vars(book) for book in library.books])

# # Display table
# st.subheader("Library Collection")
# st.dataframe(df)

# # Display bar chart of requests
# st.subheader("Most Requested Books")
# st.bar_chart(df.set_index("title")["times_requested"])

# Exercise 9

# Make the Streamlit app interactive by allowing users to "request" a book.

# 1. In app.py, add a new section below the bar chart:
#    - Use st.selectbox() to let the user choose a book title.
#    - Use st.button() to simulate a request for that book.

# 2. When the button is clicked:
#    - Call library.request_book(selected_title) to increment the counter.
#    - Recreate the DataFrame and refresh the displayed table and chart.

# 3. To ensure the counter updates in real time, use Streamlit’s session state:
#    python
#    if "library" not in st.session_state:
#        st.session_state.library = Library()
#    library = st.session_state.library

# 4. After updating, display a confirmation message (e.g., "Book requested successfully!").

# 5. Stage and commit your work


st.session_state
# Select book to request
st.title("📚 Interactive Library Dashboard")
st.write("Select a book and simulate a request to update its popularity count.")

# Initialize the library in session state
if "library" not in st.session_state:
    library = Library()
    library.add_book(Book("Python Programming", "John Doe", "1234567890", 3))
    library.add_book(Book("Advanced Python", "Jane Smith", "0987654321", 2))
    library.add_book(Book("Machine Learning Guide", "Sarah Lee", "5678901234", 5))
    library.add_book(Book("Data Science Essentials", "Alan Turing", "1122334455", 1))
    st.session_state.library = library

library = st.session_state.library

# Create DataFrame
df = pd.DataFrame([vars(book) for book in library.books])

# Select book to request
selected_title = st.selectbox("Select a book to request:", df["title"])

if st.button("📖 Request Book"):
    library.request_book(selected_title)
    st.success(f"✅ Book '{selected_title}' requested successfully!")

# Refresh DataFrame after updates
df = pd.DataFrame([vars(book) for book in library.books])

st.subheader("Library Collection")
st.dataframe(df)

st.subheader("Most Requested Books")
st.bar_chart(df.set_index("title")["times_requested"])

# Exercise 10

st.subheader("Add a New Book")
with st.form("add_book_form", clear_on_submit=True):
    title = st.text_input("Title")
    author = st.text_input("Author")
    isbn = st.text_input("ISBN")
    times_requested = st.number_input("Initial times requested", min_value=0, value=0)
    submitted = st.form_submit_button("Add Book")

if submitted:
    if title and author and isbn:
        library.add_book(Book(title, author, isbn, times_requested))
        st.success(f"Book '{title}' added successfully!")
    else:
        st.warning("Please fill in all fields before adding a book.")

# Refresh and display updated library
df = pd.DataFrame([vars(book) for book in library.books])
st.subheader("Current Collection")
st.dataframe(df)

st.subheader("Most Requested Books")
st.bar_chart(df.set_index("title")["times_requested"])

# Exercise 11

# Sidebar content
st.sidebar.title("App Settings")
st.sidebar.write("You can configure your layout and style here.")
st.sidebar.markdown("---")
st.sidebar.write("Instructor: Your Name")
st.sidebar.write("Advanced Python Course")

st.title("📚 Library Analytics Dashboard")
st.write("This dashboard showcases configuration and layout customization.")

# Exercise 12
# Matplotlib chart
fig, ax = plt.subplots()
ax.bar(df["title"], df["times_requested"], color="#3CB371")
ax.set_title("Most Requested Books")
ax.set_xlabel("Book Title")
ax.set_ylabel("Times Requested")
plt.xticks(rotation=45)

st.pyplot(fig)

# Exercise 13
# **File:** .streamlit/config.toml
#[theme]
# base="dark"
#primaryColor="#FF9800"
# backgroundColor="#1E1E1E"
# secondaryBackgroundColor="#2E2E2E"
# textColor="#FFFFFF"
# font="monospace"