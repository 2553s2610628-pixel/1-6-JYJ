import streamlit as st
import datetime

# 페이지 설정
st.set_page_config(
    page_title="오늘의 청소 당번 확인기",
    page_icon="🧹",
    layout="centered"
)

st.title("🧹 오늘의 청소 당번 안내 시스템")
st.markdown("---")

# 기본 정보 정의
TOTAL_MEMBERS = 36
GROUP_SIZE = 5

# 기준 정보 (2026년 6월 12일 금요일 -> 21, 22, 23, 24, 25번)
BASE_DATE = datetime.date(2026, 6, 12)
BASE_START_INDEX = 20  # 파이썬 인덱스 기준 (21번은 index 20)

# 1번부터 36번까지의 멤버 리스트 생성
members = [i for i in range(1, TOTAL_MEMBERS + 1)]

def get_cleaning_days_between(start_date, end_date):
    """두 날짜 사이의 월, 수, 금요일(청소일)의 개수를 계산합니다."""
    count = 0
    current_date = start_date
    
    # 시작일이 종료일보다 뒤에 있는 경우 (과거 날짜 조회 시)
    step = 1 if start_date <= end_date else -1
    
    if step == 1:
        while current_date < end_date:
            # 0:월, 2:수, 4:금
            if current_date.weekday() in [0, 2, 4]:
                count += 1
            current_date += datetime.timedelta(days=1)
    else:
        while current_date > end_date:
            current_date += datetime.timedelta(days=-1)
            if current_date.weekday() in [0, 2, 4]:
                count += 1
                
    return count, step

# 사용자 날짜 입력 (기본값: 오늘)
today = datetime.date.today()
selected_date = st.date_input("🗓️ 청소 당번을 확인할 날짜를 선택하세요:", today)

# 선택한 날짜의 요일 확인 (0:월 ~ 6:일)
weekday_kr = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
selected_weekday = selected_date.weekday()

st.info(f"선택하신 날짜: **{selected_date} ({weekday_kr[selected_weekday]})**")

# 청소일 여부 확인 (월, 수, 금만 청소)
if selected_weekday not in [0, 2, 4]:
    st.warning("⚠️ 해당 날짜는 청소일이 아닙니다! (청소일: 월요일, 수요일, 금요일)")
else:
    # 기준일(6월 12일)로부터 몇 번의 청소일이 지나갔는지(또는 모자란지) 계산
    cleaning_days_diff, direction = get_cleaning_days_between(BASE_DATE, selected_date)
    
    # 총 청소 횟수 변화량에 따른 인덱스 이동량 계산
    # 한 번 청소할 때마다 5명씩 이동
    total_shift = cleaning_days_diff * GROUP_SIZE
    
    if direction == 1:
        start_idx = (BASE_START_INDEX + total_shift) % TOTAL_MEMBERS
    else:
        start_idx = (BASE_START_INDEX - total_shift) % TOTAL_MEMBERS
        if start_idx < 0:
            start_idx += TOTAL_MEMBERS

    # 당번 5명 추출 (36번을 넘어가는 경우 순환 처리)
    duty_members = []
    for i in range(GROUP_SIZE):
        idx = (start_idx + i) % TOTAL_MEMBERS
        duty_members.append(members[idx])

    # 결과 출력
    st.success("🎉 오늘의 청소 당번을 발표합니다!")
    
    # 시각적으로 보기 좋게 폰트 크기 키움
    cols = st.columns(5)
    for index, member in enumerate(duty_members):
        with cols[index]:
            st.metric(label=f"당번 {index+1}", value=f"{member}번")
            
    st.balloons()

# 규칙 안내
st.markdown("---")
with st.expander("📌 청소 운영 규칙 안내"):
    st.write(f"- **총 인원:** {TOTAL_MEMBERS}명 (1번 ~ {TOTAL_MEMBERS}번)")
    st.write(f"- **청소 요일:** 매주 **월요일, 수요일, 금요일**")
    st.write(f"- **청소 인원:** 일일 **{GROUP_SIZE}명**")
    st.write("- **로테이션:** 36번 다음에는 다시 1번으로 돌아와 순환합니다.")
    st.caption("기준 데이터: 2026년 6월 12일(금) -> 21, 22, 23, 24, 25번")
