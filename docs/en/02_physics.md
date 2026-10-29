# 02. Portal Physics: A Disk Wormhole, Exotic Matter on the Rim, and Entanglement as "Coordinates"

*Survey note by the lead theorist. The file `01_lore.md` was missing, so the work proceeds from the original premises: the gun sprays a liquid, the liquid forms an oriented disk, the disk lives for seconds, passes a limited mass, is transparent from both sides, and does not cut the body passing through it.*

**Claim labelling** (used throughout the text):
- **[KNOWN]** — a published result; a reference is given.
- **[ESTIMATE]** — our order-of-magnitude estimate based on known formulas; coefficients of order unity are not guaranteed.
- **[ASM-n]** — an explicit assumption that goes beyond known physics. All such assumptions are collected in §7.

Units: SI unless stated otherwise; $\ell_P=\sqrt{\hbar G/c^3}\approx1.6\times10^{-35}$ m.

---

## 1. Geometry: Why a Disk and Not a Sphere

### 1.1. Morris–Thorne and thin shells
Morris and Thorne [1] wrote a static, spherically symmetric traversable wormhole in the form
$$ds^2=-e^{2\Phi(r)}c^2dt^2+\frac{dr^2}{1-b(r)/r}+r^2d\Omega^2,$$
where $b(r_0)=r_0$ defines the throat, and the "flare-out" condition $b'(r_0)\lt 1$ leads to $\rho c^2+p_r\lt 0$ at the throat, that is, to a violation of the null energy condition (NEC) **[KNOWN]**. The traveler passes straight through the exotic matter.

Visser [3] constructed a "surgical" thin-shell wormhole: balls of radius $a$ are cut out of two copies of space, and the boundaries are glued together. By the Israel junction conditions (the jump of the extrinsic curvature $[K_{ij}]$ gives the surface tensor $S_{ij}$), for two flat copies one obtains
$$\sigma=-\frac{c^2}{2\pi G a},\qquad M_{\rm shell}=4\pi a^2\sigma=-\frac{2ac^2}{G}.$$
The exotic matter is spread over the whole sphere, and a body passing through crosses it **[KNOWN, coefficients as in [3]]**.

### 1.2. Key result: flat faces carry no matter
In [2] Visser considered wormholes without spherical symmetry, for example a "cubical" one: a polyhedron is cut out of space, and the faces of the two copies are glued together. On a **flat** face the jump of the extrinsic curvature is zero, hence $S_{ij}=0$. A quote from [2]: a traveler who meets such a flat face "will not feel tidal forces and will not see any matter, exotic or otherwise". All the exotica is concentrated on the edges, and a convex edge has **negative tension**, like a cosmic string with a "minus sign" **[KNOWN]**.

The limiting case of a polyhedron with one face is the **disk**. Gibbons and Volkov [4, 5] obtained it as an exact vacuum solution of general relativity (the vacuum Zipoy–Voorhees–Weyl class, a "ring wormhole"). At a ring tension of exactly $T=-c^4/4G$ the geometry is **exactly flat** but topologically nontrivial: it is "two copies of Minkowski space glued along a disk". Geodesics are straight lines, and those that cross the disk emerge in another universe. The authors describe this as a ring that "literally punches a hole in space" **[KNOWN, [4]]**. This is our portal.

### 1.3. The metric of the disk portal
A convenient form is Minkowski space in oblate spheroidal coordinates (this is the Kerr limit at $M=0$; see the discussion in [4]):
$$ds^2=-c^2dt^2+\frac{r^2+R^2\cos^2\theta}{r^2+R^2}\,dr^2+(r^2+R^2\cos^2\theta)\,d\theta^2+(r^2+R^2)\sin^2\theta\,d\varphi^2 .$$
The surface $r=0$ is a disk of radius $R$. Ordinary space corresponds to $r\gt 0$, while the **continuation to $r\lt 0$** gives a second sheet, that is, a second universe. Crossing the disk, you pass from the sheet $r\gt 0$ to the sheet $r\lt 0$. The ring $r=0,\ \theta=\pi/2$ is a conical singularity with an angle **excess** of $2\pi$: a loop around the rim passes through both sheets, so the total angle is $4\pi$.

For a straight string the angle deficit is related to the linear density by $\delta=8\pi G\mu/c^2$. Hence at $\delta=-2\pi$
$$\mu=-\frac{c^2}{4G}\approx-3.4\times10^{26}\ \text{kg/m},\qquad T=\mu c^2=-\frac{c^4}{4G}\approx-3.0\times10^{43}\ \text{N},$$
which coincides with the Gibbons–Volkov threshold tension **[KNOWN + ESTIMATE]**. The total negative energy of the rim is
$$E_-=2\pi R\,\mu c^2=-\frac{\pi R c^4}{2G}\approx-1.9\times10^{44}\ \text{J}\cdot\left(\frac{R}{1\ \text{m}}\right),$$
that is, about $-1.1\,M_{\rm Jup}c^2$ for $R=1$ m. This agrees with the "Jupiter mass per meter" estimate from [5] **[KNOWN]**. Moreover, for a string $\rho+\sum p=\mu c^2-\mu c^2=0$, so the Tolman (ADM) mass of the portal as seen from outside is ≈ 0: the portal does not attract surrounding objects **[ESTIMATE]**.

### 1.4. Summary of the "disk versus sphere" comparison
| | Sphere (Visser [3]) | Disk (Visser [2], Gibbons–Volkov [4]) |
|---|---|---|
| Where the exotica is | the entire surface, $\propto R^2$ by area | the rim only, $\propto R$ |
| $\lvert E_-\rvert$ | $2Rc^4/G$ | $(\pi/2)Rc^4/G$ |
| Does the traveler touch the exotica | yes | no |
| Tidal forces in the opening | $\neq0$ | exactly 0 |

**Honestly:** in total energy the disk wins only by a factor of $4/\pi$. The decisive advantage of the disk is **operational**: the opening is empty and flat. In addition, the disk is naturally oriented and has a normal, which agrees with canon. The gluing "front side of $D_1$ ↔ back side of $D_2$" preserves orientation, so the traveler does not emerge mirror-reflected. From both sides of the disk the second universe is visible, since the rays travel along straight lines: the back side of $D_1$ is glued to the front side of $D_2$. *[reconciled at synthesis] This holds for the bare geometry. In the unified model the opening is closed by a gel bicellar film of the liquid (03 §1.2), so the visible portal is opaque (scattering) and gas-tight, as in canon.*

---

## 2. Energy Conditions and Quantum Inequalities

### 2.1. What is violated
Traversability requires a violation of the NEC ($T_{\mu\nu}k^\mu k^\nu\ge0$), and for a "shortcut" the **achronal averaged** NEC (AANEC) must be violated as well. Graham and Olum showed that in semiclassical gravity the AANEC forbids both wormholes and closed timelike curves [10]. The ANEC in flat space has been proven for local QFTs (review [8]). Consequently, **a "shortcut" portal with a local QFT on the background is impossible; one needs either a nonlocal source (§3) or new physics [ASM-2]** **[KNOWN]**.

Local QFT does permit a negative energy density: this is the Casimir effect $\rho_{\rm Cas}=-\pi^2\hbar c/(720\,d^4)$ and squeezed vacuum states. However, its magnitude and duration are bounded by the **quantum inequalities** (QI).

### 2.2. The Ford–Roman inequality
For a massless scalar in 4D with Lorentzian sampling of width $\tau_0$ [6]:
$$\frac{\tau_0}{\pi}\int_{-\infty}^{\infty}\frac{\langle T_{\mu\nu}u^\mu u^\nu\rangle\,d\tau}{\tau^2+\tau_0^2}\ \ge\ -\frac{3\hbar}{32\pi^2c^3\tau_0^4}.$$
This is a relation of the "energy–time" type: **the deeper the dip, the shorter it can last** **[KNOWN]**. Applying it to Morris–Thorne throats [6] gives the following. Either the throat is only slightly larger than the Planck scale, or the negative energy is confined to a layer of thickness $a_0\lesssim(r_0/8f^4\ell_P)^{1/3}\ell_P$. For $r_0=1$ m and $f\approx0.01$ this is $a_0\lesssim10^{14}\ell_P\approx10^{-21}$ m. The thinner the band, the better the QI are satisfied, and [6] explicitly mentions Visser's cubical wormholes as a possibility **[KNOWN]**. Hence the conclusion: **the geometry "exotica only on a thin rim" is not a whim but precisely what the quantum inequalities prefer.**

In addition, the "quantum interest" [7] requires that a negative energy pulse be followed, within a time $\sim\tau$, by a positive pulse of larger magnitude: the "loan" must be repaid with interest **[KNOWN]**.

### 2.3. Derivation of the lifetime $\tau(R,E)$ **[ESTIMATE]**
Let the rim be a torus with tube radius $a\ll R$, and let the negative energy be supplied by $N$ independent fields, so that the right-hand sides of the QI add up. The energy density in the tube is
$$|\rho|=\frac{|E_-|}{2\pi^2Ra^2}.$$
A constant density violates the QI if it persists longer than $\tau$. Substituting it into the inequality, we obtain:
$$\boxed{\ \tau_{\rm life}\lesssim\left(\frac{3N\hbar\,R\,a^2}{16\,c^3\,|E_-|}\right)^{1/4}\ }$$
Substituting the critical value $|E_-|=\pi Rc^4/2G$, we get
$$\tau_{\rm life}\lesssim\left(\frac{3N}{8\pi}\right)^{1/4}\frac{\sqrt{\ell_P\,a}}{c}.$$
For $a=1$ mm and $N=1$ this gives $\tau\approx2.5\times10^{-28}$ s. To obtain 10 s one needs $N\sim10^{114}$. This is **ruled out**: with $N$ species of particles gravity loses applicability at the scale $\sqrt N\ell_P$ (the Dvali species bound [20]), and at $N\sim10^{114}$ this scale would be $10^{22}$ m. Even at the maximum allowed $N\sim10^{32}$ (a TeV cutoff) the lifetime is $\tau\sim10^{-20}$ s.

**Conclusion:** with a local free QFT the gap between the QI time and "seconds" is about 20 orders of magnitude. The scaling itself is nevertheless canonical: the lifetime grows with the thickness of the rim as $a^{1/2}$ and falls with the stored exotic energy as $|E|^{-1/4}$. The smeared null energy condition SNEC [9], $\langle T_{kk}\rangle\ge-B/(G\tau^2)$, is milder for a thin static rim, but it forbids **strongly gravitating** negative energy. We have an angle excess of $2\pi$, which is exactly such a case, so the rim operates at the boundary of the SNEC with $B\sim O(1)$ **[ESTIMATE]**.

Thus the seconds of lifetime must be provided **not** by local QI but by the mechanism of §3.

### 2.4. Casimir and squeezed vacuum as a "seed"
Neither the Casimir effect nor squeezed states provides the required depth. They do, however, have a property that matters for canon. Squeezed vacuum at each point oscillates between negative and positive energy density with period $\sim\lambda/c$, and its negative "half-periods" obey the same QI and the quantum interest [7]. If the gun periodically "pumps" the rim, then within the QI its stationary state is **pulsating**, not static. This gives a natural explanation for the flicker and the "boiling" of the portal's edge seen in the show **[ESTIMATE, interpretation]**. Visser, Kar, and Dadhich [11] showed that the integral of the energy condition violation can be made arbitrarily small by a choice of geometry. This does not remove the QI constraint on the thickness, but it supports the choice of "exotica only on a thin rim".

---

## 3. Self-Consistent Traversable Wormholes and ER=EPR

**ER=EPR** [12]: two maximally entangled black holes are connected by an Einstein–Rosen bridge; more generally, entanglement is geometrically realized as connectivity **[KNOWN, conjecture]**. The bridge itself is not traversable.

**Gao–Jafferis–Wall** [13]: a direct (double-trace) coupling of the two boundaries of an eternal BTZ black hole, $\delta H=g\,\mathcal O_L\mathcal O_R$, creates a **negative averaged NEC** in the bulk, and the bridge becomes traversable. This does not contradict the ANEC theorems, because the coupling is **nonlocal** from the bulk point of view. Physically this is quantum teleportation, and causality is not violated **[KNOWN]**.

**Maldacena–Stanford–Yang** [14] provide the key to the mass limit. If the coupling costs $g\lesssim N_{\rm bits}$ bits of classical information, then the number of particles that can be sent is $N_{\rm send}\lesssim g$. The total momentum of the signal is bounded by the condition $-p_+^{\rm tot}G_Ne^{t}\lesssim1$: a heavy signal suppresses the correlator $\langle\mathcal O_L\mathcal O_R\rangle$, and the bridge **does not open** **[KNOWN]**.

**Maldacena–Qi** [15]: a permanent coupling of two SYK systems or of two NAdS$_2$ regions gives an **eternal** traversable wormhole with an energy gap **[KNOWN]**.

**Maldacena–Milekhin–Popov** [16]: in 4D, a solution of the Einstein–Maxwell equations with massless charged fermions. A pair of nearly extremal magnetically charged black holes is connected by a long throat. The negative Casimir energy is supplied by $\sim q$ two-dimensional fermion modes along the field lines, that is, the "large $N$" arises here from the magnetic flux. Passage through the wormhole takes **longer** than outside, the construction itself is fragile, and objects with energy above the binding energy destroy it **[KNOWN]**. This is the best existing prototype of a portal: real 4D physics, but a microscopic scale and no shortcut.

**Experiment:** Jafferis et al. [17] implemented a "wormhole teleportation" protocol on 9 qubits (Nature, 2022). Its interpretation is disputed [17, comment], so this is a **demonstration of the protocol, not of the geometry**.

### 3.1. What follows for the gun
The canonical "coordinates" in the gun are naturally understood as an **entanglement resource with the destination point**. One half of the pairs is in the liquid, the other in an "anchor" on the target side. The GJW–MSY mechanism then immediately gives:
- **the portal's life equals the time during which the coupling $g$ is maintained** (switching off the coupling → closure within the scrambling time $t_*\sim\frac{\hbar}{2\pi k_BT}\ln S$);
- **the throughput**: $N_{\rm send}\lesssim N_{\rm EPR}$, that is, entanglement is consumed in transferring matter.

**[ASM-3]:** the liquid contains a macroscopic number of entangled degrees of freedom, $\gtrsim10^{29}$ per passenger (§8). **[ASM-4]:** the target side already contains the partners of these pairs. A possible source is vacuum entanglement, which exists between any regions but decays quickly with distance, or a previously deployed network of "anchors". This would explain, in canonical terms, why a gun without a "coordinates cartridge" is useless.

**An honest problem:** GJW requires a classical channel between the sides, and the signal through the bridge is no faster than this channel. For an instantaneous interworld jump the classical channel must run along a **shortcut through the bulk** (§5) **[ASM-5]**.

---

## 4. The Mass Limit

**Classical gravity does not constrain it.** The characteristic mass at which a passing body noticeably distorts the portal geometry is $M_*\sim Rc^2/2G\approx6.7\times10^{26}$ kg for $R=1$ m **[ESTIMATE]**. Consequently, the mass limit is quantum in nature.

**Mechanism A (negative-energy budget) [ESTIMATE].** On passage, a mass $m$ "disappears" at the entrance and "appears" at the exit: the entrance mouth acquires $+m$, the exit mouth $-m$, as in Visser's analysis of wormhole mouths. The potential perturbation at the rim, $\delta\Phi/c^2\sim Gm/(Rc^2)$, shifts the critical tension. Since the angle excess of $2\pi$ is topologically fixed, the rim must compensate the perturbation with additional exotica:
$$|\delta E_-|\sim\frac{Gm}{Rc^2}\,|E_-|=\frac{\pi}{2}\,mc^2 .$$
The result: **each kilogram of passing mass requires of the order of a kilogram of negative energy**. If the portal is launched with a reserve $\eta|E_-|$ above the critical value, then
$$m_{\max}\approx\frac{2}{\pi}\,\frac{\eta\,|E_-|}{c^2}.$$
When the reserve is exhausted, the tension drops below the threshold and the rim collapses.

**Mechanism B (informational) [KNOWN scaling [14]].**
$$N_{\rm send}\lesssim g\lesssim N_{\rm EPR},\qquad G_N\,E_{\rm signal}\,e^{2\pi t/\beta}\lesssim\ell_{\rm throat}\ \text{(in AdS units)}.$$
For a macroscopic object one must transmit at least its entropy: for a human of mass 70 kg, $S/k_B\ln2\sim3\times10^{28}$ bits. We obtain $N_{\rm EPR}\gtrsim10^{29}$ per passenger, and this is a **resource that the liquid expends**. When the entanglement runs out → the portal closes.

**In the model both mechanisms are combined:** the reserve $\eta$ exists as long as the nonlocal coupling is maintained (mechanism B), and each passage "eats" $\sim mc^2$ of negative energy from this reserve (mechanism A).

---

## 5. Interuniverse Transitions

1. **Everett branches** [Everett 1957]. The canonical "infinite realities" is closest to them. However, branches are not places in spacetime: there is neither geometry nor a wormhole between them. The linearity of quantum mechanics forbids interaction between branches. Polchinski showed that nonlinear quantum mechanics (Weinberg) inevitably yields either superluminal signalling or an "Everett phone" between branches [18]. **A transition between branches = nonlinear QM = a violation of causality. We reject this path** as too costly an extension.
2. **Level I/II multiverse.** Infinite space contains repeating regions (Tegmark). The landscape of bubbles (Bousso–Polchinski) gives regions with different constants. These are real remote places of **one** connected spacetime, and a wormhole between them is admissible. Nearly identical "other Earths" correspond to Level I, "worlds with different physics" to Level II.
3. **Brane world** (Randall–Sundrum [19]). Our universe is a 3-brane in a 5-dimensional AdS$_5$ bulk, and parallel branes are "other dimensions". Chung and Freese showed that in such models signals through the bulk can travel faster than along the brane [20′, see note]. MMP [16] explicitly mention RS2 as a possible continuation of their construction.

**Working hypothesis [ASM-5]:** Sanchez's "dimensions" are branes and/or remote regions of one bulk. The portal is (a) a classical coordinate channel running along a shortcut through the bulk, plus (b) a disk wormhole on the brane, opened by a nonlocal coupling. Everett branches remain an interpretive label, not a physical address.

---

## 6. Why the Edge Does Not Cut the Entrant but Cuts on Collapse

**Tidal safety** (Morris–Thorne [1]). The difference of accelerations across a body of length $L$ is $|\Delta a|\approx c^2|R_{\hat t\hat\xi\hat t\hat\xi}|L$. Requiring $\le g_\oplus$ at $L=2$ m gives
$$|R_{\hat t\hat\xi\hat t\hat\xi}|\le\frac{g_\oplus}{c^2L}\approx5\times10^{-17}\ \text{m}^{-2},$$
that is, the radius of curvature must be no smaller than $\sim10^8$ m **[KNOWN formula, ESTIMATE numbers]**. For the disk portal in the ideal limit the **curvature in the opening is zero** [2, 4], and a body of any size smaller than $R-a$ passes without tidal forces and without contact with the exotica.

**The rim is dangerous:** the density in the tube is $|\rho|\sim c^4/(4\pi Ga^2)\approx10^{49}$ J/m³ at $a=1$ mm, plus the conical singularity. The part of the body that lands on the rim is destroyed.

**Cutting on collapse:** an unsupported rim with positive or zero tension contracts at a speed of order $c$, in a time $\sim\pi R/2c\approx5$ ns. The singularity with an angle excess of $2\pi$, passing through the body, **carries its parts to different sheets**: the part on one side of the rim curve stays in the first universe, the part on the other side goes to the second. This is a topological rather than a mechanical cut, and it is perfectly smooth, which matches canon. In the show the collapse lasts a fraction of a second; it could be slowed by the inertia of the carrier liquid, this is **[ASM-6]**. *[reconciled at synthesis] ASM-6 is numerically wrong (the liquid is lighter than the rim by a factor of $\sim10^{29}$) and has been replaced by E2 (04 §4): the inertia belongs to the rim itself, $t_c\approx(R/c)\sqrt{2/\varepsilon}$, where $\varepsilon$ is the relative tension shortfall; the liquid sets only the rate of growth of $\varepsilon(t)$. 5 ns is the lower limit at $\varepsilon\to1$ (coupling dump).* A regularization of the rim in which the corrections to the curvature outside the tube decay fast enough and the opening remains tidally safe is **[ASM-7]**; its stability is not proven. For the linear stability of thin shells see Poisson–Visser; the problem itself is open in the general case.

**Transparency and two-sidedness.** Light is also "passing mass-energy", but its budget is negligible. The solar flux through a disk of area $\pi$ m² is $\sim4$ kW, that is, $\sim4\times10^{-14}$ kg/s of equivalent mass. Over 10 s this is $\sim4\times10^{-13}$ kg, about $10^{-16}$ of $m_{\max}\sim1$ t (reserve $\eta\sim10^{-24}$, see §8). Therefore one can look through the portal practically for free, and it is mass that is expensive. Entry is allowed in both directions because the gluing is symmetric. However, mechanism A implies a **mass-balance asymmetry**: the flow $A\to B$ and the reverse flow $B\to A$ partly compensate each other. This gives a testable prediction of the model: "counter-flow" traffic prolongs the life of the portal **[ESTIMATE]**.

**Stability is the main open problem.** For spherical thin shells Poisson and Visser reduced stability to the equation of state of the exotica, $\beta^2=\partial p/\partial\sigma$: stable configurations require "unphysical" $\beta^2$, negative or greater than one. For ring wormholes we found no analogous analysis in the literature. We believe that the rim is unstable to bending modes (like an ordinary string with a "minus" in the tension, for which the sign of the restoring force is reversed), and that this is precisely why the portal by itself lives a finite time even if the P4 coupling is maintained. This is **[ASM-7]**, and it is the first task for the numerical group: a linear perturbation analysis of the Gibbons–Volkov ring with a regularized tube.

**Formation of the disk** (an engineering analogy): a jet of liquid from a nozzle naturally rolls up into a **vortex ring**, with a "formation number" of about 4 according to Gharib et al. (JFM, 1998). The ring sets the rim, and the surface stretched across it is the disk. The analogue in field physics is the **vorton**, a loop of superconducting cosmic string stabilized by a current or by angular momentum. We need a vorton with **negative** tension **[ASM-1]**.

---

## 7. The Minimal Theoretical Model of the Sanchez Portal (MTM-SP)

**Postulates (geometry and dynamics):**
- **P1.** The portal is a vacuum ring wormhole of Gibbons–Volkov type: the two sheets $r\gtrless0$ of the metric of §1.3, glued along a disk of radius $R$ with preservation of orientation. The opening is flat, $T_{\mu\nu}=0$ and $R_{\mu\nu\rho\sigma}=0$ on the faces.
- **P2.** The rim is a ring of negative tension $T=-c^4/4G$ (angle excess $2\pi$), regularized by a tube of radius $a$, where $\ell_P\ll a\ll R$.
- **P3.** The threshold energy is $|E_-|=\pi Rc^4/2G$, with a reserve $\eta|E_-|$. ADM mass ≈ 0.
- **P4.** The source of the negative averaged NEC on the rim is a nonlocal coupling of GJW/MQ type, $\delta H=g\sum_i\mathcal O^{(1)}_i\mathcal O^{(2)}_i$, between the rims of the two mouths, realized by entangled "liquid ↔ anchor" pairs.

**Equations:**
$$\tau_{\rm life}\simeq\min\Big\lbrace \tau_{\rm couple},\ \underbrace{(3N_{\rm eff}\hbar Ra^2/16c^3|E_-|)^{1/4}}_{\text{QI, if the coupling is off}}\Big\rbrace ,\qquad \tau_{\rm couple}\simeq\frac{N_{\rm EPR}}{\dot N_{\rm EPR}},$$
$$m_{\max}\simeq\min\Big\lbrace \tfrac{2}{\pi}\eta|E_-|/c^2,\ m_{\rm bit}N_{\rm EPR}\Big\rbrace ,\qquad t_{\rm collapse}\sim\pi R/2c,\qquad |\Delta a|_{\rm tidal}=0\ \text{in the opening}.$$

**What we have added to known physics (explicitly):**
- **[ASM-1]** A macroscopic stable ring of negative tension of order $c^4/4G$ exists (a vorton with a "minus"). Known physics has no mechanism for this, as already noted in [2].
- **[ASM-2]** The achronal ANEC is violated [10]. In the model it is violated **only** by the nonlocal coupling P4, not by local QFT, which reduces ASM-2 to ASM-3/4.
- **[ASM-3]** A macroscopic ($\gtrsim10^{29}$ per passenger), long-lived, and transportable reservoir of entanglement in the liquid. *[reconciled at synthesis] A dose of 0.5 mL holds $\le10^{26}$ pairs, so the liquid carries only a local "key"; $\ge99$ % of the pairs are supplied by the anchor network (04, E1).*
- **[ASM-4]** The target point already contains the partners of the entangled pairs ("coordinates").
- **[ASM-5]** The classical coordinate channel runs along a shortcut through the bulk (an RS-like multiverse). Everett branches are not used.
- **[ASM-6]** The inertia of the carrier liquid slows the collapse from nanoseconds to tenths of a second. *[reconciled at synthesis] Rejected; replaced by E2 (rim inertia at small $\varepsilon$), see 00_summary.md.*
- **[ASM-7]** The regularization of the rim preserves the tidal safety of the opening and linear stability.

Everything else — general relativity, the quantum inequalities, GJW/MSY/MQ/MMP — is **known physics**.

---

## 8. Numerical Handles for Engineers

For a disk with $R=1$ m; for another radius, scale $\propto R$ where indicated.

| Quantity | Formula | Value |
|---|---|---|
| Linear density of the rim | $\lvert\mu\rvert=c^2/4G$ | $3.4\times10^{26}$ kg/m (independent of $R$) |
| Tension | $c^4/4G$ | $3.0\times10^{43}$ N |
| Negative energy of the rim | $\pi Rc^4/2G$ | $1.9\times10^{44}$ J $\approx1.1\,M_{\rm Jup}c^2\approx10^{-3}M_\odot c^2$ |
| Density in the tube, $a=1$ mm | $c^4/4\pi Ga^2$ | $\sim10^{49}$ J/m³ |
| Same, $a=1$ fm | | $\sim10^{73}$ J/m³ |
| For comparison: Casimir, gap 10 nm / 1 µm | $\pi^2\hbar c/720d^4$ | $4\times10^{4}$ / $4\times10^{-4}$ J/m³ |
| Gap "required / Casimir at 10 nm" | | $\sim10^{44}$ |
| QI time, $N=1$, $a=1$ mm / 1 cm | $(3/8\pi)^{1/4}\sqrt{\ell_Pa}/c$ | $2.5\times10^{-28}$ / $8\times10^{-28}$ s |
| QI time at $N_{\max}\sim10^{32}$ (Dvali bound) | $\times N^{1/4}$ | $\sim10^{-20}$ s |
| $N$ needed for 10 s (ruled out) | | $\sim10^{114}$ |
| Thickness of the exotic layer, MT throat of 1 m [6] | $(r_0/8f^4\ell_P)^{1/3}\ell_P$ | $\lesssim10^{-21}$ m |
| Collapse without support | $\pi R/2c$ | $\approx5$ ns |
| Tidal limit 1g over 2 m | $g/c^2L$ | $\lvert R\rvert\le5\times10^{-17}$ m⁻² (in the ideal opening — 0) |
| Classical perturbation mass | $Rc^2/2G$ | $7\times10^{26}$ kg (not limiting) |
| Cost of passing 100 kg | $(\pi/2)mc^2$ | $1.4\times10^{19}$ J $\approx3.4$ Gt TNT of negative energy from the reserve |
| Reserve above threshold for $m_{\max}=1$ t | $\eta=\pi m_{\max}c^2/2\lvert E_-\rvert$ | $\eta\approx7\times10^{-25}$: the portal sits so exactly on the threshold that a tonne "costs" only $10^{-24}$ of its energy, hence the fragility |
| Entanglement per passenger | $N_{\rm EPR}\gtrsim S/k_B\ln2$ | $\gtrsim3\times10^{28}$, we take $10^{29}$ |
| A liter of liquid | $3\times10^{25}$ molecules | requires $\sim10^{3}$–$10^{4}$ entangled qubits per molecule |
| "Effective temperature" for $t_*\approx1$ s at $\ln S\approx70$ | $T=\hbar\ln S/2\pi k_Bt_*$ | $\approx0.1$ nK (the order of ultracold atoms). *[reconciled at synthesis] This is not the temperature of the liquid (it is 0–40 °C) but the energy scale of the coupled rim–anchor channel, $\hbar\ln S/2\pi t_*$; it requires thermal decoupling of the channel from the environment* |

**Main conclusion for engineers:** local exotica with a Casimir and QI budget loses by 20–44 orders of magnitude. The model rests only on P4: the portal is "held" not by negative energy stored as fuel but by a **nonlocal coupling paid for with entanglement**. Therefore the gun's budget must be counted in qubits ($\sim10^{29}$ per person), not in joules.

---

## References

1. M. S. Morris, K. S. Thorne, *Wormholes in spacetime and their use for interstellar travel*, Am. J. Phys. **56**, 395 (1988).
2. M. Visser, *Traversable wormholes: Some simple examples*, Phys. Rev. D **39**, 3182 (1989); arXiv:0809.0907.
3. M. Visser, *Traversable wormholes from surgically modified Schwarzschild spacetimes*, Nucl. Phys. B **328**, 203 (1989); arXiv:0809.0927.
4. G. W. Gibbons, M. S. Volkov, *Ring wormholes via duality rotations*, Phys. Lett. B **760**, 324 (2016); arXiv:1606.04879.
5. G. W. Gibbons, M. S. Volkov, *Weyl metrics and wormholes*, JCAP **05** (2017) 039; arXiv:1701.05533.
6. L. H. Ford, T. A. Roman, *Quantum field theory constrains traversable wormhole geometries*, Phys. Rev. D **53**, 5496 (1996); arXiv:gr-qc/9510071. (Basic QI: Ford, Roman, Phys. Rev. D **51**, 4277 (1995); arXiv:gr-qc/9410043.)
7. L. H. Ford, T. A. Roman, *The quantum interest conjecture*, Phys. Rev. D **60**, 104018 (1999); arXiv:gr-qc/9901074.
8. E.-A. Kontou, K. Sanders, *Energy conditions in general relativity and quantum field theory*, Class. Quantum Grav. **37**, 193001 (2020); arXiv:2003.01815.
9. B. Freivogel, D. Krommydas, *The smeared null energy condition*, JHEP **12** (2018) 067; arXiv:1807.03808.
10. N. Graham, K. D. Olum, *Achronal averaged null energy condition*, Phys. Rev. D **76**, 064001 (2007); arXiv:0705.3193.
11. M. Visser, S. Kar, N. Dadhich, *Traversable wormholes with arbitrarily small energy condition violations*, Phys. Rev. Lett. **90**, 201102 (2003); arXiv:gr-qc/0301003.
12. J. Maldacena, L. Susskind, *Cool horizons for entangled black holes*, Fortsch. Phys. **61**, 781 (2013); arXiv:1306.0533.
13. P. Gao, D. L. Jafferis, A. C. Wall, *Traversable wormholes via a double trace deformation*, JHEP **12** (2017) 151; arXiv:1608.05687.
14. J. Maldacena, D. Stanford, Z. Yang, *Diving into traversable wormholes*, arXiv:1704.05333 (Fortsch. Phys., 2017).
15. J. Maldacena, X.-L. Qi, *Eternal traversable wormhole*, arXiv:1804.00491.
16. J. Maldacena, A. Milekhin, F. Popov, *Traversable wormholes in four dimensions*, arXiv:1807.04726.
17. D. Jafferis et al., *Traversable wormhole dynamics on a quantum processor*, Nature **612**, 51 (2022); critique: B. Kobrin, T. Schuster, N. Yao, arXiv:2302.07897.
18. J. Polchinski, *Weinberg's nonlinear quantum mechanics and the Einstein–Podolsky–Rosen paradox*, Phys. Rev. Lett. **66**, 397 (1991).
19. L. Randall, R. Sundrum, *An alternative to compactification*, Phys. Rev. Lett. **83**, 4690 (1999); arXiv:hep-th/9906064.
20. G. Dvali, *Black holes and large N species solution to the hierarchy problem*, arXiv:0706.2050.

*Additionally, without numbering in the main list:* D. J. H. Chung, K. Freese, *Can geodesics in extra dimensions solve the cosmological horizon problem?*, arXiv:hep-ph/9910235 (cited in the text as [20′]); E. Poisson, M. Visser, Phys. Rev. D **52**, 7318 (1995), arXiv:gr-qc/9506083; H. Everett, Rev. Mod. Phys. **29**, 454 (1957); M. Gharib, E. Rambod, K. Shariff, J. Fluid Mech. **360**, 121 (1998); P. K. F. Kuhfittig, arXiv:1202.0762.

*Verification status:* the existence and arXiv numbers of all sources were confirmed by search (October 2026). The journal citation details for [14]–[16] and [20] have not been verified, so only the arXiv numbers are given. Tegmark's number in §5 is deliberately not quoted.
