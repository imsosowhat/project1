import streamlit as st

# 1. CSS 설정: 중앙 배치 및 버튼 스타일 변경
st.markdown(
    """
    <style>
    /* 메인 화면 배경 설정 */
    .stApp {
        background-color: #FF3333 !important;
        text-align: center !important; /* 모든 텍스트 중앙 정렬 */
    }
    
    /* 모든 텍스트 글자색 흰색 및 중앙 정렬 강제 */
    .stApp h1, .stApp h2, .stApp h3, .stApp p, .stApp span {
        color: white !important;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* 버튼 컨테이너를 중앙으로 정렬 */
    div.stButton {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    
    /* 버튼 자체 스타일 */
    div.stButton > button {
        background-color: white !important; /* 버튼 배경은 흰색 */
        color: #8B0000 !important; /* 글자색은 진한 빨간색 (Deep Red) */
        font-weight: bold !important;
        font-size: 20px !important;
        border: none !important;
        padding: 12px 24px !important;
        border-radius: 10px !important;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
    }
    
    /* 풍선 애니메이션 효과 */
    @keyframes floatUp {
        0% { bottom: -10%; transform: translateX(0) scale(1); opacity: 1; }
        50% { transform: translateX(50px) scale(1.2); }
        100% { bottom: 110%; transform: translateX(-50px) scale(0.8); opacity: 0; }
    }

    .balloon-container {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        overflow: hidden;
        pointer-events: none;
        z-index: 999999;
    }

    .balloon {
        position: fixed;
        bottom: -100px;
        width: 40px;
        height: 50px;
        border-radius: 50% 50% 50% 50% / 40% 40% 60% 60%;
        animation: floatUp 6s infinite linear;
    }

    .balloon::after {
        content: "▲";
        color: inherit;
        font-size: 10px;
        position: absolute;
        bottom: -8px;
        left: 14px;
    }

    .b1 { left: 10%; background-color: #FF5733; animation-duration: 5s; animation-delay: 0s; }
    .b2 { left: 25%; background-color: #FFC300; animation-duration: 7s; animation-delay: 1.5s; }
    .b3 { left: 40%; background-color: #33FF57; animation-duration: 6s; animation-delay: 0.5s; }
    .b4 { left: 55%; background-color: #3357FF; animation-duration: 8s; animation-delay: 2s; }
    .b5 { left: 70%; background-color: #E333FF; animation-duration: 5.5s; animation-delay: 1s; }
    .b6 { left: 85%; background-color: #33FFF3; animation-duration: 6.5s; animation-delay: 2.5s; }
    </style>
    """,
    unsafe_allow_html=True
)

# 2. 세션 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = "first"

# --- 첫 번째 화면 ---
if st.session_state.page == "first":
    st.title("안녕하세요")
    
    if st.button("나도 인사하기"):
        st.session_state.page = "second"
        st.rerun()

# --- 두 번째 화면 ---
elif st.session_state.page == "second":
    st.balloons()
    st.title("첫 웹페이지 제작을 축하해요오오!")
