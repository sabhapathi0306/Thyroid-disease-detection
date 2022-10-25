
import streamlit as st
import pickle
import pandas as pd


progress  = st.progress(0)
for i in range(100):
    time.sleep(0.1)
    progress.progress(i + 1)

    
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

st.set_page_config(page_title="Thyroid detection",layout="wide")


st.title("Thyriod Disease Detection")
#st.image("hh.jpg",width=650)
option = st.sidebar.radio("Menu", ['Home'])
placeholder = st.empty()
if option=='Home':
    st.markdown('Input the data in given formate')
    st.markdown("""
                - **AGE:continuous [1=><=100]**
                - **sex :M,F**
                - **on thyroxine:f,t**
                - **tumor:f,t**
                - **thyroid surgery:f,t**
                - **on antithyriod medication:f,t**
                - **TSH:numeric**
                - **FTI:numeric**
                - **T3:numeric**
                - **TT4:numeric**
                - **T4U:numeric**
                """)
    st.markdown("""
     Example: TSH:1.4,FTI:109,T3:1.9,TT4:104,T4U:0.96,On Thyroxine:f,
     Tumor:f,thyroid surgery:f,Antimedication:f,sex:F,age:32
    """)
    def clear_text():
        st.session_state["a"] =0.0
        st.session_state["b"] = 0.0
        st.session_state["c"] = 0.0
        st.session_state["d"] = 0.0
        st.session_state["e"] = 0.0
        st.session_state["f"] = "select"
        st.session_state["g"] = "select"
        st.session_state["h"] = "select"
        st.session_state["i"] = "select"
        st.session_state["j"] = 0
        st.session_state["k"] = "select"
    col1,col2,col3,col4,col5 = st.columns(5)
    
    with col1:
        TSH = st.number_input("Enter TSH value",key = "a",value =0.0,min_value = 0.0,max_value = 1000.0)
    with col2:
        FTI = st.number_input("Enter FTI value",key = "b",value=0.0,min_value = 0.0,max_value = 1000.0)
    with col3:
        T3 = st.number_input("Enter T3 value",key = "c",min_value = 0.0,max_value = 1000.0)

    with col4:
        TT4 = st.number_input("Enter TT4 value",key = "d",min_value = 0.0,max_value = 1000.0)

    with col5:
        T4U = st.number_input("Enter T4U value",key = "e",min_value = 0.0,max_value = 1000.0)

    col6,col7,col8,col9,col10 = st.columns(5)

    with col6:
         onthyroxine = st.selectbox('On Thyroxine',['select','f','t'],key = "f")

    with col7:
        tumor = st.selectbox('Tumor',['select','f','t'],key = "g")

    with col8:
        thyroidsurgery = st.selectbox('thyroid surgery',['select','f','t'],key = "h")

    with col9:
        antimedi = st.selectbox('Antimedication',['select','f','t'],key = "i")

    with col10:
        sex = st.selectbox('Sex',['select','M','F'],key = "k")

    age,sub,x,y,z = st.columns(5)
    with age:
        a = st.number_input("Age",key = "j",min_value = 0,max_value = 100)
    

    val = [TSH,FTI,T3,TT4,T4U,onthyroxine,tumor,thyroidsurgery,antimedi,a,sex]
    cols = ['TSH','FTI','T3','TT4','T4U','on thyroxine','tumor','thyroid surgery','on antithyroid medication','age','sex']
    df = pd.DataFrame([val],columns=cols)
    sex = {'M':0,'F':1}
    ont = {'f':0,'t':1}
    df['on thyroxine'] = df['on thyroxine'].map(ont)
    df['tumor'] = df['tumor'].map(ont)
    df['thyroid surgery'] = df['thyroid surgery'].map(ont)
    df['on antithyroid medication'] = df['on antithyroid medication'].map(ont)
    df['sex'] = df['sex'].map(sex)
    df['age'] = df['age'].astype('float')
    
    
   
    predict,clear = st.columns([1,1])
    with predict:
        pred = st.button("Predict")
    with clear:
        st.button("Clear",on_click=clear_text)

    if pred:
        def testing(val):
            dbfile = open('C:/Users/adith/Desktop/myp/Linkein_Api/app/JSON/model_trianed', 'rb')  
            clf= pickle.load(dbfile)
            ans = val.iloc[0].to_numpy().reshape(1,-1)
            predicts = clf.predict(ans)
            st.write("--------------Results---------------------")
            if predicts == ['-']:
                st.write('**Prediction result** :',str(predicts.tolist()))
                st.success("**No dignosis required**")
                
            if predicts == ['A'] or  predicts == ['B'] or  predicts == ['C']  or  predicts == ['D']:
                st.write('**Prediction result** :',str(predicts.tolist()))
                st.success("**hyperthyroid  condition**")
                    
            if predicts == ['E'] or  predicts == ['F'] or  predicts == ['G'] or  predicts == ['H']:
                st.write('**Prediction result** :',str(predicts.tolist()))
                st.success("**hypothyroid conditions**")
                    
                    
            if predicts == ['I'] or  predicts == ['J']:
                st.write('**Prediction result** :',str(predicts.tolist()))
                st.success("**binding protein**")
                    
            if predicts == ['K']:
                st.write('**Prediction result** : ',str(predicts.tolist()))
                st.success("**general health**")
                    
            if predicts == ['L'] or  predicts == ['M'] or  predicts == ['N']:
                st.write('**Prediction result** :',str(predicts.tolist()))
                st.success("**replacement therapy**")
                    
            if predicts == ['O'] or  predicts == ['P'] or  predicts == ['Q']:
                st.write('**Prediction result** :',str(predicts.tolist()))
                st.success("**antithyroid treatment**")
                    
            if predicts == ['R'] or  predicts == ['S'] or  predicts == ['T']:
                st.write('**Prediction result** :',str(predicts.tolist()))
                st.success("**miscellaneous condition**")
        testing(df)
        with st.expander("See Result explanation"):
            st.write("""
                    hyperthyroid conditions:

                        A	hyperthyroid
                        B	T3 toxic
                        C	toxic goitre
                        D	secondary toxic

                    hypothyroid conditions:

                        E	hypothyroid
                        F	primary hypothyroid
                        G	compensated hypothyroid
                        H	secondary hypothyroid

                    binding protein:

                        I	increased binding protein
                        J	decreased binding protein

                    general health:

                        K	concurrent non-thyroidal illness

                    replacement therapy:

                        L	consistent with replacement therapy
                        M	underreplaced
                        N	overreplaced

                    antithyroid treatment:

                        O	antithyroid drugs
                        P	I131 treatment
                        Q	surgery

                    miscellaneous:

                        R	discordant assay results
                        S	elevated TBG
                        T	elevated thyroid hormones
                        """)
