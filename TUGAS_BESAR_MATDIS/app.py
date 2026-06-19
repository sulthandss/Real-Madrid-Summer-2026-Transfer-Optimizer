import streamlit as st
import pandas as pd

st.set_page_config(page_title="Real Madrid Transfer Optimizer", layout="wide")

st.title(" Real Madrid Summer 2026 Transfer Optimizer")
st.write("Aplikasi ini menggunakan algoritma 0/1 Knapsack (Dynamic Programming) untuk mencari kombinasi pemain terbaik berdasarkan Indeks Kecocokan Taktis (TFI) dan batas anggaran.")

players_data = [
    {"name": "Enzo Fernández", "cost": 140, "tfi": 86, "pos": "CM", "image": "foto/enzo.jpg"},
    {"name": "Rúben Dias", "cost": 100, "tfi": 94, "pos": "CB", "image": "foto/rubendias.jpg"},
    {"name": "Alessandro Bastoni", "cost": 85, "tfi": 91, "pos": "CB", "image": "foto/bastoni.jpg"},
    {"name": "João Neves", "cost": 80, "tfi": 87, "pos": "DM", "image": "foto/neves.jpg"},
    {"name": "Vitinha", "cost": 70, "tfi": 79, "pos": "CM", "image": "foto/vitinha.jpg"},
    {"name": "Nico Schlotterbeck", "cost": 62, "tfi": 77, "pos": "CB", "image": "foto/nico.jpg"},
    {"name": "Bernardo Silva", "cost": 55, "tfi": 84, "pos": "AM", "image": "foto/bernardo.jpg"},
    {"name": "Denzel Dumfries", "cost": 48, "tfi": 72, "pos": "RB", "image": "foto/dumfries.jpg"},
    {"name": "Tomás Araújo", "cost": 40, "tfi": 68, "pos": "CB", "image": "foto/araujo.jpg"},
    {"name": "Nico Paz", "cost": 20, "tfi": 64, "pos": "AM", "image": "foto/nicopaz.jpg"}
]

st.sidebar.header(" Pengaturan Strategi")
budget = st.sidebar.slider("Anggaran Transfer (Juta Euro)", min_value=50, max_value=300, value=200, step=10)

st.write("### Daftar Target Transfer")
df = pd.DataFrame(players_data)
st.dataframe(df[['name', 'pos', 'cost', 'tfi']], use_container_width=True)

def knapsack_dp(players, W):
    n = len(players)
    C = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # Membangun tabel C[i][w]
    for i in range(1, n + 1):
        for w in range(W + 1):
            cost = players[i-1]['cost']
            tfi = players[i-1]['tfi']
            
            if cost > w:
                C[i][w] = C[i-1][w]
            else:
                C[i][w] = max(C[i-1][w], tfi + C[i-1][w - cost])
                
    # Backtracking untuk menemukan skuad
    w = W
    squad = []
    for i in range(n, 0, -1):
        if C[i][w] != C[i-1][w]:
            squad.append(players[i-1])
            w -= players[i-1]['cost']
            
    return C[n][W], squad

# Hitung Skuad Optimal
max_tfi, optimal_squad = knapsack_dp(players_data, budget)

st.markdown("---")
st.write(f"###  Skuad Optimal untuk Anggaran €{budget}M")

if not optimal_squad:
    st.warning("Anggaran terlalu kecil untuk merekrut pemain mana pun.")
else:
    col1, col2, col3 = st.columns(3)
    col1.metric("Total TFI", max_tfi)
    total_spent = sum(p['cost'] for p in optimal_squad)
    col2.metric("Total Pengeluaran", f"€{total_spent}M")
    col3.metric("Sisa Anggaran", f"€{budget - total_spent}M")
    st.write("#### Pemain yang Direkrut:")
    
    jumlah_kolom = max(len(optimal_squad), 4) 
    cols = st.columns(jumlah_kolom)
    
    for idx, player in enumerate(optimal_squad):
        with cols[idx]:
            # Kita batasi ukuran gambarnya
            st.image(player['image'], caption=f"{player['name']} ({player['pos']})", use_container_width=True)
            st.success(f"Biaya: €{player['cost']}M | TFI: {player['tfi']}")