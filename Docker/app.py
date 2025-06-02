import streamlit as st

# Add custom CSS
st.markdown("""
    <style>
        .table-container {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }
        .table-box {
            # background-color: #f0f2f6;
            padding: 15px;
            border-radius: 10px;
            width: 200px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
        .table-box h4 {
            text-align: center;
            # color: black;
        }
        .table-box table {
            width: 100%;
            border-collapse: collapse;
        }
        .table-box td {
            padding: 4px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("📊 Multiplication Tables Generator")

# Input
num = st.number_input("Enter how many tables you want to print:", min_value=1, max_value=50, value=5)

# Table display
st.markdown('<div class="table-container">', unsafe_allow_html=True)


html = f'''
<div class="table-box">
    <h4>Table of {num}</h4>
    <table>
        {"".join([f"<tr><td>{num} × {j}</td><td>=</td><td>{num*j}</td></tr>" for j in range(1, 11)])}
    </table>
</div>
'''
st.markdown(html, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
