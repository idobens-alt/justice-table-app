import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="ניהול טבלת צדק - מכרז 44/2025", layout="wide")

st.title("⚖️ מערכת ניהול 'טבלת צדק' - מכרז שב\"ס 44/2025")
st.subheader("חלוקה הוגנת ואיזון משימות בינוי ותשתיות")

# הגדרת נתוני היעד המקוריים לפי חוזה מכרז 44/2025
CONTRACTORS_DATA = [
    # קבוצה 1 - צפון (4 זוכים, 25% לכל אחד)
    {"קבוצה": "קבוצה 1", "אזור": "צפון", "קבלן": "קבלן צפון 1-1", "אחוז_יעד": 25.0},
    {"קבוצה": "קבוצה 1", "אזור": "צפון", "קבלן": "קבלן צפון 1-2", "אחוז_יעד": 25.0},
    {"קבוצה": "קבוצה 1", "אזור": "צפון", "קבלן": "קבלן צפון 1-3", "אחוז_יעד": 25.0},
    {"קבוצה": "קבוצה 1", "אזור": "צפון", "קבלן": "קבלן צפון 1-4", "אחוז_יעד": 25.0},
    # קבוצה 1 - דרום (4 זוכים, 25% לכל אחד)
    {"קבוצה": "קבוצה 1", "אזור": "דרום", "קבלן": "קבלן דרום 1-1", "אחוז_יעד": 25.0},
    {"קבוצה": "קבוצה 1", "אזור": "דרום", "קבלן": "קבלן דרום 1-2", "אחוז_יעד": 25.0},
    {"קבוצה": "קבוצה 1", "אזור": "דרום", "קבלן": "קבלן דרום 1-3", "אחוז_יעד": 25.0},
    {"קבוצה": "קבוצה 1", "אזור": "דרום", "קבלן": "קבלן דרום 1-4", "אחוז_יעד": 25.0},
    # קבוצה 2 - צפון (3 זוכים, 33.33% לכל אחד)
    {"קבוצה": "קבוצה 2", "אזור": "צפון", "קבלן": "קבלן צפון 2-1", "אחוז_יעד": 33.33},
    {"קבוצה": "קבוצה 2", "אזור": "צפון", "קבלן": "קבלן צפון 2-2", "אחוז_יעד": 33.33},
    {"קבוצה": "קבוצה 2", "אזור": "צפון", "קבלן": "קבלן צפון 2-3", "אחוז_יעד": 33.33},
    # קבוצה 2 - דרום (3 זוכים, 33.33% לכל אחד)
    {"קבוצה": "קבוצה 2", "אזור": "דרום", "קבלן": "קבלן דרום 2-1", "אחוז_יעד": 33.33},
    {"קבוצה": "קבוצה 2", "אזור": "דרום", "קבלן": "קבלן דרום 2-2", "אחוז_יעד": 33.33},
    {"קבוצה": "קבוצה 2", "אזור": "דרום", "קבלן": "קבלן דרום 2-3", "אחוז_יעד": 33.33},
    # קבוצה 3 - ארצי (3 זוכים, 33.33% לכל אחד)
    {"קבוצה": "קבוצה 3", "אזור": "ארצי/צפון", "קבלן": "קבלן קבוצה 3-1", "אחוז_יעד": 33.33},
    {"קבוצה": "קבוצה 3", "אזור": "ארצי/צפון", "קבלן": "קבלן קבוצה 3-2", "אחוז_יעד": 33.33},
    {"קבוצה": "קבוצה 3", "אזור": "ארצי/צפון", "קבלן": "קבלן קבוצה 3-3", "אחוז_יעד": 33.33},
]

if "orders" not in st.session_state:
    st.session_state.orders = []

st.sidebar.header("הזנת משימה חדשה")
project_name = st.sidebar.text_input("שם הפרויקט/המתקן")
group = st.sidebar.selectbox("קבוצה", ["קבוצה 1", "קבוצה 2", "קבוצה 3"])

if group in ["קבוצה 1", "קבוצה 2"]:
    region = st.sidebar.selectbox("אזור", ["צפון", "דרום"])
else:
    region = "ארצי/צפון"

amount = st.sidebar.number_input("סכום מוערך בש\"ח (לא כולל מע\"מ)", min_value=1000, step=50000)

def calculate_allocation(group_val, region_val, new_amount):
    relevant_contractors = [c for c in CONTRACTORS_DATA if c["קבוצה"] == group_val and c["אזור"] == region_val]
    active_orders = [o for o in st.session_state.orders if o["סטטוס"] == "מאושר" and o["קבוצה"] == group_val and o["אזור"] == region_val]
    total_existing = sum(o["סכום"] for o in active_orders)
    total_gross = total_existing + new_amount
    
    best_contractor = None
    min_gap = float("inf")
    
    for c in relevant_contractors:
        c_existing = sum(o["סכום"] for o in active_orders if o["קבלן"] == c["קבלן"])
        c_gross_percent = ((c_existing + new_amount) / total_gross) * 100 if total_gross > 0 else 0
        gap = c_gross_percent - c["אחוז_יעד"]
        
        if gap < min_gap:
            min_gap = gap
            best_contractor = c["קבלן"]
            
    return best_contractor

if st.sidebar.button("חשב והקצה עבודה"):
    if project_name:
        winner = calculate_allocation(group, region, amount)
        st.session_state.orders.append({
            "מזהה": len(st.session_state.orders) + 1,
            "שם פרויקט": project_name,
            "קבוצה": group,
            "אזור": region,
            "סכום": amount,
            "קבלן": winner,
            "סטטוס": "מאושר"
        })
        st.sidebar.success(f"הפרויקט הוקצה בהצלחה לקבלן: **{winner}**")
    else:
        st.sidebar.error("יש להזין שם פרויקט")

st.header("תמונת מצב מעודכנת - טבלת צדק")
dashboard_rows = []
for c in CONTRACTORS_DATA:
    active_orders = [o for o in st.session_state.orders if o["סטטוס"] == "מאושר" and o["קבוצה"] == c["קבוצה"] and o["אזור"] == c["אזור"]]
    group_total = sum(o["סכום"] for o in active_orders)
    contractor_total = sum(o["סכום"] for o in active_orders if o["קבלן"] == c["קבלן"])
    
    actual_percent = (contractor_total / group_total * 100) if group_total > 0 else 0.0
    gap = actual_percent - c["אחוז_יעד"]
    
    dashboard_rows.append({
        "קבוצה": c["קבוצה"],
        "אזור": c["אזור"],
        "שם הקבלן": c["קבלן"],
        "אחוז יעד במכרז": f"{c['אחוז_יעד']:.2f}%",
        "תקציב מוקצה (ש\"ח)": f"{contractor_total:,.0f} ₪",
        "אחוז בפועל": f"{actual_percent:.2f}%",
        "פער באחוזים": f"{gap:.2f}%"
    })

st.dataframe(pd.DataFrame(dashboard_rows), use_container_width=True)

st.header("יומן הזמנות עבודה")
if st.session_state.orders:
    st.dataframe(pd.DataFrame(st.session_state.orders), use_container_width=True)
    order_to_cancel = st.selectbox("בחר מזהה משימה לביטול", [o["מזהה"] for o in st.session_state.orders if o["סטטוס"] == "מאושר"])
    if st.button("בטל משימה זו"):
        for o in st.session_state.orders:
            if o["מזהה"] == order_to_cancel:
                o["סטטוס"] = "מבוטל"
        st.success(f"משימה {order_to_cancel} בוטלה!")
        st.rerun()

buffer = io.BytesIO()
with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
    pd.DataFrame(dashboard_rows).to_excel(writer, sheet_name="תמונת מצב", index=False)
    if st.session_state.orders:
        pd.DataFrame(st.session_state.orders).to_excel(writer, sheet_name="יומן הזמנות", index=False)

st.download_button("📥 הורד קובץ Excel מעודכן", buffer.getvalue(), "justice_table_44_2025.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
