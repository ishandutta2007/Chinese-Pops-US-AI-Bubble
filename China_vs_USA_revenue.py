import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

# Data estimated from real-world ARR reports (converted to Monthly Revenue) (2025-2026)
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
    # Estimated monthly revenue in Billions (B)
    "China_Revenue_B": [0.05, 0.08, 0.15, 0.20, 0.30, 0.40, 0.45],
    "US_Revenue_B": [1.5, 2.0, 2.5, 3.0, 4.5, 6.0, 6.5],
}

df = pd.DataFrame(data)

# Set the visual style
sns.set_theme(style="whitegrid")
plt.figure(figsize=(14, 7))

# Plotting
plt.plot(
    df["Date"],
    df["China_Revenue_B"],
    marker="o",
    linewidth=3,
    color="#d62728",
    label="Chinese Models Revenue (DeepSeek, Alibaba Qwen)",
)
plt.plot(
    df["Date"],
    df["US_Revenue_B"],
    marker="o",
    linewidth=3,
    color="#1f77b4",
    label="US Models Revenue (OpenAI, Anthropic)",
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

# Highlighting the actual revenue gap instead of a crossover
plt.axvline(x="Aug-2026", color="gray", linestyle="--", alpha=0.6)
plt.text(
    "Aug-2026", 3.0, "  Massive Revenue Gap\n  (Despite volume crossover)", verticalalignment="center"
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
plt.savefig("assets/revenue_plot.png", dpi=400)
print("Successfully generated assets/revenue_plot.png")
# Show the plot
plt.show()
