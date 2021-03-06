import streamlit as st

def ab():
    html_temp3 = """
    <hr>
    """
    st.markdown(html_temp3.format('1px', '#ffffff' ),unsafe_allow_html=True)

    st.write("### Contributors")
    
    st.write("""
Tharaka Vishwakula,
Priyanthini Sivasubramaniyam,
Roshan Nadeesha,
Lakshika Nanayakkara,
Amathri Perera,
Dilhani Samaranayake,
Ashan Cassim,
Ashmari Promodya,
Buddhi Gamage,
Bimsara Gamage,
Asoka Bandula,
Kumudu Gamage,
Chamila Liyanage,
Randil Pushpananda,
Asanka Wasala,
Dulip Herath,
Viraj Welgama, and
Ruvan Weerasinghe 

    """)
    
    st.write("### Funded by")
    st.write(
    """   
- Information and Communication Technology Agency of Sri Lanka (ICTA)
- World Intellectual Property Organization (WIPO)
- University of Colombo School of Computing (UCSC)
    """
    )
    st.write("### Disclaimer")
    st.write('Every effort is made to provide accurate and complete information. However, we cannot guarantee that there will be no errors. Additionally, LTRL, UCSC, assume no legal liability for the accuracy, completeness, or usefulness of any information, product, or process disclosed herein and do not represent that use of such information, product, or process would not infringe on privately owned rights.')
    st.write("### How to cite")
    st.code("""

        @Misc{tts,
            author = {{LTRL UCSC}},
            title = {Sinhala Text-To-Speech},
            url = {https://tts.subasa.lk},
            version ={1.0.0},
            year = {2022},
            }

    """)