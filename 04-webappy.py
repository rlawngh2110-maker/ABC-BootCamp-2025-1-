from dotenv import load_dotenv
import streamlit as st
from ai import get_personality_analysis

load_dotenv()

st.title("🔮 AI 관상 보기 프로그램")
st.write("---")
st.write("🖐️ 안녕하세요! AI 관상가입니다.")

face_desc = st.text_area("🙃 얼굴 특징을 입력해주세요.")
face_desc = face_desc.strip()

if st.button("🔍 관상 보기", type = "primary"):
    if face_desc:
        with st.spinner("관상을 분석 중입니다..."):
            result = get_personality_analysis(face_desc)
            st.write("----")
            st.write("관상 분석이 끝났습니다! 확인해보세요 ✅")
            st.info(result)
    else:
        st.warning("⚠️ 얼굴 특징을 입력하고 관상보기 버튼을 눌러주세요!")
