```python
import streamlit as st

# AI 기능용
try:
    from google import genai
except ImportError:
    genai = None

st.set_page_config(
    page_title="우리반 청소도우미",
    page_icon="🧹",
    layout="wide"
)

# ---------------------------
# Session State 초기화
# ---------------------------
if "notices" not in st.session_state:
    st.session_state.notices = [
        "청소 후 창문을 확인해주세요.",
        "분리수거를 정확히 해주세요."
    ]

# ---------------------------
# 제목
# ---------------------------
st.title("🧹 우리반 청소도우미")
st.caption("우리 반 청소를 더 쉽고 체계적으로 관리해보세요!")

# ---------------------------
# 소개
# ---------------------------
st.subheader("📖 청소앱 소개")

st.info(
    """
    이 앱은 우리 반의 청소 활동을 돕기 위해 만들어졌습니다.

    ✔ 공지사항 확인
    ✔ 청소 체크리스트 관리
    ✔ 청소 진행률 확인
    ✔ AI 청소 도우미에게 질문
    """
)

st.divider()

# ---------------------------
# 공지사항
# ---------------------------
st.subheader("📢 공지사항")

new_notice = st.text_input("새 공지 입력")

col1, col2 = st.columns([1, 5])

with col1:
    if st.button("추가"):
        if new_notice.strip():
            st.session_state.notices.append(new_notice.strip())
            st.success("공지사항이 추가되었습니다.")

if st.session_state.notices:
    for idx, notice in enumerate(st.session_state.notices):
        c1, c2 = st.columns([8, 1])

        with c1:
            st.write(f"• {notice}")

        with c2:
            if st.button("삭제", key=f"delete_{idx}"):
                st.session_state.notices.pop(idx)
                st.rerun()
else:
    st.write("등록된 공지사항이 없습니다.")

st.divider()

# ---------------------------
# 체크리스트
# ---------------------------
st.subheader("✅ 청소 체크리스트")

tasks = [
    "교실 바닥 청소",
    "칠판 깨끗이 지우기",
    "쓰레기통 비우기",
    "창문 주변 정리",
    "책상 정돈하기"
]

checked_count = 0

for task in tasks:
    checked = st.checkbox(task)
    if checked:
        checked_count += 1

progress = checked_count / len(tasks)

st.progress(progress)

st.metric(
    "청소 완료율",
    f"{int(progress * 100)}%"
)

# ---------------------------
# 청소 완료 축하 이벤트
# ---------------------------
if checked_count == len(tasks):
    st.success("🎉 모든 청소가 완료되었습니다! 수고했어요!")
    st.balloons()

    st.markdown(
        """
        ## 🏆 청소 미션 성공!

        모두의 노력 덕분에 교실이 깨끗해졌습니다.

        ✨ 오늘도 수고 많았어요!
        """
    )

st.divider()

# ---------------------------
# AI 청소 도우미
# ---------------------------
st.subheader("🤖 AI 청소 도우미")

question = st.text_input(
    "청소와 관련된 질문을 입력하세요"
)

if st.button("질문하기"):

    if not question.strip():
        st.warning("질문을 입력해주세요.")

    elif genai is None:
        st.error(
            "google-genai 라이브러리가 설치되지 않았습니다."
        )

    else:
        try:
            api_key = st.secrets["GEMINI_API_KEY"]

            client = genai.Client(
                api_key=api_key
            )

            prompt = f"""
            당신은 학교 청소 도우미 AI입니다.

            학생들이 교실 청소를 잘 할 수 있도록
            쉽고 친절하게 설명하세요.

            질문:
            {question}
            """

            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=prompt
            )

            st.success("답변")

            st.write(response.text)

        except KeyError:
            st.error(
                "Secrets에 GEMINI_API_KEY가 설정되지 않았습니다."
            )

        except Exception as e:
            st.error(
                f"AI 응답 중 오류가 발생했습니다.\n\n{e}"
            )

st.divider()

st.caption(
    "우리반 청소도우미 | Streamlit Community Cloud 배포 가능"
)
```
