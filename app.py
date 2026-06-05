import streamlit as st
from google import genai
from google.genai import types

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="연애상담 챗봇",
    page_icon="💕",
    layout="centered"
)

st.title("💕 연애상담 챗봇")
st.caption("Gemini 2.5 Flash Lite 기반")

# -----------------------------
# API 키 불러오기
# -----------------------------
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error("GEMINI_API_KEY가 설정되지 않았습니다.")
    st.stop()

# -----------------------------
# Gemini 클라이언트
# -----------------------------
try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error(f"Gemini 클라이언트 생성 실패: {e}")
    st.stop()

# -----------------------------
# 세션 상태 초기화
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "안녕하세요 😊\n\n"
                "연애 고민, 썸, 이별, 재회, 장거리 연애 등 "
                "편하게 이야기해 주세요."
            )
        }
    ]

# -----------------------------
# 기존 대화 표시
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# 시스템 프롬프트
# -----------------------------
SYSTEM_PROMPT = """
당신은 공감 능력이 좋은 연애상담 전문 AI입니다.

원칙:
1. 사용자의 감정을 존중한다.
2. 비난하거나 단정하지 않는다.
3. 현실적이고 건강한 관계를 우선한다.
4. 상대방의 입장도 균형 있게 고려한다.
5. 짧은 답변보다 구체적이고 실용적인 조언을 제공한다.
6. 사용자가 위험한 상황(폭력, 스토킹, 협박 등)에 있다면 안전을 우선으로 안내한다.
7. 답변은 한국어로 한다.
"""

# -----------------------------
# 사용자 입력
# -----------------------------
if prompt := st.chat_input("연애 고민을 입력하세요..."):

    # 사용자 메시지 저장
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Gemini에 전달할 대화 구성
    conversation_text = ""

    for msg in st.session_state.messages:
        role = "사용자" if msg["role"] == "user" else "상담사"
        conversation_text += f"{role}: {msg['content']}\n"

    full_prompt = f"""
{SYSTEM_PROMPT}

아래는 지금까지의 대화입니다.

{conversation_text}

상담사:
"""

    try:
        with st.chat_message("assistant"):
            with st.spinner("생각 중..."):

                response = client.models.generate_content(
                    model="gemini-2.5-flash-lite",
                    contents=full_prompt,
                    config=types.GenerateContentConfig(
                        temperature=0.8,
                        max_output_tokens=1000,
                    ),
                )

                answer = response.text

                st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    except Exception as e:
        error_msg = (
            "죄송합니다. 응답 생성 중 오류가 발생했습니다.\n\n"
            f"오류 내용: {str(e)}"
        )

        with st.chat_message("assistant"):
            st.error(error_msg)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": error_msg
            }
        )
