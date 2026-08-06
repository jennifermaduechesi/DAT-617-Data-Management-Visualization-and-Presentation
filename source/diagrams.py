import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon
import matplotlib.font_manager as fm
import numpy as np
import os

OUT = os.path.dirname(os.path.abspath(__file__))

# muted, professional palette (not garish)
INK = "#1f2a33"
MUTED = "#4a5b68"
LINE = "#8a97a1"
FILLS = ["#dfe7ec", "#c7d4dc", "#aec1cd", "#8fa8b8"]
ACCENT = "#c99700"  # subtle MTN-ish amber, used sparingly

plt.rcParams["font.family"] = "DejaVu Sans"

# ----------------------------------------------------------------------------
# Figure 1 — DIKW pyramid for MTN
# ----------------------------------------------------------------------------
def dikw():
    fig, ax = plt.subplots(figsize=(7.4, 5.2))
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")

    layers = [
        ("DATA", "Raw CDRs, network telemetry, MoMo transaction logs,\ntower alarms, billing and CRM records", FILLS_ := FILLS[0] if False else "#dfe7ec"),
    ]
    # build pyramid as 4 trapezoids
    tiers = [
        ("DATA", "Raw CDRs, network telemetry, MoMo logs,\ntower alarms, billing and CRM records", "#dfe7ec"),
        ("INFORMATION", "Churn by region, ARPU, uptime %,\nNPS trends on cleaned dashboards", "#c7d4dc"),
        ("KNOWLEDGE", "Why segments churn, fraud\nsignatures, fault patterns", "#aec1cd"),
        ("WISDOM", "Capex, market\ndefence, pricing", "#8fa8b8"),
    ]
    n = len(tiers)
    h = 2.0
    base_y = 0.6
    for i, (title, sub, col) in enumerate(tiers):
        # i=0 top
        level = n - 1 - i  # 3 for top
        y0 = base_y + i*h
        y1 = y0 + h*0.92
        # width shrinks going up
        half_bottom = 4.4 * (1 - i*0.185)
        half_top = 4.4 * (1 - (i+1)*0.185)
        cx = 5
        poly = Polygon([(cx-half_bottom, y0),(cx+half_bottom, y0),
                        (cx+half_top, y1),(cx-half_top, y1)],
                       closed=True, facecolor=col, edgecolor="white", linewidth=2)
        ax.add_patch(poly)
        ymid = (y0+y1)/2
        ax.text(cx, ymid+0.18, title, ha="center", va="center",
                fontsize=12, fontweight="bold", color=INK)
        ax.text(cx, ymid-0.42, sub, ha="center", va="center",
                fontsize=7.3, color=MUTED)

    # upward arrow on the left
    ax.annotate("", xy=(0.7, base_y+n*h-0.4), xytext=(0.7, base_y+0.2),
                arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.6))
    ax.text(0.35, base_y+n*h/2, "increasing value to decision-making",
            rotation=90, ha="center", va="center", fontsize=7.6, color=MUTED)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig1_dikw.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)

# ----------------------------------------------------------------------------
# Figure 2 — 9-stage enterprise analytical workflow
# ----------------------------------------------------------------------------
def workflow():
    fig, ax = plt.subplots(figsize=(7.6, 5.6))
    ax.set_xlim(0, 12); ax.set_ylim(0, 10); ax.axis("off")

    stages = [
        "1. Business Problem\nIdentification",
        "2. Requirements\nAnalysis",
        "3. Data\nCollection",
        "4. Data\nPreparation",
        "5. Data\nAnalysis",
        "6. Data\nVisualization",
        "7. Decision\nSupport",
        "8. Implementation",
        "9. Organizational\nLearning",
    ]
    # positions: 3 rows snaking
    coords = [
        (1.6, 8.4),(4.6,8.4),(7.6,8.4),(10.4,8.4),
        (10.4,5.2),(7.6,5.2),(4.6,5.2),(1.6,5.2),
        (1.6,2.0),
    ]
    bw, bh = 2.35, 1.5
    for (x,y), label in zip(coords, stages):
        box = FancyBboxPatch((x-bw/2, y-bh/2), bw, bh,
                             boxstyle="round,pad=0.03,rounding_size=0.12",
                             facecolor=FILLS[1], edgecolor=MUTED, linewidth=1.3)
        ax.add_patch(box)
        ax.text(x, y, label, ha="center", va="center", fontsize=8.2,
                color=INK, fontweight="bold")

    def arrow(p1, p2, rad=0.0):
        a = FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=13,
                            color=MUTED, lw=1.5,
                            connectionstyle=f"arc3,rad={rad}")
        ax.add_patch(a)
    # row 1 left->right
    for i in range(3):
        arrow((coords[i][0]+bw/2, coords[i][1]), (coords[i+1][0]-bw/2, coords[i+1][1]))
    # down 4->5
    arrow((coords[3][0], coords[3][1]-bh/2), (coords[4][0], coords[4][1]+bh/2))
    # row 2 right->left
    for i in range(4,7):
        arrow((coords[i][0]-bw/2, coords[i][1]), (coords[i+1][0]+bw/2, coords[i+1][1]))
    # down 8->9
    arrow((coords[7][0], coords[7][1]-bh/2), (coords[8][0], coords[8][1]+bh/2))

    # feedback loop 9 -> 1 (dashed)
    fb = FancyArrowPatch((coords[8][0]+bw/2, coords[8][1]),
                         (coords[0][0], coords[0][1]-bh/2),
                         arrowstyle="-|>", mutation_scale=13,
                         color=ACCENT, lw=1.5, linestyle=(0,(5,3)),
                         connectionstyle="arc3,rad=-0.28")
    ax.add_patch(fb)
    ax.text(3.2, 3.5, "learning feeds back into\nnew problem framing",
            fontsize=7.4, color=ACCENT, ha="left", va="center", style="italic")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig2_workflow.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)

# ----------------------------------------------------------------------------
# Figure 3 — Executive dashboard mock-up
# ----------------------------------------------------------------------------
def dashboard():
    fig = plt.figure(figsize=(7.8, 5.2))
    fig.patch.set_facecolor("#f4f6f8")
    gs = fig.add_gridspec(3, 4, hspace=0.75, wspace=0.45,
                          left=0.05, right=0.97, top=0.86, bottom=0.09)

    fig.text(0.05, 0.94, "MTN Executive Analytics Dashboard",
             fontsize=13, fontweight="bold", color=INK)
    fig.text(0.05, 0.905, "Group view  ·  rolling 12 months  ·  updated daily",
             fontsize=8, color=MUTED)

    # KPI tiles (top row)
    kpis = [("Churn rate","2.1%","-0.4 pp"),
            ("Blended ARPU","$4.30","+3.1%"),
            ("Network uptime","99.2%","+0.3 pp"),
            ("Group NPS","+34","+5")]
    for i,(t,v,d) in enumerate(kpis):
        ax = fig.add_subplot(gs[0, i]); ax.axis("off")
        ax.add_patch(FancyBboxPatch((0.02,0.05),0.96,0.9,
                     boxstyle="round,pad=0.02,rounding_size=0.06",
                     facecolor="white", edgecolor="#d7dee4", linewidth=1,
                     transform=ax.transAxes))
        ax.text(0.5,0.74,t,ha="center",fontsize=7.6,color=MUTED,transform=ax.transAxes)
        ax.text(0.5,0.44,v,ha="center",fontsize=15,fontweight="bold",color=INK,transform=ax.transAxes)
        good = not d.startswith("-") if t!="Churn rate" else d.startswith("-")
        ax.text(0.5,0.18,d,ha="center",fontsize=7.6,
                color="#2e7d4f" if good else "#b23b3b",transform=ax.transAxes)

    # churn trend line (mid, span 2)
    ax1 = fig.add_subplot(gs[1, 0:2])
    months = np.arange(12)
    churn = np.array([2.9,2.8,2.7,2.7,2.6,2.5,2.4,2.4,2.3,2.2,2.1,2.1])
    ax1.plot(months, churn, color=INK, lw=1.8, marker="o", ms=3)
    ax1.fill_between(months, churn, churn.min()-0.15, color="#dfe7ec", alpha=0.7)
    ax1.set_title("Monthly churn rate (%)", fontsize=8.5, color=INK, loc="left")
    ax1.set_xticks([0,3,6,9,11]); ax1.set_xticklabels(["M1","M4","M7","M10","M12"], fontsize=6.5)
    ax1.tick_params(labelsize=6.5); ax1.grid(axis="y", color="#e5eaee", lw=0.7)
    for s in ["top","right"]: ax1.spines[s].set_visible(False)

    # ARPU by market (mid, span 2)
    ax2 = fig.add_subplot(gs[1, 2:4])
    mk = ["Nigeria","Ghana","S.Africa","Uganda","Others"]
    arpu = [3.1,4.0,7.2,2.8,3.6]
    bars = ax2.bar(mk, arpu, color=["#8fa8b8","#aec1cd","#c99700","#aec1cd","#c7d4dc"], width=0.62)
    ax2.set_title("ARPU by market ($)", fontsize=8.5, color=INK, loc="left")
    ax2.tick_params(labelsize=6.3); ax2.grid(axis="y", color="#e5eaee", lw=0.7)
    for s in ["top","right"]: ax2.spines[s].set_visible(False)

    # data revenue stacked (bottom span 2)
    ax3 = fig.add_subplot(gs[2, 0:2])
    q = ["Q1","Q2","Q3","Q4"]
    voice = np.array([48,46,44,42]); data = np.array([38,41,44,47]); momo=np.array([14,13,12,11])
    ax3.bar(q, voice, label="Voice", color="#c7d4dc")
    ax3.bar(q, data, bottom=voice, label="Data", color="#8fa8b8")
    ax3.bar(q, momo, bottom=voice+data, label="MoMo", color="#c99700")
    ax3.set_title("Revenue mix (%)", fontsize=8.5, color=INK, loc="left")
    ax3.legend(fontsize=6, loc="upper right", ncol=3, frameon=False, bbox_to_anchor=(1.0,1.28))
    ax3.tick_params(labelsize=6.5); ax3.grid(axis="y", color="#e5eaee", lw=0.7)
    for s in ["top","right"]: ax3.spines[s].set_visible(False)

    # network faults heat-ish (bottom span 2)
    ax4 = fig.add_subplot(gs[2, 2:4])
    data_h = np.array([[3,1,0,2,4],[1,0,1,3,2],[0,2,5,1,0]])
    im = ax4.imshow(data_h, cmap="YlOrBr", aspect="auto")
    ax4.set_title("Network faults by region / week", fontsize=8.5, color=INK, loc="left")
    ax4.set_xticks(range(5)); ax4.set_xticklabels(["W1","W2","W3","W4","W5"], fontsize=6)
    ax4.set_yticks(range(3)); ax4.set_yticklabels(["North","East","Lagos"], fontsize=6)

    fig.savefig(os.path.join(OUT, "fig3_dashboard.png"), dpi=200,
                facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close(fig)

dikw(); workflow(); dashboard()
print("done:", os.listdir(OUT))
