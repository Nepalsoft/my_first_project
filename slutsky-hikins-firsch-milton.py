import matplotlib.pyplot as plt
import numpy as np

# ग्राफको सेटअप
plt.figure(figsize=(11, 8.5))
plt.title("Pure Substitution Analysis: Slutsky, Hicks & Frisch Models\n(Wage Increase Exploration)", fontsize=13, fontweight='bold')
plt.xlabel("Leisure Hours / आराम गर्ने समय (L)", fontsize=11)
plt.ylabel("Consumption / उपभोग खर्च ($)", fontsize=11)

# कुल समय र ज्याला (Regular vs Windfall Rate)
total_time = 24
w_old = 10       
w_new = 15       

# १. बजेट रेखाहरू (Budget Lines)
leisure = np.linspace(0, total_time, 100)
budget_old = w_old * (total_time - leisure)
budget_new = w_new * (total_time - leisure)

# २. मुख्य बिन्दुहरू (Equilibrium Points)
L_A, C_A = 16, 80   # बिन्दु A: पुरानो बास्कट (Deserved Baseline)

# Hicksian Point (Old Blanket - Same Utility, Constant Happiness)
L_H, C_H = 13.5, 105 

# Slutsky Point (Spendthrift - Compensated Budget passing through A)
L_S, C_S = 14.2, 115 
budget_slutsky = C_A + w_new * (L_A - leisure)

# Frisch Econometric Trend (Filtered Actual Path)
# राग्नार फ्रिसको मोडेलले यो प्रतिस्थापनको वास्तविक तथ्याङ्कीय प्रवृत्ति (Trend Line) लाई मापन गर्छ
L_F, C_F = 14.8, 98

# ३. रेखाहरू प्लट गर्ने
plt.plot(leisure, budget_old, label="Original Budget (Old Wage)", color='gray', linestyle='--')
plt.plot(leisure, budget_new, label="Potential Budget (1.5x Wage)", color='blue', alpha=0.3, linestyle='--')
plt.plot(leisure, budget_slutsky, label="Slutsky Compensated Budget Line", color='purple', linestyle=':')

# ४. इन्डिफरेन्स कर्भ (Hicksian Utility Curve U1)
ic_leisure = np.linspace(11, 21, 100)
ic_old = C_A + 0.85 * (ic_leisure - L_A)**2 - 4.2 * (ic_leisure - L_A)
plt.plot(ic_leisure, ic_old, color='red', alpha=0.4, linestyle='-', label="Hicksian Constant Utility (U1)")

# ५. बिन्दुहरू मार्किंग गर्ने
plt.scatter(L_A, C_A, color='black', s=90, zorder=5, label="A: Original Baseline (Deserved Basket)")
plt.scatter(L_H, C_H, color='darkred', s=80, zorder=5, marker='o')
plt.scatter(L_S, C_S, color='purple', s=80, zorder=5, marker='s')
plt.scatter(L_F, C_F, color='darkgreen', s=100, zorder=5, marker='^')

# लेबलहरू लेख्ने
plt.text(L_A + 0.3, C_A + 5, 'A (Baseline)', fontsize=10, weight='bold')
plt.text(L_H - 1.8, C_H - 5, 'H (Hicks)', fontsize=10, color='darkred', weight='bold')
plt.text(L_S + 0.3, C_S + 5, 'S (Slutsky)', fontsize=10, color='purple', weight='bold')
plt.text(L_F + 0.4, C_F - 3, 'F (Frisch Trend)', fontsize=10, color='darkgreen', weight='bold')

# ६. ग्राफको सजावट
plt.xlim(0, 26)
plt.ylim(0, 240)
plt.grid(True, linestyle=':', alpha=0.5)
plt.legend(loc="upper right")
plt.show()
