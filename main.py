import streamlit as st
from langchain_openai import ChatOpenAI  # ❗️ [수정] ChatOpenAI를 직접 임포트
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os # ❗️ [추가] os 모듈 추가 (Secrets를 위해)

# ❗️ [수정] ChatOpenAI를 표준 방식으로 초기화
# API 키는 Streamlit Cloud의 Secrets에서 자동으로 읽어옵니다. (os.getenv("OPENAI_API_KEY") 방식)
llm = ChatOpenAI(model="gpt-4o-mini")

# 프롬프트 템플릿 생성
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])

# 문자열 출력 파서
output_parser = StrOutputParser()

# LLM 체인 구성
chain = prompt | llm | output_parser

# --- Streamlit UI ---

# 제목
st.title("인공지능 시인")

# 시 주제 입력 필드
content = st.text_input("시의 주제를 제시해주세요")

# 시 작성 요청하기
if content:
    if st.button("시 작성 요청하기"):
        with st.spinner('시를 작성 중입니다...'):
            try:
                # ❗️ [수정] content가 비어있지 않을 때만 실행하도록 로직 변경
                result = chain.invoke({"input": content + "에 대한 시를 써줘"})
                st.write(result)
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
