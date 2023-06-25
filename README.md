В качестве решения данного кейса мы представляем приложение, которое рассчитывает сроки по основным задачам хода строительства. В прогнозе данная система учитывает различные факторы и риски: тип объекта, состояние площадки, время года и т.д.
Интерфейс приложения позволяет каждому участнику проекта заполнить форму необходимой информацией по строительным работам и получить предположительную дату окончания строительства.

Стек решения: для прогнозирования использовались CatBoost, XGBoost, LightGBM, ETNA; для создания интерфейса — Streamlit

Уникальность нашего решения в универсальности ввода данных: пользователь может как подгрузить данные в формате csv, так и заполнить форму вручную. А так же реализована интерпретация результатов с обозначением степени важности влияющих на строительство факторов.

Ссылка на сайт с демо: https://building-hack-ravwxhmc2hp.streamlit.app/
