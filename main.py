import streamlit as st
st.title("anci application")
st.header("software developer")
st.subheader("UI-UX designer")
st.metric("python",14,10)
st.write("anci")
st.write("_anci_")
st.write("- anci")
st.write("# anci")
st.write("## anci")
st.write("⭐anci⭐")
st.divider()
st.sidebar.header("My sidebar")
st.sidebar.button("get start")
st.sidebar.text_input("name")
st.code("""
        # Generate Fibonacci sequence up to n terms
def fibonacci(n):
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

print(fibonacci(10))  # Output: First 10 Fibonacci numbers


""",language="python")
st.slider("age",0,100)
st.date_input("DOB")
st.divider()
st.text_input("Student name")
st.number_input("Student number")
st.selectbox("city",options=["Madurai","chennai","dindigul"])
st.radio("Gender",options=["male","female"])
st.multiselect("skills",options=["html","sql","java","python"])