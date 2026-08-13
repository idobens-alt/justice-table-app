import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="ניהול טבלת צדק - מכרז 44/2025", layout="wide")

st.title("⚖️ מערכת ניהול 'טבלת צדק' - מכרז שב\"ס 44/2025")
st.subheader("חלוקה הוגנת, אישור משימות ואיזון ניצול תקציבי (נתוני גיליון מקרא 12.8)")

# נתוני הקבלנים והאחוזים המקוריים לפי נתחי המכרז
CONTRACTORS_DATA = [
    # קבוצה 1 - צפון
    {"קבוצה": "קבוצה 1", "אזור": "צפון", "דירוג": "זוכה 1", "קבלן": "מ.מיכאלי", "אחוז_יעד": 40.0},
    {"קבוצה": "קבוצה 1", "אזור": "צפון", "דירוג": "זוכה 2", "קבלן": "מיכאל את דוד", "אחוז_יעד": 30.0},
    {"קבוצה": "קבוצה 1", "אזור": "צפון", "דירוג": "זוכה 3", "קבלן": "רום בילדינג", "אחוז_יעד": 20.0},
    {"קבוצה": "קבוצה 1", "אזור": "צפון", "דירוג": "זוכה 4", "קבלן": "דלויה", "אחוז_יעד": 10.0},
    # קבוצה 1 - דרום
    {"קבוצה": "קבוצה 1", "אזור": "דרום", "דירוג": "זוכה 1", "קבלן": "מ.מיכאלי", "אחוז_יעד": 40.0},
    {"קבוצה": "קבוצה 1", "אזור": "דרום", "דירוג": "זוכה 2", "קבלן": "מיכאל את דוד", "אחוז_יעד": 30.0},
    {"קבוצה": "קבוצה 1", "אזור": "דרום", "דירוג": "זוכה 3", "קבלן": "מחלב", "אחוז_יעד": 20.0},
    {"קבוצה": "קבוצה 1", "אזור": "דרום", "דירוג": "זוכה 4", "קבלן": "דלויה", "אחוז_יעד": 10.0},
    # קבוצה 2 - צפון
    {"קבוצה": "קבוצה 2", "אזור": "צפון", "דירוג": "זוכה 1", "קבלן": "ביטוליט", "אחוז_יעד": 50.0},
    {"קבוצה": "קבוצה 2", "אזור": "צפון", "דירוג": "זוכה 2", "קבלן": "י. ינקוביץ", "אחוז_יעד": 30.0},
    {"קבוצה": "קבוצה 2", "אזור": "צפון", "דירוג": "זוכה 3", "קבלן": "נ. טמיר", "אחוז_יעד": 20.0},
    # קבוצה 2 - דרום
    {"קבוצה": "קבוצה 2", "אזור": "דרום", "דירוג": "זוכה 1", "קבלן": "נ. טמיר", "אחוז_יעד": 50.0},
    {"קבוצה": "קבוצה 2", "אזור": "דרום", "דירוג": "זוכה 2", "קבלן": "ביטוליט", "אחוז_יעד": 30.0},
    {"קבוצה": "קבוצה 2", "אזור": "דרום", "דירוג": "זוכה 3", "קבלן": "י.ר.נ", "אחוז_יעד": 20.0},
    # קבוצה 3 - ארצי
    {"קבוצה": "קבוצה 3", "אזור": "ארצי/צפון", "דירוג": "זוכה 1", "קבלן": "מנרב", "אחוז_יעד": 60.0},
    {"קבוצה": "קבוצה 3", "אזור": "ארצי/צפון", "דירוג": "זוכה 2", "קבלן": "נרשא", "אחוז_יעד": 40.0},
]

# פרויקטים מאושרים ומחולקים לפי גיליון מקרא מעודכן
INITIAL_ORDERS = [
    # קבוצה 1 צפון
    {"מזהה": 1, "שם פרויקט": "הקצאת בסיס צפון - מ.מיכאלי", "קבוצה": "קבוצה 1", "אזור": "צפון", "סכום": 9558000, "קבלן": "מ.מיכאלי", "סטטוס": "עלתה הזמנה"},
    {"מזהה": 2, "שם פרויקט": "הקצאת בסיס צפון - מיכאל את דוד", "קבוצה": "קבוצה 1", "אזור": "צפון", "סכום": 7000000, "קבלן": "מיכאל את דוד", "סטטוס": "עלתה הזמנה"},
    {"מזהה": 3, "שם פרויקט": "הקצאת בסיס צפון - רום בילדינג", "קבוצה": "קבוצה 1", "אזור": "צפון", "סכום": 4853000, "קבלן": "רום בילדינג", "סטטוס": "עלתה הזמנה"},
    {"מזהה": 4, "שם פרויקט": "הקצאת בסיס צפון - דלויה", "קבוצה": "קבוצה 1", "אזור": "צפון", "סכום": 2372000, "קבלן": "דלויה", "סטטוס": "עלתה הזמנה"},
    
    # קבוצה 1 דרום
    {"מזהה": 5, "שם פרויקט": "הקצאת בסיס דרום - מ.מיכאלי", "קבוצה": "קבוצה 1", "אזור": "דרום", "סכום": 11040000, "קבלן": "מ.מיכאלי", "סטטוס": "עלתה הזמנה"},
    {"מזהה": 6, "שם פרויקט": "הקצאת בסיס דרום - מיכאל את דוד", "קבוצה": "קבוצה 1", "אזור": "דרום", "סכום": 8280000, "קבלן": "מיכאל את דוד", "סטטוס": "עלתה הזמנה"},
    {"מזהה": 7, "שם פרויקט": "הקצאת בסיס דרום - מחלב", "קבוצה": "קבוצה 1", "אזור": "דרום", "סכום": 5550700, "קבלן": "מחלב", "סטטוס": "עלתה הזמנה"},
    {"מזהה": 8, "שם פרויקט": "הקצאת בסיס דרום - דלויה", "קבוצה": "קבוצה 1", "אזור": "דרום", "סכום": 2780000, "קבלן": "דלויה", "סטטוס": "עלתה הזמנה"},
    
    # קבוצה 2 דרום
    {"מזהה": 9, "שם פרויקט": "מגן - בינוי תחנת משנה", "קבוצה": "קבוצה 2", "אזור": "דרום", "סכום": 8450000, "קבלן": "נ. טמיר", "סטטוס": "עלתה הזמנה"}
]

if "orders" not in st.session_state:
    st.session_state.orders = INITIAL_ORDERS

# סרגל צד - הזנת משימה חדשה
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
    active_orders = [o for o in st.session_state.orders if o["סטטוס"] in ["מאושר", "עלתה הזמנה"] and o["קבוצה"] == group_val and o["אזור"] == region_val]
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

if st.sidebar.button("1. חשב והצג ספק מומלץ (הבא בתור)"):
    if project_name:
        recommended_winner = calculate_allocation(group, region, amount)
        st.session_state.pending_project = {
            "שם פרויקט": project_name,
            "קבוצה": group,
            "אזור": region,
            "סכום": amount,
            "קבלן": recommended_winner
        }
    else:
        st.sidebar.error("יש להזין שם פרויקט")

if "pending_project" in st.session_state and st.session_state.pending_project:
    p = st.session_state.pending_project
    st.sidebar.info(f"📍 **תוצאת חישוב:**\nהספק המומלץ לפי כללי המכרז: **{p['קבלן']}**")
    if st.sidebar.button("2. אישור והוספה רשמית לטבלה"):
        new_id = len(st.session_state.orders) + 1
        st.session_state.orders.append({
            "מזהה": new_id,
            "שם פרויקט": p["שם פרויקט"],
            "קבוצה": p["קבוצה"],
            "אזור": p["אזור"],
            "סכום": p["סכום"],
            "קבלן": p["קבלן"],
            "סטטוס": "מאושר"
        })
        st.sidebar.success(f"פרויקט מזהה {new_id} אושר והתווסף בהצלחה לטבלה!")
        st.session_state.pending_project = None
        st.rerun()

# תמונת מצב מעודכנת
st.header("תמונת מצב מעודכנת - טבלת צדק (גיליון מקרא)")
dashboard_rows = []
for c in CONTRACTORS_DATA:
    active_orders = [o for o in st.session_state.orders if o["סטטוס"] in ["מאושר", "עלתה הזמנה"] and o["קבוצה"] == c["קבוצה"] and o["אזור"] == c["אזור"]]
    group_total = sum(o["סכום"] for o in active_orders)
    contractor_total = sum(o["סכום"] for o in active_orders if o["קבלן"] == c["קבלן"])
    
    actual_percent = (contractor_total / group_total * 100) if group_total > 0 else 0.0
    gap = actual_percent - c["אחוז_יעד"]
    
    target_budget = (c["אחוז_יעד"] / 100.0) * group_total
    remaining_balance = contractor_total - target_budget
    
    dashboard_rows.append({
        "קבוצה": c["קבוצה"],
        "אזור": c["אזור"],
        "דירוג": c["דירוג"],
        "שם הקבלן": c["קבלן"],
        "נתח יעד במכרז": f"{c['אחוז_יעד']:.2f}%",
        "תקציב מוקצה בפועל (ש\"ח)": f"{contractor_total:,.0f} ₪",
        "אחוז ניצול בקבוצה": f"{actual_percent:.2f}%",
        "פער באחוזים": f"{gap:.2f}%",
        "פער כספי (ש\"ח)": f"{remaining_balance:+,.0f} ₪"
    })

st.dataframe(pd.DataFrame(dashboard_rows), use_container_width=True)

# יומן הזמנות ועדכון סטטוס משימות
st.header("יומן הזמנות עבודה וניהול סטטוסים")
if st.session_state.orders:
    df_orders = pd.DataFrame(st.session_state.orders)
    st.dataframe(df_orders, use_container_width=True)
    
    st.subheader("עדכון סטטוס משימה קיימת (למשל: 'עלתה הזמנה' / 'מבוטל')")
    col1, col2, col3 = st.columns(3)
    with col1:
        selected_id = st.selectbox("בחר מזהה משימה", [o["מזהה"] for o in st.session_state.orders])
    with col2:
        new_status = st.selectbox("בחר סטטוס חדש", ["מאושר", "עלתה הזמנה", "בתהליך אישור", "מבוטל"])
    with col3:
        st.write("")
        st.write("")
        if st.button("עדכן סטטוס משימה"):
            for o in st.session_state.orders:
                if o["מזהה"] == selected_id:
                    o["סטטוס"] = new_status
            st.success(f"משימה {selected_id} עודכנה לסטטוס: {new_status}")
            st.rerun()

# ייצוא קובץ Excel פיזי מעודכן
buffer = io.BytesIO()
with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
    pd.DataFrame(dashboard_rows).to_excel(writer, sheet_name="תמונת מצב", index=False)
    if st.session_state.orders:
        pd.DataFrame(st.session_state.orders).to_excel(writer, sheet_name="יומן הזמנות", index=False)

st.download_button("📥 הורד קובץ Excel מעודכן", buffer.getvalue(), "justice_table_44_2025.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
