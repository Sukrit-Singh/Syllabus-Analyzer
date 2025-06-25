import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

st.set_page_config(page_title="📘 Syllabus Tracker & Analyzer", layout="wide")
st.title("📘 Syllabus Tracker & Analyzer")

uploaded_file = st.file_uploader("📁 Upload your syllabus CSV file", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("✅ CSV Loaded Successfully!")
    except Exception as e:
        st.error(f"❌ Failed to read CSV: {e}")
        df = None
else:
    df = None

if df is not None:
    st.write("Detected Columns:", df.columns.tolist())

    if not {'Subject', 'Topic', 'Status'}.issubset(df.columns):
        st.error("❗ CSV must have at least 'Subject', 'Topic', and 'Status' columns.")
    else:
        tab1, tab2 = st.tabs(["✏️ Tracker", "📊 Analyzer"])

        # ========== TRACKER TAB ==========
        with tab1:
            st.subheader("✏️ Edit Syllabus Status")

            edited_statuses = []
            for i, row in df.iterrows():
                col1, col2, col3, col4 = st.columns([3, 3, 2, 2])
                with col1:
                    st.text(row.get('Subject', 'N/A'))
                with col2:
                    st.text(row.get('Topic', 'N/A'))
                with col3:
                    st.text(f"Week {row.get('Week', 'N/A')}")
                with col4:
                    current_status = row.get('Status', 'Pending')
                    new_status = st.selectbox(
                        f"Status for {row.get('Topic', 'Unknown')}:", 
                        ["Pending", "Completed", "In Progress"], 
                        index=["Pending", "Completed", "In Progress"].index(current_status)
                            if current_status in ["Pending", "Completed", "In Progress"] else 0,
                        key=f"status_{i}"
                    )
                    edited_statuses.append(new_status)

            df['Status'] = edited_statuses

            st.subheader("💾 Download Updated CSV")
            buffer = io.StringIO()
            df.to_csv(buffer, index=False)
            st.download_button(
                label="Download CSV",
                data=buffer.getvalue(),
                file_name="updated_syllabus.csv",
                mime="text/csv"
            )

        # ========== ANALYZER TAB ==========
        with tab2:
            st.subheader("📊 Analyze Syllabus Progress")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**📚 Topics per Subject**")
                subject_count = df.groupby('Subject')['Topic'].count()
                st.bar_chart(subject_count)

                if 'Week' in df.columns:
                    st.markdown("**📅 Topics by Week**")
                    week_dist = df.groupby('Week')['Topic'].count()
                    st.line_chart(week_dist)
                else:
                    st.info("🛈 No 'Week' column found in your CSV.")

            with col2:
                st.markdown("**📈 Completion Status**")
                status_count = df['Status'].value_counts()
                fig1, ax1 = plt.subplots()
                ax1.pie(status_count, labels=status_count.index, autopct='%1.1f%%', startangle=90)
                ax1.axis('equal')
                st.pyplot(fig1)

                st.markdown("**✅ Progress by Subject**")
                completed = df[df['Status'].str.lower() == 'completed']
                total = df.groupby('Subject')['Topic'].count()
                done = completed.groupby('Subject')['Topic'].count()
                progress_df = pd.DataFrame({'Completed': done, 'Total': total})
                progress_df.fillna(0, inplace=True)
                progress_df['Completed'] = progress_df['Completed'].astype(int)
                progress_df['Total'] = progress_df['Total'].astype(int)
                progress_df['% Completed'] = (progress_df['Completed'] / progress_df['Total']) * 100
                st.dataframe(
                    progress_df.style.format({
                        "Completed": "{:.0f}",
                        "Total": "{:.0f}",
                        "% Completed": "{:.1f}"
                    })
                )
                st.bar_chart(progress_df['% Completed'])

else:
    st.info("👆 Please upload a valid CSV file to begin.")
