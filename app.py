Python
import random
import streamlit as st

st.set_page_config(page_title="오늘의 점심 추천", page_icon="🍱")

st.title("🍱 오늘 뭐 먹지? 점심 메뉴 추천기")
st.write("버튼을 누르면 오늘의 점심 메뉴를 랜덤으로 골라드립니다!")

lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈가스",
    "짜장면",
    "짬뽕",
    "초밥",
    "쌀국수",
    "햄버거",
    "비빔밥",
    "순대국밥",
    "파스타",
    "떡볶이",
    "칼국수",
    "샐러드",
]

if st.button("오늘의 메뉴 추천받기 🎲", type="primary"):
  selected_menu = random.choice(lunch_menus)
  st.success(f"오늘의 추천 점심 메뉴는 **{selected_menu}**입니다! 맛있게 드세요 😋")
