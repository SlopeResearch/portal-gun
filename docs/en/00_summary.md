# 00. The Sanchez Portal: A Unified Model (Synthesis of Sections 01–05)

*Research team lead. 2026-10-27. Tags: **[KNOWN]** — published physics; **[ESTIMATE]** — order of magnitude; **[ASM-n]**, **[Dn]**, **[En]**, **[Mn]**, **[Sn]** — assumptions of sections 02, 03, 04, 05 and of the synthesis (register in §4). Edits to the source files are marked there as "[reconciled at synthesis]".*

## Abstract

We propose a self-consistent model of the portal gun from "Rick and Morty" that relies on known physics wherever possible.
The portal is a Gibbons–Volkov ring wormhole: a flat disk gluing two sheets of space together. All the exotica is concentrated on the rim, with a tension of $-c^4/4G$.
The rim's negative tension is created not by fuel but by a nonlocal coupling of the Gao–Jefferis–Wall type. It is paid for by entanglement between the fluid and the anchor on the destination side.
The portal fluid performs four functions: template (a quantized vortex ring), film (an opaque bicellar membrane), pumping (chemiluminescence), and a local entanglement key.
The anchor network supplies no fewer than 99% of the pairs, all addressing, and the reception of dissipation. The gun serves as a terminal.
The lifetime, the mass limit, the collapse time, and the momentum regime are reduced to four formulas with a single thermal threshold $E_c$.
The model explains all the canon scenes we checked: Nick, S3E7, S5E10, S6E1, the Citadel, and the mini-portals from spilled fluid.
One key assumption cannot be avoided without new physics: a macroscopic nonlocal coupling that creates a negative tension on the scale of "a Jupiter per metre".
All 11 contradictions between the sections are resolved. Three questions remain open: the inflation of the ring, the balance of the "quantum interest" on the anchor side, and the microphysics of the parameter $\kappa$.
The research programme of 10 items includes 6 experiments that are feasible today.

---

## 1. What Is Known from Canon (after 01 §7)

| No. | Requirement | Status | 01 |
|---|---|---|---|
| R1 | The portal is a flat disk, its orientation is arbitrary, no support is needed | semi-canon | §3, §7.1 |
| R2 | Opaque: the other side cannot be seen until you step in | semi-canon | §3, §7.2 |
| R3 | Passage is two-way while the portal is open | semi-canon | §7.3 |
| R4 | The lifetime is finite and set by the user, no number given | semi-canon | §3, §7.4 |
| R5 | The edge does not cut during passage, but cuts when opened inside an object and at collapse | semi-canon | §3, §7.5 |
| R6 | Intersection of a pair is lethal (Nick, S5E9) | canon | §2, §7.6 |
| R7 | Momentum: there are scenes of fall damping; momentum-conservation scenes are not confirmed | semi-canon | §3, §7.7; 05 §1 |
| R8 | Gas does not pass through (Fart, S2E2) | semi-canon | §3, §7.8 |
| R9 | Size from a palm (S5E9) to the Citadel (S3E1) | canon | §3, §7.9 |
| R10 | A consumable fluid is needed; a spill produces mini-portals; bad fluid kills (S3E7); failure is nonlocal (S5E10, S6E1); range is limited by the Curve | canon | §2, §4, §7.10–13 |

---

## 2. The Unified Model of the Sanchez Portal

### 2.1. Postulates

- **P1. Geometry.** The portal is a vacuum Gibbons–Volkov ring wormhole [4]: two Minkowski sheets glued along a disk of radius $R$ with orientation preserved. On the faces $T_{\mu\nu}=0$ and the curvature tensor vanishes, so there are no tidal forces [2, 4]. **[KNOWN]**
- **P2. Rim.** The angle excess is $|\delta|=2\pi$, i.e. the linear density is $\mu=-c^2/4G$. The rim is regularized by a tube of radius $a$, where $\ell_P\ll a\ll R$. Its position is set by the core of the fluid's quantized vortex ring [03 §1.2]. **[KNOWN] + [D1], [ASM-7]**
- **P3. Source of tension.** The negative averaged NEC on the rim is provided by a nonlocal coupling $\delta H=g\sum_i\mathcal O^{(1)}_i\mathcal O^{(2)}_i$ between the modes of the rim and of the anchor [13–16]. Local QFT mechanisms (squeezed vacuum, Casimir) serve as a seed and as a precision reserve, but not as the foundation. **[S1]**
- **P4. Resource.** The coupling consumes entangled pairs. The fluid carries a local key ($\le10^{26}$ pairs per dose); the anchor network supplies $\ge99\,\%$ of the pairs, the addressing, and the classical channel through the bulk. **[E1], [ASM-3,4,5]**
- **P5. Film.** A bicellar membrane 0.1–1 μm thick is stretched over the rim: it is opaque, gas-tight, and self-healing [03]. The film is the only matter in the opening. **[KNOWN-prototype] + [D4, D6]**
- **P6. Frame gluing.** The isometry of the shell transfers the 4-velocity with a stiffness parameter $\kappa\in[0,1]$. The value of $\kappa$ is stored in the pair; at $\kappa\lt 1$ the dissipation is taken up by the anchor. **[M1], [E3]**

### 2.2. Key Formulas

**Rim energy** (02 §1.3, $\delta=2\pi$):
$$|\mu|=\frac{c^2}{4G}=3.4\cdot10^{26}\ \tfrac{\text{kg}}{\text{m}},\qquad |E_-|=\frac{\pi Rc^4}{2G}=1.9\cdot10^{44}\ \text{J}\cdot\frac{R}{1\ \text{m}},\qquad M_{\rm ADM}=0\ \text{(ideal GV)}.$$

**Collapse** (E2, replaces ASM-6): for a relative tension shortfall $\varepsilon$
$$t_c\approx\frac{R}{c}\sqrt{\frac{2}{\varepsilon}},\qquad t_c\ge\frac{\pi R}{2c}\approx5\ \text{ns}.$$
The visible 0.1–0.3 s correspond to $\varepsilon\sim10^{-15}$–$10^{-16}$ with a smooth decay of the pumping. The final avalanche takes nanoseconds. **[ESTIMATE, toy model]**

**Lifetime** (single formula):
$$\boxed{\tau=\min\{\tau_{\rm pump},\ \tau_{\rm couple}\}\cdot\Big[1-\frac{f_{\rm loc}\sum E_d}{E_c}\Big],\qquad \sum m_i\le m_{\max}}$$
where
- $\tau_{\rm pump}=\eta\,\varepsilon_{\rm chem}V/P_{\rm loss}(T)$ is the chemical pumping resource of the dose. For $V=0.5$ mL we get $\approx2.5$ s at 20 °C; $\tau_{\rm pump}$ halves with every +10 °C (03 §4);
- $\tau_{\rm couple}=N_{\rm EPR}/\dot N_{\rm EPR}$ is the time for which the network sustains the coupling (02 §7);
- $E_c\equiv\rho V c_p\,(T_{\max}-T)$ is the **single thermal threshold of the dose**. For 0.6 g, $c_p\approx2$ J/(g·K), $T_{\max}=40$ °C and $T=20$ °C we get $E_c\approx25$ J. The threshold depends on both the dose and the temperature, so it links 03 and 05;
- $E_d=\tfrac12mv_{\rm rel}^2(1-\kappa^2)$ is the dissipation during damping (05 §5); $f_{\rm loc}\lesssim5\cdot10^{-4}$ is the fraction of the dissipation that stays in the dose (the rest goes to the anchor, E3, S3).

If the coupling is switched off, $\tau\to\tau_{\rm QI}\lesssim(3N\hbar Ra^2/16c^3|E_-|)^{1/4}\sim10^{-28}$–$10^{-20}$ s (02 §2.3). The canonical "seconds" exist only while the coupling is alive.

**Mass limit** (02 §4):
$$m_{\max}=\min\Big\{\frac{2}{\pi}\frac{\eta|E_-|}{c^2},\ \frac{N_{\rm EPR}}{n_{\rm bit}}\Big\},\qquad n_{\rm bit}\approx4.3\cdot10^{26}\ \text{bit/kg}.$$
For $m_{\max}=1$ t the reserve is $\eta\approx7\cdot10^{-25}$. Passing 100 kg costs $(\pi/2)mc^2=1.4\cdot10^{19}$ J of negative energy drawn from the reserve.

**Frame gluing** (05 §3, §6):
$$u_2^\mu=E_2\,\mathcal R\,E_1^{-1}u_1^\nu,\qquad \mathbf v_{\rm out}=\mathbf V_2+\kappa\,\mathcal R\,(\mathbf v_{\rm in}-\mathbf V_1),\qquad \mathcal R=\mathrm{diag}(1,R_\alpha,-1).$$

### 2.3. The "Gun — Fluid — Anchor — Network" Architecture

| Level | Function | Physics | Resource |
|---|---|---|---|
| **Gun** (terminal) | dispenser, vortex nozzle, pumping, address register, control of $\tau$ and $\kappa$, LED | vortex rings [21], EHD, spectrometer | 100 g battery, $\sim10^4$ shots of 5–15 J |
| **Fluid** (local key) | rim template, film, chemiluminescent pumping, $\le10^{26}$ pairs, authentication | bicelles, ferro-LC, polariton condensate [24], BPEA | 0.5 mL per portal, 50 mL cartridge |
| **Anchor** (remote mouth) | pair partners, local frame $E_2$, reception of dissipation and of the "quantum interest" | ASM-4, E3 | $\ge99\,\%$ of the pairs |
| **Network** (infrastructure) | addressing ("C-137"), log, classical channel through the bulk, coverage = Central Finite Curve | ASM-5, RS bulk [19] | up to $10^{28}$ pairs/s per person |

The log layer is optional: the J-22 gun is "unregistered and untraceable", and bootleg fluid works. The anchor layer is mandatory.

### 2.4. Firing Timeline (nominal: $R=1$ m, 0.5 mL, $\tau=3$ s)

| Time | Event | Rationale |
|---|---|---|
| before 0 | anchor capture by address, check of level, spectrum, temperature | E1 |
| 0–1 ms | dispensing 0.5 mL, mixing of the two components in the nozzle | 03 §5 |
| 1–5 ms | piston stroke, vortex ring at $L/D\approx4$ | [21] |
| 5–50 ms | flight, quantization of the vortex core | D1 |
| 50–300 ms | inflation to 1 m, stretching of the film ($\approx8$ m/s) | 03; **E5 (open)** |
| $\approx0.3$ s | coupling $g$ switches on, rim at threshold, green LED: **portal open** | P3 |
| 0.3–3.3 s | passage window; the glow line shifts from green to yellow | 03 §3 |
| $\tau-0.5$ s | red colour: "don't stand in the ring" | 03 §6 |
| $\tau\ldots\tau+0.3$ s | pumping decays, $\varepsilon$ grows, visible contraction | E2 |
| final | avalanche within nanoseconds, the film contracts onto the rim | 02 §6 |

---

## 3. How the Model Explains the Canon Scenes

| Scene / fact | Mechanism in the model |
|---|---|
| Flat disk at any angle, in mid-air (R1) | The plane of the vortex ring is perpendicular to the firing vector; near a wall the ring expands, so the portal is turned toward the shooter |
| Opacity, "jelly" on touch (R2) | A bicellar film with a phosphor and scattering platelets: optically thick, elastic |
| Gas does not pass (Fart, S2E2) | The film is gas-tight; a solid body passes at $\mathrm{We}\gg1$, and the film self-heals [23]. Natural wormholes have no film, so gas passes through them |
| "In fast, out fast" regime | $\kappa=1$: Israel's geodesic gluing, $\mathbf v_{\rm out}=\mathcal R\mathbf v_{\rm in}$, $E_d=0$, the portal's life is not shortened |
| Damping of a fall | $\kappa=0$: 14 kJ (70 kg, 20 m/s) goes to the anchor. Predictions: an injury of $\sim41g$ under instantaneous damping, hence a ramped $\kappa(\tau)$ is needed; after damping, the portal closes earlier by $\sim30\,\%$ |
| Cutting of the Gromflomite (S2E2) | The portal is opened inside the body: the rim passes through the matter and carries the parts to different sheets. This is a topological, perfectly smooth cut |
| Death of Nick (S5E9) | The mouth lands in its own partner: self-collision of a portal wormhole gives a curvature singularity [22]; both pairs and the carrier perish |
| Mini-portal on the palm (S5E9) | The drop carries a fragment of the key; the anchor is the last address used (Nick's stash). $\lvert E_-\rvert \propto R$, so a micro-ring is cheap |
| Mountain Dew (S5E9) | The sugars partially quench the pumping, and the ions lower the self-assembly threshold. The gun works, but the sensor beeps, and Rick notices the top-up by the notch. The two wiki versions agree: "accepted" and "warned" |
| Counterfeit, "math was off" (S3E7) | Stoichiometry below tolerance: midway through the passage $\varepsilon$ jumps, $t_c\sim0.1$ s is shorter than the 0.5 s passage, and the rim passes through the body |
| Log of destinations (S1E10) | The network's log layer and the gun's address register |
| Evil Morty's hack (S5E10) | Substitution of the address table or a dump of pairs at the network level: for all terminals $g\to0$, $\varepsilon\to1$, collapse within nanoseconds for those in transit. The Nerdist variant is an address without an anchor ("instant death") |
| Black hole in S5E10 | A set of loops of different signs (convex and concave Visser edges) gives a total positive mass and collapse (03 §6a). Conjecture |
| Golden portal beyond the Curve (S5E10) | A different anchor network with different coverage. The mechanism is not derived; this is an open question |
| "Fluid reboot" (S6E1) | A reset of the tables to the pilots' home addresses; everyone returns home. The network stores the home address |
| Relocation of the Citadel (S3E1) | $R\approx1.5$ km, rim $2.9\cdot10^{47}$ J ($\approx1.6\,M_\odot c^2$), $4\cdot10^{37}$ pairs/s. This is the work of the infrastructure; the gun merely initiates [E4] |
| Self-destruction of the gun | A dump of all pairs with the ring alive: $\varepsilon\to1$, collapse within $\sim5$ ns, objects near the rim go to the other sheet ("suction") |
| Green colour | BPEA chemiluminescence near the peak of the eye's sensitivity; the shift of the line works as a fuel gauge |
| Range limited by the Curve | Coverage of the anchor network: without an anchor there are no pair partners |
| Several portals at once (S1E10) | Independent pairs with different anchors, each consuming its own dose |

---

## 4. Assumption Register

Strength ratings: **K** — known physics; **E** — extrapolation of the known; **N** — new physics.

| No. | Assumption | Section | Strength |
|---|---|---|---|
| 1 | A flat-faced/ring wormhole as a solution of GR | 02 P1, 05 §3 | K |
| 2 | ASM-1: a stable macroscopic ring with tension $-c^4/4G$ | 02 | **N** (included in S1) |
| 3 | ASM-2: violation of the achronal ANEC (only by a nonlocal coupling) | 02 | N, reduced to S1 |
| 4 | ASM-3: an entanglement reservoir in the fluid; cut down at synthesis to a key of $\le10^{26}$ pairs | 02, 04 | E (the $N\times t$ record falls short by a factor of $2\cdot10^{19}$) |
| 5 | ASM-4: the pair partners are already at the anchor | 02 | **N** |
| 6 | ASM-5: classical channel by a short path through the bulk | 02 | **N** (RS models are known, but the short path is speculative) |
| 7 | ASM-6: the inertia of the fluid slows the collapse | 02 | **rejected**, replaced by E2 |
| 8 | ASM-7: the regularization of the rim is stable and preserves zero tides | 02 | E (problem unsolved) |
| 9 | D1: fast quantization of a metre-scale vortex ring | 03 | E |
| 10 | D2: balance of the rim tension and the film | 03 | E, at synthesis regulated through $\varepsilon$ |
| 11 | D3: a hidden sector with negative strings | 03 | N, **downgraded to a fallback** |
| 12 | D4: the film does not wet the skin | 03 | E (engineering problem) |
| 13 | D5: core quality factor at the level of SC resonators (seconds) | 03 | E, strong |
| 14 | D6: the film holds the atmospheric pressure difference | 03 | E, strong (a strength of $\sim5\cdot10^{10}$ Pa is needed) |
| 15 | E1: anchor network and gun-terminal | 04 | N (infrastructure) |
| 16 | E2: slow closure at small $\varepsilon$ | 04 | E (not derived from GR) |
| 17 | E3: $\kappa$ is controllable, dissipation goes to the anchor | 04 | N |
| 18 | E4: the scales of the Citadel and of the ship | 04 | a parameter, not physics |
| 19 | E5: hundredfold inflation of the ring by a field | 04 | E, **not justified** |
| 20 | M1: parameter $\kappa\lt 1$ (non-isometric gluing) | 05 | N |
| 21 | M2: the rim is tied to the shell, not to the gun (ban on Bondi runaway) | 05 | E |
| 22 | S1: the macroscopic GJW coupling gives the tension $c^4/4G$ | synthesis | **N, the most expensive** |
| 23 | S2: the coupled rim modes are thermally decoupled from the environment (effectively 0.1 nK at 300 K) | synthesis | E, strong |
| 24 | S3: $f_{\rm loc}\lesssim5\cdot10^{-4}$, the "quantum interest" and the dissipation are taken up by the anchor | synthesis | N (a consequence of S1/E3) |

**The most expensive assumption is S1** (it unites ASM-1, ASM-2, and the role of D3). The nonlocal coupling must deliver a negative energy of $1.9\cdot10^{44}$ J per metre of radius, i.e. about $-1.1\,M_{\rm Jup}c^2$. The laboratory protocol [17] works on 9 qubits, and the MMP wormholes [16] are microscopic. The scale gap cannot be assessed: known physics does not even give a direction of extrapolation. The second most expensive assumption is ASM-4: the anchors must already stand at the destination points.

---

## 5. Resolved Contradictions

1. **What holds the portal.** The coupling of 02 (P3) is adopted. D3 from 03 is redundant and is downgraded to a fallback: if S1 does not deliver the required magnitude, D3 will take its place without changing the rest of the architecture. The fluid sets the geometry: the vortex determines where the coupled modes sit. Edit: 03 §2.1.
2. **Collapse.** ASM-6 is rejected: the fluid is lighter than the rim by a factor of $10^{29}$. E2 is adopted: $t_c\approx(R/c)\sqrt{2/\varepsilon}$. The visible 0.1 s gives $\varepsilon\approx2\cdot10^{-15}$, while 5 ns is the lower limit at $\varepsilon\to1$ (coupling dump, hack, self-destruction). Edit: 02 §6, §7.
3. **Lifetime.** The single formula of §2.2. $10^{-20}$ s is the limit without coupling, 2.5 s is $\tau_{\rm pump}$ of a 0.5 mL dose, and $\tau_0$ from 05 equals $\min\{\tau_{\rm pump},\tau_{\rm couple}\}$. A single threshold $E_c=\rho Vc_p(T_{\max}-T)\approx25$ J is introduced. Edit: 05 §5.
4. **Entanglement.** Fixed: "the fluid is the local key, the network is the resource". A dose contains $\le10^{26}$ pairs, a person needs $10^{29}$, so $\ge99\,\%$ of the pairs come from the anchor. Edit: 02 §7.
5. **Temperature.** The physical temperature of the fluid is 0–40 °C. "0.1 nK" is the energy scale of the coupled channel $\hbar\ln S/2\pi t_*$, not the temperature of the medium; maintaining it requires decoupling (S2). Edit: 02 §8.
6. **Transparency and gas.** The bare geometry is transparent (02), but the opening is covered by a bicellar film (P5). Therefore the portal is opaque from both sides, the exit is not visible before passage, gas does not pass, and this agrees with R2 and R8. Light is almost free for the budget (02 §6): a thin film would give a "window" (prediction). Edit: 02 §1.4, 03 §6.
7. **Deficit angle.** $|\delta|=2\pi$ is adopted: only it gives an exactly flat opening. $|\mu|=c^2/4G$, $|E_-|=1.9\cdot10^{44}$ J/m, and the rim recoil in 05 is recomputed ($7\cdot10^{-25}$ m/s). The conclusions of 03 and 05 do not change. Edits: 03 §2.1, 05 §4.
8. **Dissipation.** 14 kJ in 0.6 g would heat the dose by $\sim7000$ K. The energy leaves through the coupling channel to the anchor (E3). What remains in the dose is $f_{\rm loc}\lesssim5\cdot10^{-4}$, i.e. $\lesssim7$ J $\lt E_c$. The "50 g" in 05 is the whole cartridge. Edit: 05 §5.
9. **$\kappa$.** Israel's conditions on a bare disk give $\kappa=1$. Honestly: $\kappa\lt 1$ is a non-isometric gluing, and it cannot be derived from a thin shell. We treat it as a degree of freedom of the coupling $\delta H$ on the network side: the anchor sets the frame $E_2$ and takes up the difference. This remains an assumption of the M1/E3 "new physics" class; the testable predictions of 05 §6 are retained.
10. **ADM and quantum interest.** In the ideal Gibbons–Volkov case $M_{\rm ADM}=0$ exactly, because the geometry is flat. The quantum interest refers to the fluctuating part: the reserve $\eta$ and the cost of passage $(\pi/2)mc^2$. By Visser's accounting, the mass of the body passes from the entrance mouth to the exit mouth, and the positive "return" beyond that is paid by the anchor (S3). The scale per person is up to $10^{19}$ J per session at the anchor; see §6.
11. **Cartridge and soda.** Baseline: 50 mL in two compartments, $\sim100$ short portals (0.5 mL, $\sim3$ s) or $\sim25$ long ones (2 mL, $\sim10$ s). Mountain Dew: the gun works on the diluted mixture, but the sensor beeps and the self-assembly threshold drops, hence the tendency toward mini-portals; Rick sees the top-up by the notch. Edit: 03 (parameters). Item 11 from the list of 04 (ring inflation) is not resolved and is carried over to §6.

---

## 6. What Remains Unexplained

1. **The magnitude of S1.** There is neither a derivation nor an extrapolation: from the 9-qubit protocol to $10^{44}$ J.
2. **Where the anchors in a new world come from** (ASM-4). Area-law vacuum entanglement requires a resolution of $\sim6$ fm on a disk of $\pi$ m² (04 §2). The first visit to an unknown dimension is not explained by the model.
3. **Instantaneity.** GJW requires a classical channel; the transition "without delay" rests on ASM-5 (a short path through the bulk). The risk of closed timelike curves with moving mouths [05 §2] is not excluded.
4. **Hundredfold inflation of the ring** (E5): in free air a vortex ring does not grow like this.
5. **Stability of the rim** (ASM-7): a linear perturbation analysis of the Gibbons–Volkov ring has not been carried out.
6. **Quantum interest on the anchor side:** up to $10^{19}$ J per person. Where the anchor puts this energy is unknown.
7. **Pressure difference** (D6): the film holds $\sim0.1$ Pa, not an atmosphere. Portals into vacuum or underwater are not yet described by the model.
8. **Microphysics of $\kappa\lt 1$** and the role of living/non-living (prediction: the regime belongs to the pair).
9. **The golden portal** and exit beyond the Curve: no mechanism.
10. **Canon on momentum:** conservation scenes are not confirmed frame by frame (05 §1); the model may be explaining a regime that is not in the show.
11. **Energetics of the Citadel:** $1.6\,M_\odot c^2$ on the rim. Even for an infrastructure, this is the scale of a star.

---

## 7. Research Programme

Priorities: **P1** — critical for the model, **P2** — test subsystems, **P3** — exploratory. "Today" means feasible with existing means.

| No. | Experiment / calculation | Tests | Priority | Today? |
|---|---|---|---|---|
| 1 | Linear stability of the regularized Gibbons–Volkov ring; derivation of $t_c(\varepsilon)$ from GR | ASM-7, E2 | P1 | yes (numerical relativity) |
| 2 | Scaling the protocol [17] to 20–50 qubits; counter-propagating signals; a heavy signal kills the correlation | P3, mechanism B, "counter-traffic extends life" | P1 | yes (quantum processors) |
| 3 | Vortex gun with a DMPC/DHPC film, high-speed imaging, growth near a wall | P5, orientation, E5 | P1 | yes (benchtop setup) |
| 4 | $\kappa$ model: two superfluid reservoirs through an aperture with a ring, momentum transfer | M1, E3 | P2 | partly |
| 5 | Vortex rings in He-II, collision of two rings (analogue of Nick) | D1, R6 | P2 | yes |
| 6 | Polariton condensate at 300 K with ring pumping: lifetime, squeezing on the rim, line shift | D5, fuel gauge | P2 | yes |
| 7 | Self-healing of the film at We ≈ $5\cdot10^4$, pressure difference, non-wetting | D4, D6 | P2 | yes |
| 8 | Trend of the $N\times t$ record for entangled ensembles (need $3\cdot10^{29}$ qubit·s) | ASM-3, E1 | P2 | trend monitoring |
| 9 | QI for thin rings: numerical check of $\tau\propto a^{1/2}\lvert E\rvert ^{-1/4}$ | 02 §2.3 | P3 | yes (theory) |
| 10 | Search for negative-mass gravitational lenses in archives | D3 (fallback) | P3 | yes (archival data) |

Criterion of model failure: if item 1 shows instability for any $\varepsilon$, and item 2 shows no scaling $N_{\rm send}\lesssim g$, the unified model loses the support of P3 and switches to D3.

---

## 8. Document Map

| File | Contents |
|---|---|
| `00_summary.md` | this synthesis: postulates, formulas, arbitration, register, programme |
| `01_lore.md` | canon with confidence levels, corrections to the brief, 15 requirements (§7), list of sources |
| `02_physics.md` | disk wormhole, QI and lifetime, ER=EPR/GJW, mass limit, inter-universe transitions, ASM-1…7 |
| `03_fluid.md` | self-assembly (vortex + bicelles), carrier of the exotica, glow, consumption, production, D1…D6 |
| `04_engineering.md` | parameters, energy balance, network architecture, units, firing timeline, failure modes, 5-year plan, E1…E5, list of contradictions |
| `05_momentum.md` | lore of the momentum regimes, Israel gluing, $\kappa$, energetics of damping |

---

## 9. References

1. M. S. Morris, K. S. Thorne, *Am. J. Phys.* **56**, 395 (1988).
2. M. Visser, *Traversable wormholes: Some simple examples*, Phys. Rev. D **39**, 3182 (1989); arXiv:0809.0907.
3. M. Visser, *Traversable wormholes from surgically modified Schwarzschild spacetimes*, Nucl. Phys. B **328**, 203 (1989); arXiv:0809.0927.
4. G. W. Gibbons, M. S. Volkov, *Ring wormholes via duality rotations*, Phys. Lett. B **760**, 324 (2016); arXiv:1606.04879.
5. G. W. Gibbons, M. S. Volkov, *Weyl metrics and wormholes*, JCAP **05** (2017) 039; arXiv:1701.05533.
6. L. H. Ford, T. A. Roman, *Quantum field theory constrains traversable wormhole geometries*, Phys. Rev. D **53**, 5496 (1996); arXiv:gr-qc/9510071.
7. L. H. Ford, T. A. Roman, *The quantum interest conjecture*, Phys. Rev. D **60**, 104018 (1999); arXiv:gr-qc/9901074.
8. E.-A. Kontou, K. Sanders, *Energy conditions in general relativity and quantum field theory*, Class. Quantum Grav. **37**, 193001 (2020); arXiv:2003.01815.
9. B. Freivogel, D. Krommydas, *The smeared null energy condition*, JHEP **12** (2018) 067; arXiv:1807.03808.
10. N. Graham, K. D. Olum, *Achronal averaged null energy condition*, Phys. Rev. D **76**, 064001 (2007); arXiv:0705.3193.
11. M. Visser, S. Kar, N. Dadhich, Phys. Rev. Lett. **90**, 201102 (2003); arXiv:gr-qc/0301003.
12. J. Maldacena, L. Susskind, *Cool horizons for entangled black holes*, Fortsch. Phys. **61**, 781 (2013); arXiv:1306.0533.
13. P. Gao, D. L. Jafferis, A. C. Wall, *Traversable wormholes via a double trace deformation*, JHEP **12** (2017) 151; arXiv:1608.05687.
14. J. Maldacena, D. Stanford, Z. Yang, *Diving into traversable wormholes*, arXiv:1704.05333.
15. J. Maldacena, X.-L. Qi, *Eternal traversable wormhole*, arXiv:1804.00491.
16. J. Maldacena, A. Milekhin, F. Popov, *Traversable wormholes in four dimensions*, arXiv:1807.04726.
17. D. Jafferis et al., *Traversable wormhole dynamics on a quantum processor*, Nature **612**, 51 (2022); critique: B. Kobrin, T. Schuster, N. Yao, arXiv:2302.07897.
18. G. Dvali, *Black holes and large N species solution to the hierarchy problem*, arXiv:0706.2050.
19. L. Randall, R. Sundrum, *An alternative to compactification*, Phys. Rev. Lett. **83**, 4690 (1999); arXiv:hep-th/9906064.
20. J. G. Cramer, R. L. Forward, M. S. Morris, M. Visser, G. Benford, G. A. Landis, *Natural wormholes as gravitational lenses*, Phys. Rev. D **51**, 3117 (1995); arXiv:astro-ph/9409051.
21. M. Gharib, E. Rambod, K. Shariff, *A universal time scale for vortex ring formation*, J. Fluid Mech. **360**, 121 (1998).
22. J. C. Feng, *Self-collision of a portal wormhole*, arXiv:2105.03433 (2021).
23. T. Killian, J. Huey, J. Bryson, T. Truscott, *Self healing soap films*, arXiv:1210.3797 (2012).
24. J. D. Plumhof et al., *Room-temperature Bose–Einstein condensation of cavity exciton–polaritons in a polymer*, Nature Mater. **13**, 247 (2014).
25. M. A. Khamehchi et al., *Negative-mass hydrodynamics in a spin-orbit-coupled Bose–Einstein condensate*, Phys. Rev. Lett. **118**, 155301 (2017); arXiv:1612.04055.

*Additional (no arXiv, see the sections): W. Israel, Nuovo Cimento B **44**, 1 (1966); C. Barceló, S. Liberati, M. Visser, Living Rev. Relativ. **8**, 12 (2005), arXiv:gr-qc/0505065; E. Poisson, M. Visser, Phys. Rev. D **52**, 7318 (1995), arXiv:gr-qc/9506083. Status: the arXiv numbers are taken from sections 02, 03, 05, where they were verified by search; number [22] was re-confirmed at synthesis.*
