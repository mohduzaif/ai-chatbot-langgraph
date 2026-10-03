import streamlit as st


def load_style():

    st.markdown(
        """
        <style>

        /* =========================
           SIDEBAR
           ========================= */

        [data-testid="stSidebar"] .block-container {
            padding-top: 0.5rem;
        }


        /* =========================
           AI ASSISTANT TITLE
           ========================= */

        .sidebar-title {
            font-size: 25px;
            font-weight: 600;

            margin-top: -55px;
            margin-left: 5px;
            margin-bottom: 15px;
        }


        /* =========================
           NEW CHAT BUTTON
           ========================= */

        [data-testid="stSidebar"] button[kind="primary"] {

            width: 130px;
            margin-left: 15px;

            padding: 10px 18px;

            background-color: #4F46E5;
            color: white;

            border: none;
            border-radius: 5px;

            font-size: 16px;
            font-weight: 500;
        }


        [data-testid="stSidebar"] button[kind="primary"]:hover {

            background-color: #6366F1;
            color: white;

            border: none;
        }


        /* =========================
           MY CONVERSATION
           ========================= */

        .conversation-box {

            background-color: #30313D;

            padding: 12px 15px;

            border-radius: 5px;

            margin-top: 15px;
            margin-bottom: 5px;

            color: white;

            font-size: 15px;
            font-weight: 500;
        }


        /* =========================
           CHAT THREAD BUTTONS
           ========================= */

        [data-testid="stSidebar"] button[kind="secondary"] {

            width: 100%;
            margin-left: 0;

            padding: 8px 12px;

            background-color: #30313D;
            color: white;

            border: none;
            border-radius: 5px;

            font-size: 14px;
            font-weight: 400;

            text-align: left;

            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;

            transition: background-color 0.2s ease;
        }


        /* =========================
           THREAD HOVER
           ========================= */

        [data-testid="stSidebar"] button[kind="secondary"]:hover {

            background-color: #3A3B49;
            color: white;

            border: none;
        }


        </style>
        """,
        unsafe_allow_html=True
    )