import streamlit as st
import base64


st.set_page_config(page_title="Riyadh, and The Hunt for a Home!", page_icon="🏠", layout="wide")

# This to center the image, DO NOT REMOVE
st.markdown(
    """
    <style>
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)

left_co, right_co = st.columns(2)
file_ = open("./assets/23.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

with right_co:
    st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="Riyadh, and The Hunt for a Home!">',
    unsafe_allow_html=True,
)
    
with left_co:
    st.markdown("# Riyadh, and The Hunt for a Home!")


st.markdown("""

## CONGRATULATIONS! For graduating from the top academy for Data Science!

##### Pretty nice getting all those job offers ha? Better go back and thank the academy, especially your instructors! But wait… all offers are in Riyadh? Interviewers are asking if you live in Riyadh?

Oh, now it’s getting real..

Yeah… Yeah we know… it's time to seriously consider moving, and finding a place to stay in Riyadh is a bit annoying (might be an understatement) and it doesn’t help that whenever you go online to find something you just get bombarded by so many options, or none! 

And you’re probably thinking “Wouldn’t it be nice if someone just picked something for me? Or at least help me decide? I need an expert…” 

Well look no more! We did the search for you!

See Riyadh, just like any city, is split into multiple regions:
""")

#FIXME - Plot 1.0
# Columns to center the image
left_co, cent_co, right_co = st.columns(3)
with cent_co:
    st.image("./assets/k.png", width=500, caption="Riyadh, and The Hunt for a Home!")

st.markdown("""
And although accommodations are found in all regions, prices vary.

What affects the price is how far the place is from the center, and whether or not it's in a "fancy" new neighborhood.
""")

#FIXME - Plot 2.0
# Columns to center the image
left_co, cent_co, right_co = st.columns(3)
with cent_co:
    st.image("./assets/k.png", width=500, caption="Riyadh, and The Hunt for a Home!")
with cent_co:
    st.image("./assets/k.png", width=500, caption="Riyadh, and The Hunt for a Home!")

#REVIEW - {insert example} search for bold
st.markdown("""
Now all you have to do is consider transportation.

If you’re a practical person and prices don’t matter to you, you would want to be near your workplace.

Or if you’re a person that spends wisely, and transportation is not a concern, then we recommend finding a place in the more affordable areas, like **{insert example based on the charts}**.

Everything you just saw, can be found at **{website}**, and their offers cover all regions of Riyadh.

Feels great doesn't it? No more worry about where and what to pick. We’re glad we could help!

Take a look at the below list of scenarios, and hopefully one of them could be a great fit for you!

Wishing you all the best in your future endeavors!

""")

st.markdown("""
# Living Scenarios:

#### 1.	Money is not a problem, and I want a fancy neighborhood:
- a.	Option1
- b.	Option2
- c.	Option3

#### 2.	Money is not a problem, but I hate driving for too long:
- a.	Option1
- b.	Option2
- c.	Option3

#### 3.	I like to spend wisely, but I also want a good neighborhood:
- a.	Option1
- b.	Option2
- c.	Option3

#### 4.	I like to be smart about my money, but I hate driving for too long:
- a.	Option1
- b.	Option2
- c.	Option3
""")