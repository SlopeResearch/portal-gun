# 04. Engineering Section: The Portal Gun as a Network Terminal

*Chief Engineer. Labels: **[KNOWN]** verified by search or literature; **[ESTIMATE]** order-of-magnitude calculation; **[02-ASM-n]**, **[03-Dn]** assumptions from files 02 and 03; **[E1–E5]** new engineering assumptions of this section (§8). External figures verified in October 2026 (sources at the end).*

## 1. Summary Table of Parameters

Where the files disagree, both values are given and the choice is justified. The full list of discrepancies is in §9.

| Parameter | 02 | 03 | 05 | **Choice (baseline)** | Rationale |
|---|---|---|---|---|---|
| Disk radius $R$ | 1 m (scale $\propto R$) | Ø2 m | $L=2\pi$ m, i.e. 1 m | **1 m**; from 5 cm (palm, S5E9) to 1.5 km (Citadel, [E4]) | All three files agree |
| Angle $\delta$ and rim energy $\lvert E_-\rvert$ | $2\pi$; $1.9\cdot10^{44}$ J | $c^2/8G$…$c^2/4G$; $\approx1.2\cdot10^{27}$ kg | $\pi/2$; $5\cdot10^{26}$ kg, i.e. 4 times smaller | **$\delta=2\pi$, $1.9\cdot10^{44}$ J** | Only $2\pi$ gives an exactly flat opening without tidal forces (Gibbons–Volkov). The factor of 4 does not change the conclusions |
| Lifetime | $\sim10^{-20}$ s (local QI); with coupling $\tau_{\rm couple}$ | 2.5 s per 0.5 mL dose; 1–10 s needed | decreases with thermal load | **3 s nominal, up to 10 s** | Lore gives no number. We take 03 and add the coupling from 02 |
| Mass before collapse | $\sim1$ t at $\eta\approx7\cdot10^{-25}$ | passage of a human $\sim0.5$ s | human 70 kg, 20 m/s | **1 t; human 100 kg** | From 02, the rest is compatible |
| Dose volume | not specified | 0.2–1 mL (film 0.3–3 mL) | 50 g of liquid (heating) | **0.5 mL** (film $\sim$160 nm over $\pi$ m²) | 05 takes the whole cartridge, not a dose (see §9) |
| Cartridge | "a litre" as a unit | 20–50 mL | 50 g | **50 mL**, two compartments | Size of the flask on the gun |
| Number of shots | not specified | 30–150 | not specified | **$\sim100$ short or $\sim25$ long (2 mL)** | Dividing 20–50 mL by 0.2–1 mL gives 20–250; 03 is coarser |
| Temperature window | effective $\sim0.1$ nK | 0–40 °C | overheating on damping | **0–40 °C physical** | 0.1 nK is the temperature of the dual system, not of the liquid; not reconciled |
| Self-assembly | not specified | ring 4 ms; full 0.05–0.3 s | not specified | **0.3 s before opening** | 03; $L/D=4$ with a 2 cm nozzle and 20 m/s gives $t=L/U=4$ ms |
| Collapse | 5 ns ($\pi R/2c$) | $\sim0.1$ s | not specified | **0.1 s visible, 5 ns final** | Resolution in §4 |
| Entanglement per human | $\gtrsim3\cdot10^{28}$, we take $10^{29}$ | not specified | not specified | **$10^{29}$** (1.4 nucleon masses per bit) | From 02 |
| $\kappa$ | not introduced | not introduced | $[0,1]$, a property of the pair | **default 1; 0.3–0 for landing** | At $\kappa=1$ the gluing is geodesic; $\kappa\lt 1$ is a separate assumption [E3] |

## 2. Energy Budget

**Scale of the problem.** $\lvert E_-\rvert=1.9\cdot10^{44}$ J equals 1.1 times the rest energy of the mass of Jupiter. The cost of passing 100 kg according to 02 is $(\pi/2)mc^2=1.4\cdot10^{19}$ J. The flask and the handle do not store this.

### (a) "Borrowing from the vacuum" (model 02)

Negative energy is not produced: the portal maintains a coupling, which is paid for by entanglement. The gun spends only operational energy:

| Item | Estimate per shot | Basis |
|---|---|---|
| Ring: kinetic energy of 0.6 g at 20 m/s | 0.12 J | $\tfrac12mU^2$ |
| Film: surface energy $2\sigma\pi R^2$ | 0.19 J | $\sigma=0.03$ N/m |
| Chemical pumping (in the cartridge) | 2.5 J per 0.5 mL | 03 |
| Electrical pumping and field, 3 s | 1–10 J | 10 mW into the condensate at 1–10 % efficiency |
| Control, memory, radio | $\sim1$ J | estimate |
| **Standard shot** | **$\sim5$–15 J** | |
| Damping at $\kappa\lt 1$ (70 kg, 20 m/s) | up to **14 kJ** | 05 |

Sources, **[KNOWN]**: a lithium-ion cell stores 160–450 Wh/kg (gravimetric 240–300, the best silicon cells up to 450). A 100 g pack at 300 Wh/kg stores $\sim1\cdot10^5$ J, i.e. $\sim10^4$ standard shots. An MMRTG delivers 125 W of electrical power at 45 kg, i.e. 2.8 W/kg. Proportional scaling to 100 g gives 0.3 W: suitable for trickle charging, not for a pulse. Damping at 14 kJ consumes up to 10 % of such a battery at once.

**The hidden item: preparation of entangled pairs.** Lower bound on the work needed to prepare a pure state from a thermal environment: $k_BT\ln2=2.9\cdot10^{-21}$ J per qubit at 300 K **[ESTIMATE]**.

| Object | Qubits | Work at 300 K | Equivalent |
|---|---|---|---|
| Human | $10^{29}$ | $3\cdot10^{8}$ J | 80 kWh, 1800 times the gun's battery |
| 10 t ship | $4\cdot10^{30}$ | $1\cdot10^{10}$ J | 3 MWh |
| Citadel [E4] | $4\cdot10^{38}$ | $1\cdot10^{18}$ J | 330 TWh |

Conclusion: the pairs cannot be prepared at the moment of the shot. Either they are prepared in advance (§3, block 6), or they are supplied externally. The exception is the "effective temperature" of 0.1 nK from 02: then the work is $10^{-4}$ J. But a liquid at 0–40 °C has no such temperature, and this is a contradiction between 02 and 03 (§9).

**Drawing from the vacuum: the scale.** If entanglement is drawn from the vacuum by the area law $S\sim A/\varepsilon^2$, then $S=10^{29}$ on a disk of area $A=\pi$ m² requires a resolution $\varepsilon\approx6$ fm, i.e. the nuclear scale **[ESTIMATE, order-one coefficient]**. For the gun this means that access to such entanglement cannot be built into the flask.

**The open item.** Quantum interest (02 §2.2) requires the borrowing to be repaid with positive energy. File 02 asserts that the ADM mass is $\approx0$, but does not show where the positive side of the balance is. If it lies outside the portal, the network will have to pay.

### (b) Micro black hole and antimatter: rejected

- **Sign.** Antimatter gives positive energy; negative energy is needed.
- **Mass.** To cover $1.9\cdot10^{44}$ J even in absolute value, $\sim1.1\cdot10^{27}$ kg of antimatter is needed (0.56 of the mass of Jupiter). The Fermilab accumulation record is $\sim1.2\cdot10^{11}$ antiprotons per hour, i.e. $\sim2$ ng per year **[KNOWN]**. The gap is $\sim10^{36}$. Even 10 g + 10 g in the hand is $1.8\cdot10^{15}$ J, 430 kt of TNT.
- **Black hole.** For $2.1\cdot10^{27}$ kg the Schwarzschild radius is 3.1 m, larger than the gun. Its negative flux at the horizon equals the Hawking luminosity, $8\cdot10^{-23}$ W. A light hole radiates powerfully (6 mg — $10^{43}$ W), but it lives $2\cdot10^{-32}$ s and contains only $5\cdot10^{11}$ J. A hole never gives back more than $Mc^2$.

### (c) The network ("dimensions" as infrastructure)

Lore directly supports this architecture:
- The Council of Ricks reads the destination log from the gun (S1E10) and learns of the gun's destruction (semi-canon, 01 §1).
- Evil Morty's hack worked on all guns at once (S5E10).
- The "liquid reboot" in S6E1 returned all users to their original dimensions, i.e. the system stores the pilot's home address.
- The range is set by the Central Finite Curve, i.e. a global object.

Honest caveats: (1) a mass failure of standalone devices is not impossible, but it is possible given a common cause (one firmware, one batch of liquid); the argument is strong, but it is not a proof. (2) The "unregistered and untraceable" gun (J-22) and the contraband liquid (S3E7) work. This means that a registry is not necessary, whereas the physical layer (anchors and pairs) is necessary. We separate the two: the **log layer** (optional) and the **anchor layer** (mandatory).

**Conclusion: network architecture.** The gun is a terminal: the liquid and the pulses form the ring, while the entangled partners, addressing, the bulk channel and the absorption of dissipation belong to the network [E1]. This removes the problem of §2(a): $\sim10$ J is spent, not $10^8$.

## 3. Design by Blocks

| No. | Block (canon) | Parameters | Exists today | New physics |
|---|---|---|---|---|
| 1 | Body, handle; the prototype is bulky (S5E9) | titanium/polymer, 100 g battery | yes | no |
| 2 | Flask/cartridge with a level mark | 50 mL; two compartments (peroxide/oxalate), mixing in the nozzle; conductivity and spectrum sensor | chemiluminescent mixtures, bicelles, ferromagnetic LCs | polariton suspension at 300 K [03-D5] |
| 3 | Dispenser | piezo/MEMS, 0.2–2 mL, stoichiometry to within $\le$ a few % | yes | no |
| 4 | Vortex nozzle | $D=2$ cm, $U=20$ m/s, stroke $L=4D=8$ cm (25 mL of air), $t=4$ ms; $\mathrm{Re}\approx2.7\cdot10^4$ | yes. **[KNOWN]** formation number: $L/D=3.6$–$4.5$ (Gharib 1998); a stroke longer than 4.5 gives a jet tail and a loss of circulation | no |
| 4a | Ring inflation | radius growth from 1 cm to 1 m ($\times100$) | EHD and field in the laboratory; in free air a ring does not grow this way | **gap in 03**, [E5]: field + rim tension [03-D2] |
| 5 | Pumping (light/field) | laser diodes at the nozzle, coils (mT, platelet orientation), HV electrodes | yes | condensate with a quality factor of 2 s [03-D5] |
| 6 | Coordinate storage | local qubit register + 128-bit address ("C-137"); pairs are replenished by the network | memory 6 h (Eu:YSO, 2015), more than 10 h (ANU); ensemble of $1.5\cdot10^{13}$ atoms at 450 K, $\sim1$ ms (2020) | $10^{29}$ qubits, gap $\sim7\cdot10^{15}$ in number; [02-ASM-3,4] |
| 7 | Coordinate dial (canon) | rotary encoder into the address register; log in memory | yes | no |
| 8 | Control of $\tau$ and $\kappa$ | PID on the line shift (green, yellow, red — a fuel gauge, 03 §3) | spectrometer, MCU | $\kappa$ actuator [E3] |
| 9 | LED (canon) | green: anchor lock and mixture quality; red: no lock | yes | no |
| 10 | Self-destruct (button under a hatch) | two-stage lock, dump of all pairs at once, $\varepsilon\to1$, notification of the network | mechanics: yes | coupling dump [02-ASM-4] |

Self-destruct: dumping the coupling while the ring is alive gives a collapse in $\sim5$ ns and a short "funnel". This agrees with 02 §6: parts of objects near the rim go to the other sheet.

## 4. Firing Timeline

| Time | Event | Physics / source |
|---|---|---|
| before 0 | Anchor lock, address read, level and temperature check | network [E1] |
| 0 ms | Trigger pressed, $\tau$ and $\kappa$ fixed | control |
| 0–1 ms | Dosing of 0.5 mL, mixing of the components | piezo |
| 1–5 ms | Piston stroke, ring formation ($L/D=4$) | Gharib |
| 5–50 ms | Free flight, quantization of the core $\lesssim10$ ms | [03-D1] |
| 50–300 ms | Inflation to $R=1$ m, film with the Taylor–Culick speed $\sqrt{2\sigma/\rho h}\approx7$–8 m/s, i.e. 0.13 s per metre | 03, [E5] |
| $\approx300$ ms | Coupling $g$ switched on, rim at threshold, green LED. **Portal open** | [02-ASM-4] |
| 0.3–3.3 s | Transit window (human $\sim0.5$ s). The line shifts from green to yellow | 03 §3 |
| $\tau-0.5$ s | Red: "do not stand in the ring" | 03 §6 |
| $\tau\ldots\tau+0.3$ s | Decay of the coupling, visible closing | see below |
| final | Final collapse within ns | 02 §6 |

**The contradiction: nanoseconds versus tenths of a second.** File 02 computes a free collapse $\pi R/2c\approx5$ ns upon loss of support. File 03 gives $\sim0.1$ s as the convergence of the film. The original wording of 02-ASM-6 ("fluid inertia") does not work: the linear mass of the liquid is $\sim10^{-3}$ kg/m, at the rim it is $3.4\cdot10^{26}$ kg/m, a ratio of $10^{-29}$.

Resolution [E2]: the inertia belongs to **the rim itself**. Let the tension differ from the critical value by a fraction $\varepsilon$. Then the force per unit length is $\varepsilon T/R$, the acceleration is $\varepsilon c^2/R$, and
$$t_c\approx\frac{R}{c}\sqrt{\frac{2}{\varepsilon}}\quad\Rightarrow\quad t_c=0.1\ \text{s at}\ \varepsilon\approx2\cdot10^{-15},\qquad t_c=1\ \text{s at}\ \varepsilon\approx2\cdot10^{-17}.$$
The liquid sets only the growth rate of $\varepsilon(t)$ (decay of the pumping, 0.1–0.3 s). As long as $\varepsilon\ll1$ the rim creeps, and the avalanche finale takes ns. **[ESTIMATE, toy model, not derived from GR.]** Consequence: on a sudden pumping failure ($\varepsilon\to1$ in a jump) the closing is instantaneous, whereas a smooth one requires control of $\varepsilon$ at the $10^{-17}$ level. This is a requirement of the same kind as the fragile margin above threshold $\eta\sim10^{-24}$.

## 5. Throughput

Calculation: $N_{\rm EPR}\approx$ entropy in bits ($\approx4.3\cdot10^{26}$ bit/kg, the value for a human, an upper bound); cost $E=(\pi/2)mc^2$; $\eta=E/\lvert E_-\rvert$ (02).

| Object | $m$ | $R$ | $N_{\rm EPR}$ | $E$ | $\eta$ | Replenishment rate over 10 s |
|---|---|---|---|---|---|---|
| Human | 100 kg | 1 m | $4\cdot10^{28}$ ($10^{29}$ with margin) | $1.4\cdot10^{19}$ J | $7\cdot10^{-26}$ | $10^{28}$ pairs/s |
| Ship [E4] | 10 t | 5 m | $4\cdot10^{30}$ | $1.4\cdot10^{21}$ J | $1.5\cdot10^{-24}$ | $4\cdot10^{29}$ pairs/s |
| Citadel [E4] | $10^{12}$ kg | 1.5 km | $4\cdot10^{38}$ | $1.4\cdot10^{29}$ J (≈6 minutes of the Sun's luminosity) | $5\cdot10^{-19}$ | $4\cdot10^{37}$ pairs/s |

Conclusions:
- **Human.** A 0.5 mL dose contains $\sim10^{21}$–$10^{22}$ molecules; at the density of 02 ($10^4$ pairs per molecule) this is $\le10^{26}$, i.e. 200–1000 times less than needed. The entire 50 mL cartridge covers only 10–25 % of a human. Hence at least $99\,\%$ of the pairs must come from the anchor and the network [E1], or $10^7$–$10^8$ pairs per molecule are needed.
- **Ship.** The same reasoning applies. In addition, $R\approx5$ m is needed: the entire mass of the ship must be inside the opening.
- **Citadel.** The rim is $2.9\cdot10^{47}$ J, i.e. 1.6 $M_\odot c^2$ in absolute value: this is the scale of a star, not of a device. The anchor memory at $10^4$ qubits per molecule is no less than $\sim4\cdot10^9$ kg (4 million t). Pre-preparing the pairs at 300 K costs $10^{18}$ J. A flux of $4\cdot10^{37}$ pairs/s is unattainable by any network known today. The transfer of the Citadel (S3E1) is the work of **infrastructure**, not of the gun; the terminal merely initiates it.
- **Asymmetry.** File 02 §6 predicts that counter-traffic partially compensates for the consumption of the reserve and prolongs the lifetime.

## 6. Failure Modes

| Failure | Mechanism in the model | Effect | Protection |
|---|---|---|---|
| Spill: mini-portals (S5E9) | A drop carries pairs [02-ASM-3]; the partners are already at the anchor (Nick's cache); pumping gives a micro-ring, $\lvert E_-\rvert\propto R$ | A portal on the palm lives for seconds | Sealed compartments; coupling only when pumping is present |
| Bad liquid (S3E7) | Stoichiometry below threshold: pumping drops at the moment of transit, $\varepsilon$ jumps | Decay within $\sim R/v_T\approx0.1$ s, faster than the 0.5 s transit | Mixture tolerance of a few %, spectrum monitoring |
| Foreign admixture (Mountain Dew, S5E9) | Sugars quench the pumping, ions destroy the bicelles; the self-assembly threshold drops [03 §6a] | Thousands of uncontrolled rings | Sensor (but in canon the gun "accepted" the mixture — a discrepancy) |
| Intersecting disks (Nick, S5E9) | The disk or rim of one mouth lands in its own partner. Self-collision: curvature singularity (Feng 2021, [03]) | Both pairs vanish, and so does the carrier | Rule: "do not open a portal through a portal" |
| Overheating | Damping at $\kappa\lt 1$: 14 kJ into 0.5 g heats by $\sim7000$ K; Arrhenius: +10 °C halves $\tau$ | Evaporation of the film, breakdown of pumping | Heat sink to the anchor [E3] |
| Damping ($\kappa=0$) | $\tau=\tau_0(1-\sum E_d/E_c)$ [05] | Shortened lifetime; $41g$ overload over 0.5 m | Increasing $\kappa(\tau)$ or mode (K) |
| Mass overload | $m\gt m_{\max}$: margin $\eta$ exhausted, tension below threshold (02 §4) | Collapse with the body inside | Limit via a sensor of the mass flow |
| Network hack (S5E10) | Substitution of the address table or a dump of the pairs: coupling $g\to0$ at all terminals, $\varepsilon\to1$ | Mass collapse for those in transit (Nerdist variant: an "instant death" address without a partner) | Signed addresses, independent local reserve |
| "Liquid reboot" (S6E1) | Return of the tables to the pilots' home addresses | Everyone is returned home | Log of home addresses |

## 7. Five-Year Programme

| Year | Experiment | Tests | Criterion |
|---|---|---|---|
| 1 | Vortex gun with a DMPC/DHPC bicellar film, high-speed filming (03 §7.1–2) | Film formation in the ring, orientation, 100-fold inflation [E5], non-wetting [03-D4] | $L/D\approx4$, film on the ring, radius growth at the wall |
| 1 | Numerical stability of the Gibbons–Volkov ring (linear modes) | [02-ASM-7], [E2] | Sign of the restoring force, $t_c(\varepsilon)$ |
| 1–2 | Vortex rings in He-II ($T\lt 1.5$ K) and collision of two rings | [03-D1] (classical to quantum), an analogue of disk intersection | Quantization of the ring, outcome of the reconnection |
| 2–3 | Polariton condensate (room T, polymer) with ring pumping, quadrature noise at the rim, spectrum | [03-D5], squeezing in the core, line shift as a fuel gauge | Lifetime vs pumping; squeezing localised at the rim |
| 2–4 | SYK protocol of Jafferis 2022 (9 qubits, 164 gates, Sycamore) on 20–50 qubits; counter-propagating signals | Mechanism B: $N_{\rm send}\lesssim g$; a heavy signal destroys the correlation; counter-traffic | Scaling. **Caveat:** the protocol is tested, not the geometry (criticism by Kobrin et al.) |
| 2–5 | Casimir–Lifshitz in a colloid; negative-energy windows in squeezed vacuum | Stability of the suspension; dependence $\tau\propto\lvert E\rvert^{-1/4}$ (02 §2.3) | Repulsion is measured; the exponent agrees |
| 3–5 | Growth of ensembles: $N\times t$ (record $1.5\cdot10^{13}\times10^{-3}$ s $=1.5\cdot10^{10}$ qubit·s; need $\sim3\cdot10^{29}$, gap $\sim2\cdot10^{19}$) | [02-ASM-3,4] as a trend | A trend, not an achievement |
| 4–5 | Analogue of $\kappa$: two superfluid reservoirs connected through an aperture with a ring along the edge, measurement of momentum transfer | [05], $\kappa$ and thermal load [E3] | Dependence of $\Delta p$ on the coupling parameters |
| 5 | Archival search for negative-mass lenses | [03-D3] | A null result bounds the loop density |

[03-D3] and [02-ASM-5] cannot be tested in the laboratory. If the growth of the $N\times t$ record by the fifth year shows no trend toward $10^{29}$, the network scenario (§2c) remains the only conclusion of the model.

## 8. Engineering Assumptions

- **[E1]** The anchor network supplies the partners of the pairs, addressing and the bulk channel; the gun is a terminal.
- **[E2]** The slow closing is determined by a small $\varepsilon$ together with the enormous inertia of the rim (a reformulation of 02-ASM-6).
- **[E3]** $\kappa$ is realised by a controllable coupling; the dissipation is taken up by the anchor side.
- **[E4]** Citadel: $M=10^{12}$ kg, $R=1.5$ km; ship: 10 t, $R=5$ m. There are no canonical numbers.
- **[E5]** The inflation of the ring from 1 cm to 1 m is provided by the field and the rim tension.

## 9. Contradictions Between Files 02, 03, 05

*[reconciled at synthesis] All items are resolved in 00_summary.md (section "Resolved contradictions"); item 11 (ring inflation) remains open, this is E5.*

1. What holds the portal: coupling and entanglement (02) versus the hidden sector D3 (03); in 03 entanglement is only a fallback.
2. Collapse time 5 ns (02) versus 0.1 s (03); ASM-6 is misformulated (§4).
3. Lifetime: $10^{-20}$ s (02 without coupling) versus 2.5 s (03) and $\tau_0$ without $E_c$ (05).
4. Entanglement: $\ge10^{29}$ (02) versus a dose of $\le10^{26}$ at the density of 02 (03).
5. Temperature: 0–40 °C (03) versus 0.1 nK (02).
6. Transparency: transparent (02) versus opaque (03, lore); gas passes through an empty opening (02) versus "gas does not pass" (lore, 03).
7. Angle $\delta$: $2\pi$ (02), $\pi$–$2\pi$ (03), $\pi/2$ (05): the energy differs by a factor of 4.
8. Dissipation of 14 kJ (05) versus a dose with 2.5 J (03): an excess by a factor of 5600; the "50 g" in 05 is the whole cartridge.
9. $\kappa\lt 1$ in 05 is not derived: a thin shell gives $\kappa=1$ by default; $E_c$ is not specified.
10. The balance of 02 ("ADM $\approx0$") versus quantum interest: the positive side is not shown.
11. A 100-fold inflation of the ring is not described in 03.

## Sources

Gharib, Rambod, Shariff 1998: authors.library.caltech.edu/441 (3.6–4.5). MMRTG: en.wikipedia.org/wiki/Multi-mission_radioisotope_thermoelectric_generator. Batteries: timharper.net/battery-energy-density-2025. Entanglement record: Kong et al. 2020 (interestingengineering.com). Antimatter: fnal.gov/pub/science/inquiring/questions/antimatterprod.html. SYK protocol: physicsworld.com/a/quantum-teleportation-opens-a-wormhole-in-spacetime. Memory: Zhong 2015 (six hours) and ANU (more than ten hours), from search headlines, articles not read.
