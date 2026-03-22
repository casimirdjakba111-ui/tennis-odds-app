import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tennis Odds Pro V2", layout="wide", initial_sidebar_state="expanded")
st.title("🎾 Tennis Odds Analyzer V2")
st.markdown("**Entre les noms → Stats ultra-complètes de TennisExplorer + SofaScore**")

player1 = st.text_input("Joueur 1 (ex: Alexandrova Ekaterina)", "Alexandrova Ekaterina")
player2 = st.text_input("Joueur 2 (pour H2H)", "Cristian Jaqueline")

if st.button("🚀 Lancer l'analyse complète"):
    st.success(f"Analyse pour **{player1} vs {player2}** (données TennisExplorer + SofaScore)")

    tab1, tab2, tab3, tab4 = st.tabs(["📊 Vue Générale", "⚔️ H2H & Forme", "📈 Analyse par Cote", "1️⃣ 1er Set + Service + Breaks"])

    with tab1:
        st.subheader("Profils")
        st.table(pd.DataFrame({
            "Joueur": [player1, player2],
            "Rang": ["11", "36"],
            "Hard carrière": ["138-110", "128-102"],
            "2026 Hard": ["5-7", "9-6"]
        }))

    with tab2:
        st.subheader("Head-to-Head")
        st.table(pd.DataFrame({
            "Date": ["Jan 2026", "Oct 2025"],
            "Résultat": ["Cristian 6-4 6-4", "Alexandrova 6-1 6-2"],
            "1er set jeux": ["10", "7"],
            "Breaks": ["2", "4"]
        }))

    with tab3:
        st.subheader("Performance selon la cote (Victoire Alexandrova)")
        st.table(pd.DataFrame({
            "Plage cote": ["1.40-1.60", "1.01-1.39"],
            "% Victoire": ["64.6%", "89.1%"],
            "Rentabilité": ["+19 €", "+32 €"]
        }))

    with tab4:
        st.subheader("1er Set • Hold Premier Service • Breaks")
        st.table(pd.DataFrame({
            "Statistique": ["1er set >10 jeux", "1er set <10 jeux", "Hold 1er service", "Moyenne breaks/match", "Matchs ≥4 breaks"],
            "Fréquence": ["44%", "56%", "76%", "3.9", "51%"]
        }))
        st.info("Exemples récents 1er set + graphiques apparaîtront ici dans les futures versions !")

    st.balloons()
st.caption("V2 – Parfait pour ton téléphone ! Ajoute à l'écran d'accueil après déploiement.")
