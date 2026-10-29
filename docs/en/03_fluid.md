# 03. The Portal Fluid: A Materials-Science Rationale

*A section of the "Scientific Basis of the Portal" team effort. Author: condensed matter physics / materials science.*
*Labels: **[FACT]** — a published result; **[ESTIMATE]** — an order-of-magnitude calculation; **[ASSUMPTION Dn]** — a minimal extension of known physics, explicitly unconfirmed.*

## 0. Canon and the Working Model

The file `01_lore.md` did not exist, so the canon was taken from the fan wiki (Rick and Morty Wiki, article Portal Gun). It states:
- the fluid is stored in a flask on the body of the gun and works as fuel;
- it is extremely toxic, and in large quantities it dissolves solids;
- if a bootleg fluid is mixed incorrectly, the portal collapses on the user;
- portals are opaque, open in the air at any angle, and come in different sizes;
- the time until collapse varies, presumably set by the user;
- a closing portal **cuts** objects, and **gases do not pass through the portal**.

I found no canonical indications of the fluid changing color (yellow, red), so §3 offers this only as a hypothesis.

**The main idea of the section.** The disk does not need to consist entirely of exotic matter. General relativity has a solution that is morphologically identical to the portal from the cartoon. Visser (1989) constructed a wormhole with flat faces: the stress–energy tensor on the faces is zero, and all the exotica is concentrated on the **edges** in the form of a classical string with negative tension [FACT, reference 2]. The limiting case is a "portal": a flat throat framed by **a single loop** of exotic cosmic string (Cramer et al. 1995 [3]; "portal wormhole", Feng 2021 [4]). Space is flat everywhere except at the string itself. The traveler passes through the flat region and does not touch the exotica (Visser 1989 [2]).

Hence the materials scientist's task: **within a fraction of a second the fluid must curl into a thin ring (the rim) and carry the exotic state on it**. The visible green "disk" is a thin luminous film stretched across the ring, like a soap film on a bubble wand. Ford and Roman (1996) [5] independently concluded that in a macroscopic wormhole the negative energy must be gathered in a band many orders of magnitude thinner than the throat. This is the "sharp rim".

## 1. Self-Assembly into a Disk

### 1.1 Real prototypes

| System | What it provides | Reference |
|---|---|---|
| Bicelles (long-chain + short-chain lipid) | A flat bilayer **disk** with a rim of different composition. In a magnetic field the disks align | Sanders & Prosser, *Structure* 6, 1227 (1998) |
| Lamellar/smectic phases | Flat layers with long-range order | — |
| Ferromagnetic nematic (barium hexaferrite platelets in an LC) | Alignment by a weak field, spontaneous magnetization of the liquid | Mertelj et al. 2013 [11] |
| Bubbles and pores in membranes | An edge with line tension γ; a pore closes in a time ~ηR/γ | Sandre et al. 1999 [15] |
| Savart sheets, "liquid marbles", EHD (Taylor cone) | Flat sheets with a thickened rim; droplets in an armoring shell; field-controlled spraying | Clanet & Villermaux, JFM 2002; Aussillous & Quéré, Nature 2001 |
| **Vortex ring** from a pulsed jet | A compact toroidal vortex. The formation time is universal: L/D ≈ 4 | Gharib, Rambod, Shariff 1998 [12] |

### 1.2 Proposed mechanism (three-stage)

1. **The shot = a vortex gun.** The gun ejects not a jet but a pulsed "puff", and it rolls up by itself into a vortex ring [FACT, 12]. The plane of the ring is perpendicular to the shot vector, so **the orientation of the disk is set by the momentum of the shot**. As the ring approaches a wall, it expands in radius (the known effect of vortex–wall interaction). Hence a portal on a wall, turned toward the shooter.
2. **The vortex core = the rim.** The superfluid component of the fluid (§2) captures the classical vorticity and quantizes it into a **quantized vortex ring** with a core of nanometer or micron scale. This is the "sharp edge". The comparison "vortex in a superfluid ↔ cosmic string" is a standard analogy (Zurek, *Nature* 317, 505, 1985). The magnetic platelets of the ferro-LC gather in the core (there is a pressure gradient there) and stabilize it. In addition, the orientation may be fixed by a field pulse from the gun [11].
3. **The film.** The amphiphilic component stretches a bicelle-like bilayer membrane across the ring. The short-chain "edge" agent goes to the rim, as in bicelles. The film is opaque because it luminesces (§3). It also explains the canon that "gases do not pass": a thin film is gas-tight, while a solid body passes through it and the film self-heals behind it [13].

**[ASSUMPTION D1]** A classical vortex ring can be converted within ≲10 ms into a quantized ring of macroscopic radius. The real analogue is quantized vortices in BEC and He-II, but there they are microns and millimeters, not meters.

**Why a disk, and not a sphere or a droplet.** Surface tension by itself pulls a cloud into a sphere, as in ordinary droplet coalescence. The flat shape is provided by two factors: (a) a vortex ring has a distinguished plane, set by the direction of the momentum; (b) a bicelle-like membrane has an edge line tension. If the edge is "softened" by a short-chain agent, a flat disk turns out to be energetically more favorable than a closed bubble as long as its radius is smaller than a critical one. This is the well-known "disk ↔ vesicle" transition in lipid systems. The sharpness of the rim is explained by the separation of scales: film thickness ~0.1–1 µm, vortex core ~1–10 µm, radius ~1 m. To the eye the boundary looks perfectly sharp.

**An alternative orientation channel: electrohydrodynamics.** If the nozzle charges the aerosol (electrospray through a Taylor cone), the charged droplets line up in the field between the nozzle and the target. This gives a second, controllable way to set the orientation and size: the cone opening and the voltage set the droplet distribution. In the gun it is logical to use both channels: the mechanical impulse is responsible for the coarse geometry, the field for the fine adjustment.

**Why the portal is opaque.** The film contains an excited dye and strongly scattering magnetic platelets, so the optical thickness at h ~ 1 µm is large. This agrees with canon: "the far edge is not visible until you go in".

**Stability of the radius.** The negative tension of the rim tends to expand the ring, while the positive surface tension of the film tends to contract it. The radius R* is set by their balance. **[ASSUMPTION D2]**: the effective coupling coefficient of the exotic sector to the film is tuned so that a balance is possible, although the "bare" quantities differ by tens of orders of magnitude (§2).

## 2. The Carrier of Exotic Energy

### 2.1 How much is needed

A Visser portal requires a linear mass density on the rim of the order of |μ| ~ c²/(8G)…c²/(4G) ≈ 2·10²⁶–3·10²⁶ kg/m [ESTIMATE from 2]. The quantity is **independent of the radius**, because it is set by an angle, not by a size. For a portal 2 m in diameter (rim length ≈ 6 m) this is ≈ −10²⁷ kg, that is, about −170 Earth masses. *[reconciled at synthesis] An angle excess of 2π is adopted, i.e. |μ| = c²/4G: ≈ −2.1·10²⁷ kg (≈350 Earth masses, ≈1.1 M_Jup), |E₋| ≈ 1.9·10⁴⁴ J.* For comparison: the Casimir energy density between ideal plates, −π²ħc/(720a⁴), at a = 10 nm gives ≈ −4·10⁴ J/m³, or ≈ −5·10⁻¹³ kg/m³ [ESTIMATE]. For a rim of cross-section ~1 µm² this is −5·10⁻²⁵ kg/m against the required −2·10²⁶ kg/m: a gap of about 50 orders of magnitude. Moreover, the quantum inequalities limit how much negative energy can be accumulated and for how long it can be held (review by Kontou & Sanders 2020 [6]). None of the candidates below **closes the gap in magnitude**. Therefore we introduce:

**[ASSUMPTION D3, key]** There exists a hidden sector (a field φ) whose topological defects are lines with negative tension ("exotic strings"). Visser states explicitly that a natural mechanism for negative tension is unknown [2]; Cramer et al. discuss relic loops of this type [3]. The fluid does **not produce** this energy "from scratch". It serves as a **template condensate**: its quantized vortex is topologically bound to the φ defect and sets its shape and location (as a vortex in a superconductor sets the location of magnetic flux). The energy for the "nucleation" of the loop is supplied by the core of the gun; this is outside the scope of the section. The condensed medium solves three problems: geometry, orientation, confinement. *[reconciled at synthesis] In the unified model (00_summary.md) the negative tension is provided by a nonlocal coupling (02, P4), and D3 is downgraded to a fallback. The fluid remains a template (the vortex sets where the coupled modes sit), a film, and a local "key".*

A fallback without D3: traversability through the quantum coupling of entangled systems (Gao–Jafferis–Wall, JHEP 2017, 151; Maldacena–Milekhin–Popov, arXiv:1807.04726). Then the fluid is needed to preserve the entanglement on the rim (see §4).

### 2.2 Candidates

| Candidate mechanism | What it explains | What it does not explain | Real prototype/reference |
|---|---|---|---|
| Squeezed vacuum in a nonlinear medium | Locally negative energy density in a narrow band, which is inevitably accompanied by a positive "quantum payback"; grows naturally in a thin rim-waveguide | The magnitude (tens of orders smaller); the lifetime is limited by decoherence | 15 dB squeezing: Vahlbruch et al., PRL 117, 110801 (2016); QI analysis: Maclay & Davis, arXiv:1806.01269 |
| Casimir nanostructures, repulsion in a medium | Stability of the suspension: nanoparticles do not stick together when compressed into the vortex core; "levitation" of components | Does not give an NEC violation of the required scale | Munday, Capasso, Parsegian 2009 [7]; Leonhardt & Philbin, NJP 9, 254 (2007) |
| BEC / superfluid component | **A quantized vortex = a sharp thin rim**; a string analogue; coherence | By itself does not violate the energy conditions | Zurek 1985; BEC analogues [8] |
| Analogue gravity (acoustic horizon) | Provides a "horizon" and radiation on the rim; an effective metric; a language for describing the throat | An effective metric is not a real spacetime geometry | Unruh, PRL 46, 1351 (1981); BLV [8]; Steinhauer 2016 [10] |
| Negative effective mass in an SO-coupled BEC | The rim "reacts the other way", i.e. expands under a contracting force; a mechanism of self-stabilization of the radius (D2) | The mass is effective, not gravitationally negative | Khamehchi et al. 2017 [9] |
| Polariton condensate at room temperature | A coherent phase **without cryogenics**, pumped by light; it glows | Polariton lifetimes are picoseconds and nanoseconds, continuous pumping is required | Plumhof et al. 2014 [14]; acoustic horizon: Nguyen et al., PRL 114, 036402 (2015) |
| Hidden sector with exotic strings (D3) | The required \|μ\|, the "Visser portal" | Not observed | Visser 1989 [2]; Cramer et al. [3]; Feng [4] |

**Analysis by candidate.** Squeezed vacuum is the only candidate from laboratory practice that *literally* gives a negative energy density of the electromagnetic field in a bounded region of space and time. The quantum inequalities require it to be compensated by positive energy nearby. In the portal geometry this is even convenient: the positive "payback" goes into the film and into the glow, while the negative part stays in the vortex core. The Casimir energy is static and small. Its role is structural: Casimir–Lifshitz repulsion in a suitably chosen triple of media (solid–liquid–solid) [7] prevents the aggregation of nanoparticles when they are strongly compressed by the vortex core. Analogue gravity gives us not exotica but a **language**: in the superfluid component around the core an acoustic metric with an effective horizon arises [8, 10]. This makes it possible to test the stability of the rim by laboratory methods long before D3 is obtained. Negative effective mass [9] pertains to dispersion, not to gravity, but it gives a useful "reverse" response that stabilizes the radius.

**Conclusion.** A "disk with exotica on the rim" is obtained naturally from a combination of **a superfluid/polariton component (vortex-rim) + squeezed vacuum in the core + D3**. The Casimir particles are responsible for colloidal stability, the negative effective mass for self-regulation of the radius.

## 3. The Glow and the Green Color

Cherenkov radiation in a medium is blue and requires relativistic particles, so it is excluded. The Hawking or Unruh temperature of a throat of meter size is negligible: of order ħc/(4πk_B R) ≈ 2·10⁻⁴ K·(1 m/R) [ESTIMATE], that is, fractions of a millikelvin, and it does not produce visible light.

The proposed model: **the pumping channel glows**. The fluid is two-component, like a chemical light stick (glow stick). A peroxyoxalate reaction excites a dye emitter, for example 9,10-bis(phenylethynyl)anthracene, the standard emitter of green light sticks [FACT]. The excitation energy is pumped into an organic polariton condensate [14], and whatever does not get into the condensate is radiated away as green luminescence of the film and of the cloud. This also yields two canonical facts: **toxicity** (peroxides, oxalate esters, organic solvents) and the **lethality of incorrect mixing**: at wrong stoichiometry the pumping falls below the condensation threshold, and the rim loses coherence at the moment of passage.

**The color-change hypothesis.** In polariton condensates the emission line shifts to the blue with increasing density because of interaction [FACT, a general effect]. Then the shift "green → yellow → red" reads as a **depletion indicator**: the density of the condensate falls, the line moves to the red. This is a physically meaningful "fuel-gauge needle".

Why green specifically, and not another color. First, around 510–555 nm is the maximum sensitivity of the eye, so a green marker is the most visible at minimal pumping power, which saves fuel. Second, organic emitters based on anthracene have a high quantum yield precisely in the blue-green region. Third, a green line is convenient as a reference for the optical quality sensor in the gun (§6a). The glow of the cloud before self-assembly is the chemiluminescence of the not-yet-condensed fraction. After assembly the glow concentrates in the film and in the rim, and the rim looks brighter than the faces because of the larger optical thickness of the core. This gives the bright edge characteristic of canon.

## 4. Consumption and Collapse

The fluid is consumed through three channels:
1. **Burn-up of the pumping.** The chemiluminescent fuel is irreversibly consumed to keep the condensate above threshold.
2. **Decoherence.** The squeezed state and the entanglement on the rim are destroyed by losses: absorption, scattering, thermal phonons.
3. **"Quantum interest".** According to the Ford–Roman conjecture (PRD 60, 104018, 1999), a negative energy "credit" must be repaid with a surplus, and the longer it is held, the more expensive it is.

Collapse: when the exotic tension of the rim falls below the threshold (D2), the film contracts the ring, like a closing pore [15]. The ring, converging, **cuts** whatever it crosses. This matches canon: the portal cuts objects when it closes.

Lifetime model [ESTIMATE]:
τ ≈ (V_dose · ε_chem · η) / P_loss(T),
where ε_chem ~ 10⁶–10⁷ J/m³ is the energy reserve of the chemiluminescent mixture, η is the efficiency of transfer into the condensate, and P_loss is the loss power. The reaction rate obeys the Arrhenius law: light sticks in the cold glow more dimly but longer [FACT]. Therefore **in the heat the portal lives shorter**, and at T below ~0 °C the pumping may fail to reach the threshold and the portal will not open. The "user-set lifetime" of the canon is the choice of the dose V_dose at the shot.

A numerical example [ESTIMATE]: V_dose = 0.5 mL, ε_chem = 5·10⁶ J/m³ → 2.5 J of chemical energy. With η ~ 1 % and losses P_loss ~ 10 mW (per 1 m of rim: scattering plus radiation from the film) one obtains τ ≈ 2.5 s, which agrees with the "seconds" of the phenomenology. A doubling of the reaction rate per +10 °C (van 't Hoff rule) shortens τ by about half. For "long" portals (minutes) either a larger dose or external feeding from the gun is needed. The canon on the stationary portals of the Citadel points precisely to reactors.

Why **an incorrect mixture is lethal**: if the pumping falls below the threshold in the middle of a passage, the rim collapses in a time ~R/v_T (§ "Parameters"), that is, in tenths of a second. This is less than the time it takes a person to pass (~0.5 s). Hence the manufacturing requirement: the stoichiometry tolerance must be better than a few percent.

## 5. Production: A Roadmap

| Stage | What we do | Technology status |
|---|---|---|
| 1 | Solvent + amphiphiles (a bicelle-forming lipid pair) | Exists |
| 2 | Magnetic nanoplatelets (BaHF) dispersed in an LC | Exists [11] |
| 3 | Two-component peroxyoxalate pumping + a green emitter | Exists (industrially) |
| 4 | Nanoshell microresonators with an organic polariton condensate in **suspension** | A room-temperature condensate exists only in films [14]; a suspension is an R&D task |
| 5 | Nanoparticles with Casimir repulsion (metamaterial response) | Repulsion has been measured [7]; mass synthesis is R&D |
| 6 | Generation of squeezed vacuum in the nonlinear vortex core | Squeezing exists in optics (15 dB); in a liquid it does not |
| 7 | Coupling to the hidden sector (D3) | Requires new physics |

The two-component nature (stage 3) explains why mixing is the critical operation: the components are stored separately and mixed in the nozzle of the gun, otherwise the pumping would "burn out" in the flask.

## 6. Safety of Passage

- **The body is not cut**, because there is no exotica in the disk: the faces of a Visser portal are flat space [2]. Only the **rim** can cut, and only when it is moving (collapsing). Hence the engineering rule: "do not stand in the ring at depletion", that is, when the color is red.
- **The body is not contaminated.** A film of thickness h ~ 0.1–1 µm on a disk of 3 m² amounts to only ~0.3–3 mL. A solid body passes through a soap film, and the film self-heals. The regime is set by the Weber number We = ρv²D/σ, with thresholds at We ≈ 3200 and 6100 [13]. For a human at v ≈ 2 m/s We ~ 5·10⁴, which is the regime of an elongated cavity with pinch-off. The residual layer is nanoliters per cm², and it can be removed by a fluorinated (low-energy, non-wetting) formulation of the amphiphiles. **[ASSUMPTION D4]**: the film does not wet skin and clothing.
- **Why gases do not pass while bodies do.** The film works as a selective barrier. The air pressure difference across it is too small to rupture it, so gas does not flow. A solid body passes through it with We ≫ 1 [13]. A side effect useful to engineers: the portal works as an airlock and does not equalize pressure between the worlds. A film with surface tension holds a difference of ~2σ/R, not an atmospheric one, so with a large pressure difference a reinforced film is needed — **[ASSUMPTION D6]**. *[reconciled at synthesis] For R = 1 m this is ~0.1 Pa. To hold 1 atm, a film of 1 µm thickness would have to withstand ~5·10¹⁰ Pa (graphene level), so D6 is rated as strong.*
- **Recycling.** When a body passes through, the film contracts toward the rim and stretches again. This is exactly why one dose withstands many passages while the pumping is alive.
- The canonical fact "in large quantities it dissolves matter" refers to the bulk liquid, not to the film. At the standard dose the exposure to the substance is practically nil.

## 6a. Emergency Modes (Cross-Check with Canon)

- **Substitution of the fluid by a foreign substance** (in canon Morty tops up with soda). Sugars and acids quench the peroxyoxalate reaction, while surfactants and ions destroy the bicellar phase. A sensor in the gun compares the conductivity and the optical spectrum of the flask with a reference. The canonical "foreign liquid" warning looks like an ordinary quality-control check.
- **The mixture with lemonade "portals everything it touches".** Interpretation: the admixture removes the self-assembly threshold (lowers the critical concentration). Then every drop that touches a surface launches a miniature rim, and instead of one controlled ring thousands of uncontrolled ones form.
- **Huge quantities → a "weak black hole".** If many exotic loops with different signs of tension are put together (the convex and concave edges in Visser [2]), the net mass of the system may become positive and large. The result is a collapse, not a wormhole. Qualitatively this agrees with canon.
- **A small portal that has entered a large one "implodes" the object.** The intersection of two rims is topologically forbidden without a break of one of them. By the result of Feng [4], bringing the mouths of a portal together leads to a curvature singularity. Operating rule: never open a portal through a portal.

## 7. Testable Predictions and a Laboratory Program

The model is useful if its parts can be tested separately, without waiting for D3:

1. **Vortex gun + bicellar film.** A vortex-ring generator (piston and nozzle) on a DMPC/DHPC mixture with a fluorescent marker. Prediction: at L/D ≈ 4 the ring carries a stretched film, the plane of the ring is perpendicular to the shot axis, and on approaching a wall the radius grows. This can be tested today on a benchtop setup with a high-speed camera.
2. **Magnetic stabilization of the core.** We add BaHF platelets [11]. Prediction: the vortex core is enriched in platelets, the lifetime of the ring increases, and the orientation can be adjusted by a weak (mT) field.
3. **A quantized rim.** In a cold-atom BEC or in a polariton liquid we create a vortex ring and measure phonon correlations on both sides of the acoustic horizon, following the method of Steinhauer [10]. This tests that the rim carries a "horizon" structure.
4. **Squeezing in the core.** We measure the quadrature noise of the radiation emerging from the core of the ring in a polariton system. Prediction: squeezing below the vacuum level is localized on the rim, not on the film.
5. **A depletion indicator.** Prediction of §3: the shift of the emission line is monotonically related to the remaining lifetime. We measure the spectrum as a function of time.

**What to hand over to other sections.** To the gravity team (GR): the rim is a Visser–Cramer loop, |μ| ≈ c²/4G, the faces are flat. An estimate is needed of the tidal forces near the rim and of the minimal safe clearance. To the quantum team: which of the scenarios (D3 or GJW/MMP entanglement) requires less intervention in known physics, and what the pumping power should be. To the gun engineers: a 20 m/s impulse through a 2 cm nozzle, a dose of 0.2–1 mL, separate storage of the two components with mixing in the nozzle, electrodes for EHD fine adjustment.

## Parameters for Engineers (Guidelines)

| Parameter | Value | Basis |
|---|---|---|
| Fluid density | 1.1–1.3 g/cm³ | Organics + 1–5 vol.% inorganic platelets [ESTIMATE] |
| Surface tension | 0.02–0.04 N/m | Amphiphilic system |
| Cartridge volume | 20–50 mL | Size of the flask on the gun [canon, ESTIMATE] |
| Dose per portal Ø 2 m | 0.2–1 mL (film 0.3–3 mL taking into account recycling from the rim) | §6 |
| Portals per cartridge | ~30–150; *[reconciled at synthesis] baseline: a 50 mL cartridge, ~100 short ones (0.5 mL, ~3 s) or ~25 long ones (2 mL, ~10 s)* | Ratio of the two rows above |
| Vortex ring formation | ~4 ms (2 cm nozzle, 20 m/s, L/D ≈ 4) | [12] |
| Film stretching (Taylor–Culick speed √(2σ/ρh)) | ~8 m/s at h = 1 µm → ~0.1 s per 1 m | [ESTIMATE] |
| Total self-assembly | 0.05–0.3 s | "Fractions of a second" ✓ |
| Coherence time without pumping | ps–ns (polaritons); squeezing — up to the resonator τ | [14] |
| Required time with pumping | 1–10 s | A Q-factor at the level of superconducting 3D resonators is needed (photon lifetime up to 2 s — Romanenko et al., *Phys. Rev. Applied* 13, 034032, 2020) — **[ASSUMPTION D5]** |
| Temperature window | ~0–40 °C | Arrhenius for the pumping, §4 |
| Linear exotic density of the rim | ~ −2·10²⁶ kg/m | [2], only via D3 |

**Estimate of the decoherence time of the squeezed state in the rim [ESTIMATE].** For squeezing at a level of s dB with a loss fraction L the noise level grows as V = (1−L)·10^(−s/10) + L. To keep at least 3 dB out of the initial 15 dB, the losses must be L ≲ 0.5. With an absorption coefficient α of the medium the lifetime is τ_dec ≈ L/(α·c/n). For an organic medium with α ~ 1 cm⁻¹ one obtains τ_dec ~ 10⁻¹¹ s, that is, **without pumping the rim lives picoseconds**. Hence the central requirement: continuous regeneration from chemical pumping (§4), and for an autonomous mode a reduction of α in the core by ~10 orders of magnitude, to the level of superconducting resonators (D5).

## Summary of Assumptions

| No. | Assumption | How radical |
|---|---|---|
| D1 | A classical vortex ring rapidly quantizes into a macroscopic ring | Moderate (scale extrapolation) |
| D2 | A balance of the tensions of the rim and the film exists | Moderate |
| D3 | A hidden sector with strings of negative tension bound to the vortex | **New physics**; downgraded to a fallback at synthesis [reconciled at synthesis] |
| D4 | The film does not wet biological surfaces | Weak (an engineering problem) |
| D5 | Core Q-factor at the level of superconducting resonators | Strong |
| D6 | A reinforced film holds an atmospheric pressure difference | Moderate |

## References

1. Morris M. S., Thorne K. S. Wormholes in spacetime and their use for interstellar travel. *Am. J. Phys.* 56, 395 (1988).
2. Visser M. Traversable wormholes: Some simple examples. *Phys. Rev. D* 39, 3182 (1989); arXiv:0809.0907.
3. Cramer J. G., Forward R. L., Morris M. S., Visser M., Benford G., Landis G. A. Natural wormholes as gravitational lenses. *Phys. Rev. D* 51, 3117 (1995); arXiv:astro-ph/9409051.
4. Feng J. C. Self-collision of a portal wormhole. arXiv:2105.03433 (2021).
5. Ford L. H., Roman T. A. Quantum field theory constrains traversable wormhole geometries. *Phys. Rev. D* 53, 5496 (1996); arXiv:gr-qc/9510071.
6. Kontou E.-A., Sanders K. Energy conditions in general relativity and quantum field theory. *Class. Quantum Grav.* 37, 193001 (2020); arXiv:2003.01815.
7. Munday J. N., Capasso F., Parsegian V. A. Measured long-range repulsive Casimir–Lifshitz forces. *Nature* 457, 170 (2009).
8. Barceló C., Liberati S., Visser M. Analogue gravity. *Living Rev. Relativ.* 8, 12 (2005); upd. 14, 3 (2011); arXiv:gr-qc/0505065.
9. Khamehchi M. A. et al. Negative-mass hydrodynamics in a spin-orbit–coupled Bose–Einstein condensate. *Phys. Rev. Lett.* 118, 155301 (2017).
10. Steinhauer J. Observation of quantum Hawking radiation and its entanglement in an analogue black hole. *Nature Phys.* 12, 959 (2016).
11. Mertelj A., Lisjak D., Drofenik M., Čopič M. Ferromagnetism in suspensions of magnetic platelets in liquid crystal. *Nature* 504, 237 (2013).
12. Gharib M., Rambod E., Shariff K. A universal time scale for vortex ring formation. *J. Fluid Mech.* 360, 121 (1998).
13. Killian T., Huey J., Bryson J., Truscott T. Self healing soap films. arXiv:1210.3797 (2012).
14. Plumhof J. D., Stöferle T., Mai L., Scherf U., Mahrt R. F. Room-temperature Bose–Einstein condensation of cavity exciton–polaritons in a polymer. *Nature Mater.* 13, 247 (2014).
15. Sandre O., Moreaux L., Brochard-Wyart F. Dynamics of transient pores in stretched vesicles. *PNAS* 96, 10591 (1999).

*Source of the canon: Rick and Morty Wiki, "Portal Gun" (rickandmorty.fandom.com/wiki/Portal_Gun).*
