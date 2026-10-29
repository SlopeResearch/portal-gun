"""Generates all README figures (RU + EN) into assets/. Run: python3 make_figures.py"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch, Ellipse, Wedge, Polygon
import os

OUT = os.path.dirname(os.path.abspath(__file__))
BG, FG, DIM = "#0b1020", "#e8f0ff", "#8a94b0"
GREEN, GREEN2, YEL, RED, CYAN, MAG = "#3dff7a", "#9dffb8", "#ffd84d", "#ff4d6d", "#4de1ff", "#c77dff"

plt.rcParams.update({
    "figure.facecolor": BG, "axes.facecolor": BG, "savefig.facecolor": BG,
    "text.color": FG, "axes.edgecolor": DIM, "axes.labelcolor": FG,
    "xtick.color": DIM, "ytick.color": DIM, "font.family": "DejaVu Sans", "font.size": 12,
})

T = {
    "ru": dict(
        banner_sub="Научное обоснование портальной пушки · коллектив из 6 ИИ-учёных · 60 минут",
        banner_tag="Слова «невозможно» не существует. Каждое допущение помечено.",
        anat_title="Анатомия портала Санчеса",
        anat_rim="Обод: экзотическое натяжение\n$\\mu=-c^2/4G$ (≈ Юпитер на метр)",
        anat_flat="Внутри: ровно плоское\nпространство, приливных сил нет",
        anat_film="Бицеллярная плёнка 0,1–1 мкм:\nнепрозрачна, газ не пропускает,\nтело проходит",
        anat_vortex="Квантованное вихревое кольцо\nжидкости задаёт положение обода",
        anat_sheets="Два листа пространства\nсклеены по диску (Гиббонс–Волков)",
        arch_title="Архитектура: пушка — жидкость — якорь — сеть",
        arch=[("ПУШКА\n(терминал)", "дозатор, вихревое сопло,\nнакачка, адрес, τ и κ\nбатарея: ~10⁴ выстрелов"),
              ("ЖИДКОСТЬ\n(локальный ключ)", "шаблон обода, плёнка,\nхемилюминесценция\n≤10²⁶ пар на дозу"),
              ("ЯКОРЬ\n(дальнее устье)", "партнёры пар, репер E₂,\nприём диссипации\n≥99 % пар"),
              ("СЕТЬ\n(инфраструктура)", "адресация «C-137»,\nканал через балк,\nпокрытие = Кривая")],
        arch_note="Массовый сбой пушек (S5E10) и «перезагрузка жидкости» (S6E1)\nневозможны для автономных устройств → сетевая модель",
        gap_title="Энергетический разрыв (лог. шкала, Дж)",
        gap_labels=["Один выстрел\nпушки", "Падение\n70 кг, 20 м/с", "Батарея\n100 г", "Заготовка\n10²⁹ пар", "Казимир\nна ободе 1 м", "Обод R = 1 м\n|E₋| = πRc⁴/2G", "mc²\nЮпитера"],
        gap_note="≈ 43 порядка между выстрелом и ободом\n(и 52 — между Казимиром и ободом).\nПоэтому энергию не хранят —\nеё «занимает» нелокальная связь.",
        tl_title="Циклограмма выстрела (R = 1 м, доза 0,5 мл, τ = 3 с)",
        tl=[(0.001, "доза 0,5 мл,\nсмешение"), (0.005, "вихревое кольцо\nL/D ≈ 4"), (0.05, "квантование\nядра вихря"),
            (0.3, "раздув до 1 м,\nплёнка — ОТКРЫТ"), (1.5, "окно прохода"), (2.8, "красный:\n«не стой в кольце»"),
            (3.3, "схлопывание\nε→0, ~нс")],
        tl_axis="время, с (лог. шкала)",
        mom_title="Два режима импульса — один параметр κ",
        mom_a="κ = 1: склейка жёсткая\nскорость сохраняется",
        mom_b="κ = 0: склейка мягкая\nпадение гасится, E → якорь",
        mom_formula="$\\mathbf{v}_{out}=\\mathbf{V}_2+\\kappa\\,\\mathcal{R}\\,(\\mathbf{v}_{in}-\\mathbf{V}_1)$",
        mom_pred="Предсказание: режим κ=0 греет дозу → портал живёт меньше",
        nick_title="Урок Ника: не пересекай пару",
        nick_a="два диска одной пары", nick_b="пересечение", nick_c="аннигиляция связи\n(«zero-point vacuum»)",
    ),
    "en": dict(
        banner_sub="A scientific case for the portal gun · a collective of 6 AI scientists · 60 minutes",
        banner_tag="The word “impossible” does not exist here. Every assumption is labelled.",
        anat_title="Anatomy of the Sanchez portal",
        anat_rim="Rim: exotic tension\n$\\mu=-c^2/4G$ (≈ one Jupiter per metre)",
        anat_flat="Inside: exactly flat space,\nno tidal forces",
        anat_film="Bicellar film 0.1–1 µm:\nopaque, gas-tight,\nbodies pass through",
        anat_vortex="Quantized vortex ring of the fluid\nsets the rim position",
        anat_sheets="Two sheets of space glued\nalong the disc (Gibbons–Volkov)",
        arch_title="Architecture: gun — fluid — anchor — network",
        arch=[("GUN\n(terminal)", "dispenser, vortex nozzle,\npumping, address, τ and κ\nbattery: ~10⁴ shots"),
              ("FLUID\n(local key)", "rim template, film,\nchemiluminescence\n≤10²⁶ pairs per dose"),
              ("ANCHOR\n(far mouth)", "pair partners, frame E₂,\nabsorbs dissipation\n≥99 % of pairs"),
              ("NETWORK\n(infrastructure)", "addressing “C-137”,\nchannel through the bulk,\ncoverage = the Curve")],
        arch_note="Mass gun failure (S5E10) and the “fluid reboot” (S6E1)\nare impossible for autonomous devices → network model",
        gap_title="The energy gap (log scale, J)",
        gap_labels=["One gun\nshot", "Fall of\n70 kg at 20 m/s", "100 g\nbattery", "Preparing\n10²⁹ pairs", "Casimir on\na 1 m rim", "Rim R = 1 m\n|E₋| = πRc⁴/2G", "Jupiter's\nmc²"],
        gap_note="≈ 43 orders of magnitude between a shot\nand the rim (52 between Casimir and the rim).\nSo the energy is not stored —\nit is “borrowed” via a non-local coupling.",
        tl_title="Firing timeline (R = 1 m, 0.5 mL dose, τ = 3 s)",
        tl=[(0.001, "0.5 mL dose,\nmixing"), (0.005, "vortex ring\nL/D ≈ 4"), (0.05, "vortex core\nquantizes"),
            (0.3, "inflates to 1 m,\nfilm — OPEN"), (1.5, "transit window"), (2.8, "red:\n“step out of the ring”"),
            (3.3, "collapse\nε→0, ~ns")],
        tl_axis="time, s (log scale)",
        mom_title="Two momentum regimes — one parameter κ",
        mom_a="κ = 1: stiff gluing\nvelocity is conserved",
        mom_b="κ = 0: soft gluing\nfall is damped, E → anchor",
        mom_formula="$\\mathbf{v}_{out}=\\mathbf{V}_2+\\kappa\\,\\mathcal{R}\\,(\\mathbf{v}_{in}-\\mathbf{V}_1)$",
        mom_pred="Prediction: κ=0 heats the dose → the portal lives shorter",
        nick_title="Nick's lesson: never cross a pair",
        nick_a="two discs of one pair", nick_b="intersection", nick_c="coupling annihilates\n(“zero-point vacuum”)",
    ),
}


def portal(ax, cx, cy, r, rings=9, seed=0, alpha=1.0, rot=0.0):
    """Swirly green disc with a bright rim."""
    rng = np.random.default_rng(seed)
    th = np.linspace(0, 2 * np.pi, 400)
    for i in range(rings, 0, -1):
        rr = r * i / rings
        wob = 1 + 0.05 * np.sin(5 * th + rot + i) * (i / rings)
        col = GREEN if i % 2 else "#1f8f46"
        ax.fill(cx + rr * wob * np.cos(th), cy + rr * wob * np.sin(th), color=col, alpha=alpha * (0.35 + 0.5 * i / rings), lw=0)
    # swirl arms
    for k in range(4):
        t = np.linspace(0, 3.2, 200)
        rr = r * (0.1 + 0.28 * t)
        ang = t * 2.4 + k * np.pi / 2 + rot
        ax.plot(cx + rr * np.cos(ang), cy + rr * np.sin(ang), color="#0b4d26", lw=2.2, alpha=0.8 * alpha)
    ax.add_patch(Circle((cx, cy), r, fill=False, lw=6, ec=GREEN2, alpha=alpha))
    ax.add_patch(Circle((cx, cy), r * 1.03, fill=False, lw=14, ec=GREEN, alpha=0.25 * alpha))


def stars(ax, n, xlim, ylim, seed=1):
    rng = np.random.default_rng(seed)
    ax.scatter(rng.uniform(*xlim, n), rng.uniform(*ylim, n), s=rng.uniform(1, 9, n), c=FG, alpha=0.5, lw=0, zorder=0)


def fig_banner(L, lang):
    fig, ax = plt.subplots(figsize=(16, 6))
    ax.set_xlim(0, 16); ax.set_ylim(0, 6); ax.axis("off")
    stars(ax, 250, (0, 16), (0, 6))
    portal(ax, 13.6, 3, 1.95, seed=3)
    # tiny stick figure mid-jump into the portal (original, generic)
    sx, sy = 11.0, 1.4
    ax.plot([sx - 0.3, sx], [sy, sy + 0.2], color=FG, lw=3); ax.plot([sx, sx + 0.3], [sy + 0.2, sy - 0.1], color=FG, lw=3)
    ax.plot([sx, sx - 0.05], [sy + 0.2, sy + 0.8], color=FG, lw=3); ax.add_patch(Circle((sx - 0.07, sy + 1.05), 0.22, color=FG))
    ax.plot([sx - 0.05, sx - 0.4], [sy + 0.65, sy + 0.45], color=FG, lw=3); ax.plot([sx - 0.05, sx + 0.4], [sy + 0.65, sy + 0.85], color=FG, lw=3)
    ax.text(0.6, 4.3, "PORTAL GUN SCIENCE", fontsize=40, weight="bold", color=GREEN, va="center")
    ax.text(0.65, 3.3, L["banner_sub"], fontsize=14, color=FG, va="center")
    ax.text(0.65, 2.6, L["banner_tag"], fontsize=12.5, color=DIM, va="center", style="italic")
    ax.text(0.65, 1.6, "|E₋| = πRc⁴/2G ≈ 1.9·10⁴⁴ J/m        κ ∈ [0, 1]", fontsize=12, color=CYAN, va="center", family="DejaVu Sans Mono")
    ax.text(0.65, 1.0, "τ = min{τ_pump, τ_couple}·[1 − f_loc ΣE_d/E_c]", fontsize=12, color=CYAN, va="center", family="DejaVu Sans Mono")
    fig.savefig(f"{OUT}/banner_{lang}.png", dpi=110, bbox_inches="tight", pad_inches=0.1); plt.close(fig)


def fig_anatomy(L, lang):
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13); ax.set_ylim(0, 8); ax.axis("off")
    ax.set_title(L["anat_title"], fontsize=20, color=GREEN, weight="bold", pad=14)
    # two sheets (perspective parallelograms)
    for dy, col in [(0.0, "#16203a"), (-0.35, "#121a30")]:
        ax.add_patch(Polygon([[1, 1.2 + dy], [8.5, 1.2 + dy], [10.5, 6.5 + dy], [3, 6.5 + dy]], closed=True, fc=col, ec=DIM, lw=1, alpha=0.9))
    cx, cy, r = 5.8, 3.9, 2.0
    ax.add_patch(Ellipse((cx, cy), 2 * r, 2 * r * 0.55, fc="#0e2a1a", ec=GREEN, lw=5, zorder=3))
    ax.add_patch(Ellipse((cx, cy), 2 * r * 1.03, 2 * r * 0.55 * 1.03, fill=False, ec=GREEN, lw=14, alpha=0.25, zorder=2))
    ax.add_patch(Ellipse((cx, cy), 2 * r * 0.93, 2 * r * 0.55 * 0.93, fc="#1a4a2c", ec="none", alpha=0.85, zorder=3))
    # vortex ring hint (small circles along rim)
    th = np.linspace(0, 2 * np.pi, 28, endpoint=False)
    ax.scatter(cx + r * np.cos(th), cy + r * 0.55 * np.sin(th), s=28, c=GREEN2, zorder=5)
    # grid inside to show flatness
    for k in np.linspace(-0.8, 0.8, 5):
        ax.plot([cx + k * r * 0.95, cx + k * r * 0.95], [cy - 0.5, cy + 0.5], color=GREEN2, lw=0.6, alpha=0.4, zorder=4)
        ax.plot([cx - 1.6, cx + 1.6], [cy + k * 0.55 * r * 0.9, cy + k * 0.55 * r * 0.9], color=GREEN2, lw=0.6, alpha=0.4, zorder=4)
    # arrow through
    ax.add_patch(FancyArrowPatch((cx - 0.4, cy + 2.9), (cx + 0.6, cy - 1.9), arrowstyle="-|>", mutation_scale=28, lw=3, color=CYAN, zorder=6))

    def note(x, y, text, px, py, col):
        ax.annotate(text, xy=(px, py), xytext=(x, y), fontsize=11.5, color=col, ha="center", va="center",
                    bbox=dict(boxstyle="round,pad=0.5", fc="#0f1630", ec=col, lw=1.4),
                    arrowprops=dict(arrowstyle="-", color=col, lw=1.4), zorder=7)
    note(2.2, 7.1, L["anat_rim"], cx - r * 0.75, cy + 0.72, GREEN)
    note(10.9, 6.9, L["anat_flat"], cx + 0.4, cy + 0.1, CYAN)
    note(10.8, 2.0, L["anat_film"], cx + r * 0.5, cy - 0.5, MAG)
    note(2.0, 1.1, L["anat_vortex"], cx - r * 0.3, cy - 1.05, GREEN2)
    note(6.3, 0.6, L["anat_sheets"], 8.2, 1.2, DIM)
    fig.savefig(f"{OUT}/anatomy_{lang}.png", dpi=110, bbox_inches="tight", pad_inches=0.15); plt.close(fig)


def fig_arch(L, lang):
    fig, ax = plt.subplots(figsize=(15, 6.2))
    ax.set_xlim(0, 15); ax.set_ylim(0, 6.2); ax.axis("off")
    ax.set_title(L["arch_title"], fontsize=20, color=GREEN, weight="bold", pad=14)
    cols = [CYAN, GREEN, YEL, MAG]
    xs = [0.3, 4.05, 7.8, 11.55]
    for (head, body), x, c in zip(L["arch"], xs, cols):
        ax.add_patch(FancyBboxPatch((x, 1.6), 3.1, 3.4, boxstyle="round,pad=0.08,rounding_size=0.25", fc="#0f1630", ec=c, lw=2.5))
        ax.text(x + 1.55, 4.45, head, ha="center", va="center", fontsize=14, weight="bold", color=c)
        ax.text(x + 1.55, 2.75, body, ha="center", va="center", fontsize=11, color=FG)
    for i in range(3):
        ax.add_patch(FancyArrowPatch((xs[i] + 3.12, 3.3), (xs[i + 1] - 0.02, 3.3), arrowstyle="<|-|>", mutation_scale=22, lw=2.4, color=FG, zorder=6))
    for i, lab in enumerate(["0.5 mL", "EPR", "bulk"]):
        ax.text(xs[i] + 3.72, 3.7, lab, ha="center", fontsize=10, color=DIM)
    ax.text(7.5, 0.7, L["arch_note"], ha="center", va="center", fontsize=12, color=YEL, style="italic")
    fig.savefig(f"{OUT}/architecture_{lang}.png", dpi=110, bbox_inches="tight", pad_inches=0.15); plt.close(fig)


def fig_gap(L, lang):
    vals = [10, 1.4e4, 1.1e5, 3e8, 4.5e-8, 1.9e44, 1.7e44]  # J; Casimir: 5e-25 kg/m * c^2 * 2π m
    cols = [CYAN, CYAN, CYAN, YEL, DIM, GREEN, MAG]
    fig, ax = plt.subplots(figsize=(13, 6.5))
    ax.set_title(L["gap_title"], fontsize=20, color=GREEN, weight="bold", pad=14)
    x = np.arange(len(vals))
    ax.bar(x, np.log10(vals) + 10, bottom=-10, color=cols, width=0.62, alpha=0.9)
    for xi, v in zip(x, vals):
        ax.text(xi, np.log10(v) + 1.0, f"10$^{{{np.log10(v):.0f}}}$", ha="center", fontsize=12, color=FG)
    ax.set_xticks(x); ax.set_xticklabels(L["gap_labels"], fontsize=10.5)
    ax.set_ylim(-10, 52); ax.set_yticks(range(-10, 51, 10)); ax.set_yticklabels([f"10$^{{{k}}}$" for k in range(-10, 51, 10)])
    ax.grid(axis="y", color=DIM, alpha=0.2); ax.spines[["top", "right"]].set_visible(False)
    ax.annotate("", xy=(5, 44.3), xytext=(0, 1.3), arrowprops=dict(arrowstyle="<->", color=RED, lw=2, ls="--"))
    ax.text(2.0, 30, L["gap_note"], fontsize=12, color=RED, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.6", fc="#0f1630", ec=RED, lw=1.4))
    fig.savefig(f"{OUT}/energy_gap_{lang}.png", dpi=110, bbox_inches="tight", pad_inches=0.15); plt.close(fig)


def fig_timeline(L, lang):
    fig, ax = plt.subplots(figsize=(15, 5.2))
    ax.set_title(L["tl_title"], fontsize=20, color=GREEN, weight="bold", pad=14)
    ax.set_xscale("log"); ax.set_xlim(5e-4, 5); ax.set_ylim(-1.6, 1.8); ax.set_yticks([])
    ax.spines[["top", "right", "left"]].set_visible(False)
    # colour band: open window green→yellow→red
    tt = np.logspace(np.log10(0.3), np.log10(3.3), 200)
    for a, b in zip(tt[:-1], tt[1:]):
        f = (np.log10(a) - np.log10(0.3)) / (np.log10(3.3) - np.log10(0.3))
        c = np.array(matplotlib.colors.to_rgb(GREEN)) * (1 - f) + np.array(matplotlib.colors.to_rgb(RED)) * f
        ax.axvspan(a, b, ymin=0.42, ymax=0.58, color=c, lw=0)
    ax.axhline(0, color=DIM, lw=1.5, zorder=0)
    levels = [0.6, -0.6, 0.6, -0.6, 1.15, -0.6, 0.6]
    for (t, lab), lv in zip(L["tl"], levels):
        col = GREEN if t < 2.5 else (YEL if t < 3 else RED)
        ax.plot([t, t], [0, lv], color=col, lw=1.5); ax.scatter([t], [0], s=90, c=col, zorder=5)
        ax.text(t, lv + (0.05 if lv > 0 else -0.05), lab, ha="center", va="bottom" if lv > 0 else "top", fontsize=11, color=FG)
    ax.set_xlabel(L["tl_axis"], color=DIM)
    fig.savefig(f"{OUT}/timeline_{lang}.png", dpi=110, bbox_inches="tight", pad_inches=0.15); plt.close(fig)


def fig_momentum(L, lang):
    fig, axs = plt.subplots(1, 2, figsize=(14, 6.6))
    fig.subplots_adjust(top=0.80, bottom=0.17)
    fig.suptitle(L["mom_title"], fontsize=20, color=GREEN, weight="bold", y=0.98)
    for ax, kappa, title in zip(axs, [1.0, 0.0], [L["mom_a"], L["mom_b"]]):
        ax.set_xlim(0, 10); ax.set_ylim(0, 8); ax.axis("off")
        ax.set_title(title, fontsize=13, color=FG, pad=8)
        # floor portal (horizontal ellipse at top = entry), wall portal (exit)
        ax.add_patch(Ellipse((2.5, 1.2), 3, 0.9, fc="#1a4a2c", ec=GREEN, lw=4))
        ax.add_patch(Ellipse((8.2, 4.5), 0.9, 3, fc="#1a4a2c", ec=GREEN, lw=4))
        # falling ball
        ys = np.linspace(7.2, 1.6, 7)
        for k, y in enumerate(ys):
            ax.add_patch(Circle((2.5, y), 0.25, color=CYAN, alpha=0.25 + 0.75 * k / 6))
        ax.add_patch(FancyArrowPatch((2.5, 7.0), (2.5, 2.0), arrowstyle="-|>", mutation_scale=18, lw=2, color=CYAN, alpha=0.6))
        if kappa == 1.0:
            xs = np.linspace(7.7, 4.0, 7)
            for k, x in enumerate(xs):
                ax.add_patch(Circle((x, 4.5), 0.25, color=CYAN, alpha=1 - 0.75 * k / 6))
            ax.add_patch(FancyArrowPatch((7.5, 4.5), (4.3, 4.5), arrowstyle="-|>", mutation_scale=18, lw=2, color=CYAN, alpha=0.6))
            ax.text(5.8, 5.2, "|v_out| = |v_in|", ha="center", fontsize=12, color=CYAN)
        else:
            ax.add_patch(Circle((7.4, 4.5), 0.25, color=CYAN))
            ax.text(6.6, 5.2, "v_out ≈ 0", ha="center", fontsize=12, color=CYAN)
            ax.add_patch(FancyArrowPatch((8.4, 3.0), (9.6, 1.4), arrowstyle="-|>", mutation_scale=18, lw=2, color=YEL, ls="--"))
            ax.text(9.3, 2.5, "E_d → anchor", fontsize=10, color=YEL, rotation=-50, ha="center")
    fig.text(0.5, 0.08, L["mom_formula"], ha="center", fontsize=17, color=GREEN2)
    fig.text(0.5, 0.02, L["mom_pred"], ha="center", fontsize=12, color=YEL, style="italic")
    fig.savefig(f"{OUT}/momentum_{lang}.png", dpi=110, bbox_inches="tight", pad_inches=0.15); plt.close(fig)


def fig_nick(L, lang):
    fig, axs = plt.subplots(1, 3, figsize=(14, 4.8))
    fig.suptitle(L["nick_title"], fontsize=20, color=RED, weight="bold", y=1.0)
    for ax, lab in zip(axs, [L["nick_a"], L["nick_b"], L["nick_c"]]):
        ax.set_xlim(0, 10); ax.set_ylim(0, 8); ax.axis("off"); ax.set_title(lab, fontsize=12, color=FG)
    portal(axs[0], 3, 4, 1.8, seed=5); portal(axs[0], 7.2, 4, 1.8, seed=6, rot=1.0)
    axs[0].plot([4.8, 5.4], [4, 4], color=DIM, lw=1.5, ls=":")
    portal(axs[1], 4.2, 4, 1.8, seed=5); portal(axs[1], 5.8, 4, 1.8, seed=6, rot=1.0, alpha=0.9)
    axs[1].text(5, 1.0, "!", fontsize=30, color=YEL, ha="center", weight="bold")
    # explosion
    rng = np.random.default_rng(7)
    th = np.linspace(0, 2 * np.pi, 40)
    rr = 2.6 + 0.9 * rng.uniform(-1, 1, 40)
    axs[2].fill(5 + rr * np.cos(th), 4 + rr * 0.9 * np.sin(th), color=RED, alpha=0.8)
    axs[2].fill(5 + 0.6 * rr * np.cos(th + 0.3), 4 + 0.5 * rr * np.sin(th + 0.3), color=YEL, alpha=0.9)
    axs[2].text(5, 4, "S5E9", fontsize=16, color=BG, ha="center", va="center", weight="bold")
    fig.savefig(f"{OUT}/nick_{lang}.png", dpi=110, bbox_inches="tight", pad_inches=0.15); plt.close(fig)


if __name__ == "__main__":
    for lang, L in T.items():
        for f in (fig_banner, fig_anatomy, fig_arch, fig_gap, fig_timeline, fig_momentum, fig_nick):
            f(L, lang)
    print("done")
