import streamlit as st
import os
import time
import glob
import os
from streamlit_option_menu import option_menu
from bokeh.models.widgets import Div 
import base64


@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
    
# HTTP + URL packages
import httplib2
from urllib.parse import urlencode, quote # For URL creation
from about import ab

mary_host = "localhost"
mary_port = "59125"
app_dir = "/home/services/TTS/TTS/app"
# from gtts import gTTS
# from googletrans import Translator

os.chdir(app_dir)
try:
    os.mkdir("temp")
except:
    pass
st.set_page_config(page_title='Sinhala_TTS.LTRL;', page_icon="🗣️")
# translator = Translator()

# st.sidebar.markdown("""<h1 style='text-align: center; color:white; font-size:60px;margin-top:-50px; color:white;'><a style='text-align: center; color:white; font-size:60px;margin-top:-50px;text-decoration:none;' href="https://subasa.ga/" >සුබස</a></h1><h1 style='text-align: center; font-size:30px;margin-top:-30px;'></h1>""",unsafe_allow_html=True)
# st.sidebar.markdown('''
#     <a href="https://subasa.ga/">
#         <img style=' align:center;  display: block;margin-left: auto;margin-right: auto;width: 50%;' src="https://subasa.ga/wp-content/uploads/2021/11/subasda-png-1536x878.png" />
#     </a>''',
#     unsafe_allow_html=True
# )

# subasa_logo = get_base64_of_bin_file('logo/subas_logo.png')
# html_code = f'''    
#     <img style=' align:center;  display: block;margin-left: auto;margin-right: auto;width: 50%;' src="data:image/png;base64,{subasa_logo}" />
#     '''
# st.sidebar.markdown(html_code, unsafe_allow_html=True)
# st.sidebar.markdown("""<h1 style='text-align: center; font-size:60px;margin-top:-20px; '><a style='text-align: center; color:{font_colour}; font-size:60px;margin-top:-50px;text-decoration:none;' >සුබස</a></h1><h1 style='text-align: center; font-size:30px;margin-top:-30px;'></h1>""",unsafe_allow_html=True)

subasa_banner = get_base64_of_bin_file('logo/Subasa_Banner_TTS.jpg')
html_code = f'''    
    <img style=' align:center;  display: block;margin-left: auto;margin-right: auto;width: 75%;margin-top:-40px;margin-bottom:50px;' src="data:image/png;base64,{subasa_banner}" />
    '''
st.markdown(html_code, unsafe_allow_html=True)


# st.sidebar.markdown('''
  
#         <img style=' align:center;  display: block;margin-left: auto;margin-right: auto;width: 50%;' src="https://subasa.ga/wp-content/uploads/2021/11/subasda-png-1536x878.png" />
#     ''',
#     unsafe_allow_html=True
# )
# html_temp3 = """
# <hr>
# """
# st.sidebar.markdown(html_temp3.format('2px', '#ffffff' ),unsafe_allow_html=True)


# st.sidebar.markdown("""<h2 style='text-align: left; '>About</h2><p style='text-align: justify;'>In this project we focus on developing a human quality Text-to-Speech (TTS) systems for Sinhala. Human quality TTS, enables visually impaired community to use a computer and access digital text in their mother language. </p>""",unsafe_allow_html=True)




    # js = "window.open('https://www.streamlit.io/')" # New tab or window
    
    
# with st.sidebar:
#     selected = option_menu("", ["Sinhala ASR", "Sinhala TTS", "Tamil - Sinhala MT","Sinhala OCR"], 
#         default_index=1)

# if selected == "Sinhala ASR":
#     # js = "window.open('https://www.streamlit.io/')" # New tab or window
#     js = "window.location.href = 'https://stt.subasa.lk/'" # Current tab 
#     html = '<img src onerror="{}">'.format(js) 
#     div = Div(text=html) 
#     st.bokeh_chart(div)
# elif selected == "Sinhala TTS":
#     print('',end='')
#     # js = "window.open('https://www.streamlit.io/')" # New tab or window
#     # js = "window.location.href = 'https://tts.subasa.lk/'" # Current tab 
#     # html = '<img src onerror="{}">'.format(js) 
#     # div = Div(text=html) 
#     # st.bokeh_chart(div)
# elif selected == "Tamil - Sinhala MT":
#     # js = "window.open('https://www.streamlit.io/')" # New tab or window
#     js = "window.location.href = 'https://mt.subasa.lk/'" # Current tab 
#     html = '<img src onerror="{}">'.format(js) 
#     div = Div(text=html) 
#     st.bokeh_chart(div)
# else:
#     # js = "window.open('https://www.streamlit.io/')" # New tab or window
#     js = "window.location.href = 'https://ocr.subasa.lk/'" # Current tab 
#     html = '<img src onerror="{}">'.format(js) 
#     div = Div(text=html) 
#     st.bokeh_chart(div)

# images = ['ltrllogo.png', 'ucsclogo.png']
# st.sidebar.image(images, width=50)

# logos

# bin_str1 = get_base64_of_bin_file('logo/ltrllogo.png')
# bin_str2 = get_base64_of_bin_file('logo/ucsclogo.png')
# html_code = f'''
   
#         <img style='margin-left: 10%;margin-right: 10%;width: 28%;' src="data:image/png;base64,{bin_str1}" />

#     <a style='text-decoration:none;' href="https://ucsc.cmb.ac.lk/">
#         <img style='margin-left: 10%;margin-right: 10%;width: 28%;' src="data:image/png;base64,{bin_str2}" />
#     </a>
#     '''
# st.sidebar.markdown(html_code, unsafe_allow_html=True)

# col1, col2, col3,col4,col5 = st.sidebar.columns([0.1,1, 0.1, 1,0.1])
# col2.image("logo/ltrllogo.png", use_column_width=True)
# col4.image("logo/ucsclogo.png", use_column_width=True)

# st.sidebar.markdown('''
#     <a href="https://subasa.ga/">
#         <img style=' align:center;  display: block;margin-left: auto;margin-right: auto;width: 50%;' src="http://subasa.lk/images/ltrllogo.png" />
#         <img style=' align:center;  display: block;margin-left: auto;margin-right: auto;width: 50%;' src="https://subasa.ga/wp-content/uploads/2021/11/subasda-png-1536x878.png" />
#     </a>''',
#     unsafe_allow_html=True
# )

# st.sidebar.markdown("""<h2 style='text-align: center;color: white;'><a style='text-align: center;color: white;' href="https://stt.subasa.lk/" target="_blank">ASR Deepspeech</a></h2>""", unsafe_allow_html=True)
# st.sidebar.markdown("""<h2 style='text-align: center;color: white;'><a style='text-align: center;color: white;' href="http://35.230.103.157:8501/" target="_blank">Sinhala OCR</a></h2>""", unsafe_allow_html=True)
# st.sidebar.markdown("""<h2 style='text-align: center;color: white;'><a style='text-align: center;color: white;' href="https://mt.subasa.lk/" target="_blank">Tamil - Sinhala MT</a></h2>""", unsafe_allow_html=True)
#st.sidebar.markdown("""<h2 style='text-align: center;color: white;'><a style='text-align: center;color: white;' href="https://tts.subasa.lk/" target="_blank">Sinhala TTS</a></h2>""", unsafe_allow_html=True)

st.markdown("""<h1 style='text-align: center;font-size:40px;margin-top:-50px;margin-bottom:-30px;'>Sinhala Text-To-Speech</h1>""",unsafe_allow_html=True)


# st.markdown("<div align='center',padding:5px ><br>"
#                 "<img src='https://img.shields.io/badge/MODELS%20WITH-MaryTTS-critical?style=for-the-badge'"
#                 "alt='API stability' height='25'/>"
#                 "<img src='https://img.shields.io/badge/CODE%20WITH-Python-blue?style=for-the-badge'"
#                 "alt='API stability' height='25'/>"
#                 "<img src='https://img.shields.io/badge/DASHBOARDING%20WITH-Streamlit-green?style=for-the-badge'"
#                 "alt='API stability' height='25'/></div>", unsafe_allow_html=True)

home_button = get_base64_of_bin_file('logo/home1.png')
home_button_blue = get_base64_of_bin_file('logo/home2.png')

html_code1 = f"""
    <a href="https://subasacms.tk">
    <img class="default" style='align:left; width:90px; margin-bottom:-20px;' src="data:image/png;base64,{home_button}"/>
    <img class="hover" style='align:left; width:90px;margin-bottom:-20px;' src="data:image/png;base64,{home_button_blue}"/>
</a>
"""
html_code2="""
<style>
a img.hover {
    display: none;
}
a img.default {
    display: inherit;
}
a:hover img.hover {
    display: inherit;
}
a:hover img.default {
    display: none;
}
</style>
    """

st.markdown(html_code1+html_code2, unsafe_allow_html=True)

html_temp2 = """
<hr>
"""
st.markdown(html_temp2.format('2px', '#ffffff' ),unsafe_allow_html=True)
#input_text = st.text_input("Enter text")
st.markdown("<h3 style='text-align: Left; margin-top:-30px;margin-bottom:-10px;'>Enter text</h3>", unsafe_allow_html=True)
# input_text = st.text_area("Type sinhala text ..",height = 150, max_chars=250)
input_text = st.text_area("Type sinhala text ..",height = 150)

def text_to_speech(input_text, mary_host, mary_port):
    # translation = translator.translate(text, src=input_language, dest=output_language)
    # trans_text = translation.text
    # Build the query
    query_hash = {"INPUT_TEXT":input_text,
                "INPUT_TYPE":"TEXT", # Input text
                "LOCALE":"si",
                "OUTPUT_TYPE":"AUDIO",
                "AUDIO":"WAVE", # Audio informations (need both)
                }
    query = urlencode(query_hash)
    print("query = \"http://%s:%s/process?%s\"" % (mary_host, mary_port, query))

    # Run the query to mary http server
    h_mary = httplib2.Http()
    resp, content = h_mary.request("http://%s:%s/process?" % (mary_host, mary_port), "POST", query)

    #  Decode the wav file or raise an exception if no wav files
    if (resp["content-type"] == "audio/x-wav"):

        # Write the wav file
        fileName = time.strftime("%Y%m%d-%H%M%S")
        f = open("temp/"+fileName+".wav", "wb")
        f.write(content)
        f.close()

    else:
        raise Exception(content)

    #return send_from_directory('tmp/', fileName+'.wav', as_attachment=True)
    return fileName


if st.button("Speak"):
    if input_text == "":
            st.warning('Please **enter text** ')
    else :
        result = text_to_speech(input_text, mary_host, mary_port)
        audio_file = open(f"temp/{result}.wav", "rb")
        audio_bytes = audio_file.read()
        st.markdown(f"## Your audio:")
        st.audio(audio_bytes, format="audio/wav", start_time=0)

    # if display_output_text:
    #     st.markdown(f"## Output text:")
    #     st.write(f" {output_text}")


def remove_files(n):
    wav_files = glob.glob("temp/*wav")
    if len(wav_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in wav_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)

ab()

html_temp2 = """
<hr>
"""
st.markdown(html_temp2.format('2px', '#ffffff' ),unsafe_allow_html=True)
html_temp = f"""
    <div style = padding:1px">
    <p style = "text_align:center;padding:0.5px;line-height: 0.65"> </p>
    <p style = "text_align:center;padding:0.5px;line-height: 0.65"> Language Technology Research Laboratory </p>
    <p style = "text_align:center;line-height: 1.5"> University of Colombo School of Computing, Sri Lanka</p>
    </div>
    
   """

st.markdown(html_temp, unsafe_allow_html = True)
# logos

bin_str1 = get_base64_of_bin_file('logo/ltrllogo.png')
bin_str2 = get_base64_of_bin_file('logo/ucsclogo.png')
html_code = f'''
   
        <img style='margin-left: 33%;margin-right: 5%;width: 13%;' src="data:image/png;base64,{bin_str1}" />

    <a style='text-decoration:none;' href="https://ucsc.cmb.ac.lk/">
        <img style='margin-left: 3%;margin-right: 31%;width: 13%;' src="data:image/png;base64,{bin_str2}" />
    </a>
    '''
st.markdown(html_code, unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)