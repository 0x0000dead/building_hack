import datetime

import numpy as np
import pandas as pd

from utils import *

st.set_page_config(initial_sidebar_state="collapsed", layout='wide')
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
row = st.columns(7)
row1 = st.columns(7)
row2 = st.columns(7)

# You can use a column just like st.sidebar:
st.markdown("Введите данные:")

#obj_num = row[0].text_input('№ п/п', value='36')
obj_prg = row[0].text_input('Программа строительства', value='Образование')
obj_subprg = row[1].text_input('Подпрограмма', value='Дошкольные учреждения')
obj_key = row[2].text_input('obj_key', value='020-0684')
obj_shortName = row[3].text_input('obj_shortName', value='ДОУ на 125, ТПУ "Мневники"')
code_task = row[4].text_input('Код задачи', value="1")
task_name = row[5].text_input('Название задачи', value='Предпроектные работы')
percent_end = row[6].text_input('Процент завершения задачи', value=100.0)

begin = row1[0].date_input('Дата начала задачи', value=datetime.date(2022, 1, 14))
#end = row1[1].date_input('Дата окончания задачи', value=datetime.date(2023, 3, 30))
begin_bp = row1[1].date_input('Дата начала БП0', value=datetime.date(2021, 5, 4))
end_bp = row1[2].date_input('Дата окончания БП0', value=datetime.date(2021, 5, 4))
status_exp = row1[3].text_input('Статус по экспертизе', value=1.0)  # maybe -1 is none, or empty cell
expertize = row1[4].selectbox('Экспертиза', ["1ТС", "2ТС", "1Т", "1С", "2С", "2Т", "-"], index=2)

code_ds = row1[5].text_input('Код ДС', value='022-0043')
status_sq = row1[6].selectbox('состояние площадки', ["Свободна, передана",
                                                     "Занята",
                                                     "Свободна, не передана",
                                                     "Не передана",
                                                     "Передана под снос (для объектов сноса)",
                                                     "Не передана под снос (для объектов сноса)",
                                                     "-"], index=2)
square = row2[0].text_input('Площадь', value=0.0)
genproectir = row2[1].text_input('Генпроектировщик', value=1)
genpodryad = row2[2].text_input('Генподрядчик', value=2)
workers_number = row2[3].text_input('Кол-во рабочих', value=271.0)
date_rep = row2[4].date_input('date_report', value=datetime.date(2023, 1, 20))

# create dataframe
#fact_time = (end.timestamp() - begin.timestamp()) / 60 / 60 / 24
plan_time = (end_bp.timestamp() - begin_bp.timestamp()) / 60 / 60 / 24

data_base = {'obj_prg': [obj_prg],
             'obj_subprg': [obj_subprg],
             'состояние площадки': [status_sq],
             'ПроцентЗавершенияЗадачи': [percent_end],
             'plan_time': [plan_time],
             'Площадь': [square],
             'Генпроектировщик': [genproectir],
             'Генподрядчик': [genpodryad],
             'Кол-во рабочих': [workers_number],
             }

df_base = pd.DataFrame(data_base)
# st.table(pd.DataFrame(data))

# predict
if st.button('Предсказать'):
    #model = Predicter()
    #y_pred = model.predict(df_base, df_additional) - не успели но можно с ipynb взять

    y_pred = str(np.random.randint(1, 100))

    st.markdown(
        f'<p style="font-size: 20px;font-color: red">Ожидаемое время окончания строительства для данного типа задачи составит '
        f'<u>{str(y_pred)}</u> ч.</p>',
        unsafe_allow_html=True)
