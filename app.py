import streamlit as st

# 1. 전체 화면을 빨간색 배경으로 만드는 CSS 설정
st.markdown(
    """
    <style>
    /* 메인 화면 배경 및 텍스트 색상 설정 */
    .stApp {
        background-color: #FF3333 !important;
        color: white !important;
    }
    
    /* 버튼 스타일 커스텀 (빨간 배경에서도 잘 보이도록) */
    div.stButton > button {
        background-color: white !important;
        color: #FF3333 !important;
        font-weight: bold !important;
        border: none !important;
        padding: 10px 20px !important;
        border-radius: 8px !important;
    }
    
    /* 끊임없이 올라가는 알록달록 풍선 애니메이션 효과 */
    @keyframes floatUp {
        0% {
            bottom: -10%;
            transform: translateX(0) scale(1);
            opacity: 1;
        }
        50% {
            transform: translateX(50px) scale(1.2);
        }
        100% {
            bottom: 110%;
            transform: translateX(-50px) scale(0.8);
            opacity: 0;
        }
    }

    .balloon-container {
        position: fixed;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        overflow: hidden;
        pointer-events: none;
        z-index: 9999;
    }

    .balloon {
        position: absolute;
        width: 40px;
        height: 50px;
        border-radius: 50% 50% 50% 50% / 40% 40% 60% 60%;
        animation: floatUp 6s infinite linear;
    }

    /* 풍선 꼬리 부분 */
    .balloon::after {
        content: "▲";
        color: inherit;
        font-size: 10px;
        position: absolute;
        bottom: -8px;
        left: 14px;
    }

    /* 각 풍선의 색상, 크기, 속도, 위치 다양화 */
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

# 2. 화면 전환을 위한 세션 상태(Session State) 초기화
if "page" not in st.session_state:
    st.session_state.page = "first"

# --- 첫 번째 화면 ---
if st.session_state.page == "first":
    st.title("안녕하세요")
    
    # 버튼을 누르면 세션 상태를 'second'로 변경
    if st.button("나도 인사하기"):
        st.session_state.page = "second"
        st.rerun()

# --- 두 번째 화면 ---
elif st.session_state.page == "second":
    st.title("첫 웹페이지 제작을 축하해요오오!")
    
    # HTML 무한 풍선 애니메이션 삽입
    st.markdown(
        """
        <div class="balloon-container">
            <div class="balloon b1"></div>
            <div class="balloon b2"></div>
            <div class="balloon b3"></div>
            <div class="balloon b4"></div>
            <div class="balloon b5"></div>
            <div class="balloon b6"></div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # 처음으로 돌아가는 버튼 (선택 사항)
    st.write("")
    if st.button("처음으로 돌아가기"):
        st.session_state.page = "first"
        st.rerun()
