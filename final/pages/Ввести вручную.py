import numpy as np
import pandas as pd
import streamlit as st
from model import Predicter
from utils import *

st.set_page_config(initial_sidebar_state="collapsed", layout='wide')
# st.markdown("# Ввести данные вручную️")
col = st.columns(7)
col = st.columns(7)
col = st.columns(7)
col = st.columns(7)
col = st.columns(7)
col = st.columns(7)
add_bg_from_local('/app/building_hack/final/16922.png')
# set color text to black
st.markdown(
    """
<style>
p {
    color: black;
}
</style>
""",
    unsafe_allow_html=True,
)

# create manual input with layout
col = st.columns(7)
col1 = st.columns(7)
col2 = st.columns(7)

col4 = st.columns(7)
# You can use a column just like st.sidebar:
st.markdown("Основная таблица")

pr_bl = col[0].text_input('Программа строительства', value='Образование')
podpr_bl = col[1].text_input('Подпрограмма строительства', value='Общеобразовательные учреждения')
uniq_id = col[2].text_input('Уникальный айди', value='022-0527')
identificator = col[3].text_input('Идентификатор вида', value=1.1)
name_task = col[4].text_input('Название 3адачи', value='Предпроектные работы')
percent_end = col[5].text_input('Процент 3авершения', value=100.0)
begin = col[6].text_input('Дата начала задачи', value="2022-01-14")
end = col1[0].text_input('Дата окончания задачи', value="2023-03-30")
begin_bp = col1[1].text_input('Дата начала БП0', value="2021-05-04")
end_bm = col1[2].text_input('Дата окончания БП0', value="2021-05-04")
status_exp = col1[3].text_input('Статус по экспертизе', value=1.0) # maybe -1 is none, or empty cell
form_ksg = col1[4].text_input('Дата формирования КСГ', value="2023.01.17") # "-" - meaning none
expertize = col1[5].selectbox('Экспертиза', ["1ТС", "2ТС","1Т","1С","2С","2Т","-"], index=2)

st.markdown("Дополнительная таблица ")

code_ds = col2[0].text_input('Код ДС', value='022-0043')
status_sq = col2[1].selectbox('состояние площадки', ["Свободна, передана", 
                                                               "Занята",
                                                                "Свободна, не передана",
                                                                "Не передана",
                                                                "Передана под снос (для объектов сноса)",
                                                                "Не передана под снос (для объектов сноса)",
                                                                "-"], index=2)

genproectir = int(col2[3].text_input('Генпроектировщик', value=1))
genpodryad = int(col2[4].text_input('Генподрядчик', value=2))
name_of_worker = col2[2].text_input('Кол-во рабочих', value='wagondigitalnewyearrailway:)happy')
date_rep = col2[2].text_input('date_report', value='2023.01.20')

# create dataframe
data_base = {'pr_bl': [pr_bl],
        'podpr_bl': [podpr_bl],

        # TODO continue        
        }
data_additional = {'pr_bl': [pr_bl],
        'podpr_bl': [podpr_bl],

        # TODO continue        
        }
df = pd.DataFrame(data_base)
df = pd.DataFrame(data_additional)
# st.table(pd.DataFrame(data))

# predict
if st.button('Предсказать'):
    model = Predicter()
    y_pred = model.predict(df_base, df_additional)
    # print(y_pred)
    # df.insert(0, 'y', y_pred)
    # append to dataframe
    # add y_pred col to the beginning of the dataframe
    # y_pred = [np.random.randint(1, 100) for i in range(len(df))]
    # write text Ожидаемое время

    # increase text size
    st.markdown(f'<p style="font-size: 20px;font-color: red">Ожидаемое время окончания строительства <b>{st_code_snd}</b> до <b>{st_code_rsv}</b> составит <u>{str(y_pred[0])[:6]}</u> ч.</p>', unsafe_allow_html=True)
    df.insert(0, 'y', y_pred)
    # st.write(df)
    # st.table(pd.DataFrame(df))




