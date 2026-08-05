import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

# Data estimated from industry reports (2025-2026)
data = {
    "Date": [
        "Jan-2025",
        "Jun-2025",
        "Dec-2025",
        "Feb-2026",
        "Apr-2026",
        "Jun-2026",
        "Aug-2026",
    ],
    # Estimated revenue in Billions (B)
    "China_Revenue_B": [0.1, 0.5, 1.2, 2.5, 4.0, 6.0, 8.5],
    "US_Revenue_B": [8.0, 10.0, 12.0, 11.5, 10.0, 8.5, 7.0],
}

df = pd.DataFrame(data)

# Set the visual style
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))

# Plotting
plt.plot(
    df["Date"],
    df["China_Revenue_B"],
    marker="o",
    linewidth=3,
    color="#d62728",
    label="Chinese Models Revenue",
)
plt.plot(
    df["Date"],
    df["US_Revenue_B"],
    marker="o",
    linewidth=3,
    color="#1f77b4",
    label="US Models Revenue",
)

# Annotate the plotted points
for i, row in df.iterrows():
    plt.annotate(
        f"${row['China_Revenue_B']}B",
        (row["Date"], row["China_Revenue_B"]),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        fontsize=9,
        color="#d62728",
    )
    plt.annotate(
        f"${row['US_Revenue_B']}B",
        (row["Date"], row["US_Revenue_B"]),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        fontsize=9,
        color="#1f77b4",
    )

# Highlighting the "Crossover Event"
plt.axvline(x="Aug-2026", color="gray", linestyle="--", alpha=0.6)
plt.text(
    "Aug-2026", 5, "  Projected Crossover\n  in Revenue", verticalalignment="center"
)

# Labels and Title
plt.title(
    "Monthly AI Revenue: China vs. US (2025-2026)", fontsize=16, fontweight="bold"
)
plt.ylabel("Monthly Revenue (Billions of USD)", fontsize=12)
plt.xlabel("Timeline", fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)

# Create assets folder if it doesn't exist
os.makedirs("assets", exist_ok=True)

# Save the plot
plt.tight_layout()
plt.savefig("assets/revenue_plot.png", dpi=300, bbox_inches="tight")
print("Successfully generated assets/revenue_plot.png")
# Show the plot
plt.show()
