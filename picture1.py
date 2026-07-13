'''
Author: DamaHou 1483193713@qq.com
Date: 2026-07-13 16:51:58
LastEditors: DamaHou 1483193713@qq.com
LastEditTime: 2026-07-13 16:53:53
FilePath: \无线通信基础与应用\picture1.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 中文字体设置
chinese_fonts = [
    "Microsoft YaHei",
    "SimHei",
    "SimSun",
    "Noto Sans CJK SC",
    "Source Han Sans SC",
]

available_fonts = {f.name for f in font_manager.fontManager.ttflist}
for font in chinese_fonts:
    if font in available_fonts:
        plt.rcParams["font.sans-serif"] = [font]
        break

plt.rcParams["axes.unicode_minus"] = False

# 参数
N = 15
Tc = 1.0
T = N * Tc

tau = np.linspace(-0.6 * T, 1.6 * T, 3000)

def mseq_autocorr(tau, N, Tc):
    T = N * Tc
    x = ((tau + T / 2) % T) - T / 2
    ax = np.abs(x)

    R = np.full_like(tau, -1 / N)

    main_lobe = ax <= Tc
    R[main_lobe] = 1 - (1 + 1 / N) * ax[main_lobe] / Tc

    return R

R = mseq_autocorr(tau, N, Tc)

plt.figure(figsize=(10, 4))
plt.plot(tau / Tc, R, color="black", linewidth=2)

plt.axhline(0, color="black", linewidth=1)
plt.axhline(-1 / N, color="black", linestyle="--", linewidth=1)
plt.axvline(0, color="black", linewidth=0.8)
plt.axvline(N, color="black", linewidth=0.8)

plt.text(0, 1.05, r"$R_c(\tau)$", ha="center", fontsize=13)
plt.text(N / 2, 1.02, r"$NT_c$", ha="center", fontsize=12)
plt.text(0.6, 0.2, r"$T_c$", fontsize=12)
plt.text(-2.5, -1 / N - 0.08, r"$-1/N$", fontsize=12)

plt.xlabel(r"$\tau/T_c$")
plt.ylabel(r"$R_c(\tau)$")
plt.title("最长序列的自相关函数")
plt.ylim(-0.25, 1.15)
plt.grid(True, linestyle=":", alpha=0.5)

plt.tight_layout()
plt.show()