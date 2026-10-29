# 05. Momentum Conservation When Passing Through a Portal

Labels: **[canon]**, **[semi-canon]** (wiki and retellings), **[assumption]**, **[derived]** (follows from the assumptions), **[hypothesis]** (testable against episodes). The file `02_physics.md` is not in the directory, so the throat model is specified here minimally: a flat disk without matter, an exotic rim along the edge (Visser's flat-faced throat, 1989).

## 1. Lore: Scenes of the Two Modes

I did not obtain frames or transcripts of scenes with an explicit exit speed: Fandom and Wikipedia give retellings, and a search of Reddit and r/AskScienceFiction returned only discussions of the game Portal. Therefore the table is short rather than invented.

| Scene | Episode | Mode | Confidence |
|---|---|---|---|
| A general wiki statement: "Speed does not seem to be conserved through portals, so they can be used to break falls" (section Weaponization and Tactics) | episode not specified | damping | semi-canon, no references to frames |
| Rick's early experiment of teleporting a fruit, in a memory under the brainalyzer: wiki note "lack of conservation of momentum... at least when teleporting fruit" | the wiki page `Portal_Technology` does not name the episode. The brainalyzer memory belongs to S3E1 "The Rickshank Rickdemption", but I inferred the attribution myself | damping (not conservation) | low |
| Exit from a wrist-mounted time portal "from a small height" | "Gotron Jerrysis Rickvangelion" per the wiki | undetermined: a fall from a small height | low |
| Morty throws bottles of wine into a portal for accelerated time | "Mort Dinner Rick Andre" (S5E1), Wikipedia | undetermined: the exit speed is not described in the retelling | low |
| A fall with acceleration at the exit, a ship flying out at speed, throwing objects | **episodes not found** | conservation, according to the client | no confirmation |

Lore conclusion: the damping mode has indirect support in the wiki. The conservation mode so far rests only on the client's words. A frame-by-frame check is needed for the scenes "falling into a portal on the floor, emerging from a portal on a wall or ceiling" and "a ship flying through a portal". I do not confirm what I have not seen.

## 2. Physics: "speedy thing goes in, speedy thing comes out"

In the game Portal, GLaDOS says that momentum is conserved between portals. The key rule: **velocity relative to the portal normal**. If the entrance has outward normal $\mathbf n_1$ and the exit has $\mathbf n_2$, then a body that flew in against $\mathbf n_1$ flies out along $\mathbf n_2$, while the tangential component is conserved or rotated (angle $\alpha$):

$$\mathbf v_{out}=\mathcal R\,\mathbf v_{in},\qquad \mathcal R=\begin{pmatrix}R_\alpha&0\\0&-1\end{pmatrix}\ \text{in the bases } (\mathbf e_1,\mathbf e_2,\mathbf n).$$

This is a "reflection with rotation" in the throat frame. The minus on the normal component means: it entered against $\mathbf n_1$, it exited along $\mathbf n_2$. The magnitude of the speed is conserved [derived].

The forum dispute (for example, the thread "Portal physics" on Omnimaga) was about a moving portal. Two positions:
- **A, spatial reference**: the portal gives no momentum, so the body keeps its velocity in the *world* frame. Consequence: on a fast train the body is "torn apart" at the entrance.
- **B, the portal as a reference frame**: the body keeps its velocity *relative to the entrance*. Then an entrance moving at a stationary ball with speed $u$ ejects the ball from a stationary exit with speed $u$. The kinetic energy $\tfrac12mu^2$ arises "from nothing". A perpetual motion machine was obtained from a cycle of two moving portals.

**Resolution of the paradox** [derived]. Position B is consistent if the throat takes part in the balance. Passage through a moving portal is equivalent to an elastic reflection from a moving wall (Fermi acceleration): the relative velocity is conserved, and the wall's velocity is added. The energy and the momentum $\Delta\mathbf p=-m\Delta\mathbf V$ are given up by the entrance–exit pair, and whoever moved the portals paid for their kinetic energy. In the model of Frolov and Novikov the mass of a mouth changes as matter passes through. If the throat is rigidly glued in time, the relative motion of the mouths creates closed timelike curves (Morris, Thorne, Yurtsever 1988). For the series this is the boundary of the assumption: the portals either are at rest relative to each other, or the gluing renormalises time (see §3).

## 3. Gluing Two Charts and the Formula for the 4-Velocity

The shell $\Sigma$ glues the manifolds $\mathcal M_1$ and $\mathcal M_2$. The Israel junction conditions (1966):

1. continuity of the induced metric $h_{ab}$, that is, proper time and lengths on the shell coincide;
2. a jump in curvature: $[K_{ab}]-h_{ab}[K]=-8\pi G\,S_{ab}/c^4$ and the conservation law $D_bS^{ab}=-[T^{a}{}_{n}]$.

In a flat-faced throat on the disk $K_{ab}=0$ on both sides, therefore $S_{ab}=0$ and the disk does not interact with matter. All the curvature and the exotic matter sit on the rim (a conical deficit angle $\delta$, linear density $\mu=-c^2|\delta|/8\pi G$) [assumption, Visser 1989].

Each mouth has an orthonormal frame $E_i=(U_i,\mathbf e^{(i)}_1,\mathbf e^{(i)}_2,\mathbf n_i)$, where $U_i$ is the 4-velocity of the disk centre. The isometry of the shell maps $U_1\to U_2$ and acts on the tangent axes by a rotation, while the normal changes sign. A geodesic body crosses the shell without an impulsive force if $[T_{an}]=0$, so its components in the frame are continuous:

$$\boxed{u_2^\mu=E_2\,\mathcal R\,E_1^{-1}\,u_1^\nu}\qquad \mathcal R=\mathrm{diag}(1,R_\alpha,-1).$$

Let $E_i=\Lambda(\mathbf V_i)$ be boosts from the frame $G$ (the ground at each mouth) into the frame of the mouth. For small velocities:

$$\boxed{\mathbf v_{out}^{G_2}=\mathbf V_2+\mathcal R\,(\mathbf v_{in}^{G_1}-\mathbf V_1)}$$

With coinciding orientations $\mathbf v_{out}=\mathbf v_{in}+\Delta\mathbf V$, $\Delta\mathbf V=\mathbf V_2-\mathbf V_1$. This is precisely "the incoming velocity plus $\Delta v$ of the relative motion of the disks".

**Gravitational potentials.** For static mouths $N_i=1+\Phi_i/c^2$. By condition 1 the local velocities on the shell coincide. A body that has fallen from rest at infinity onto mouth 1 and climbs out of mouth 2 to infinity gets

$$\Delta\!\left(\tfrac12v_\infty^2\right)=\Phi_2-\Phi_1\quad(\Phi\le 0).$$

If $|\Phi_1|\gt |\Phi_2|$, the body flies out faster than it fell. The difference is taken from the mass-energy of the mouths.

**Two ways to "damp the fall"** [derived]:
- **(K) kinematic**: the exit slides away from the body: $\mathbf V_2=-\mathcal R(\mathbf v_{in}-\mathbf V_1)$, and $\mathbf v_{out}^{G}=0$. The momentum of the body has not vanished: it was taken up by the throat together with the motion $\mathbf V_2$. But the exit must run away from the body at the speed of the fall, whereas in the ground frame the exit is usually at rest, so (K) is suitable only for portals on moving carriers.
- **(A) absorbing**: a gluing with "losses". We introduce a parameter $\kappa\in[0,1]$ (§6): $\mathbf v_{out}^{G}=\mathbf V_2+\kappa\mathcal R(\mathbf v_{in}-\mathbf V_1)$. The momentum $\Delta\mathbf p=-m(1-\kappa)\mathcal R\,\mathbf v_{rel}$ is transferred to the rim.

## 4. Negative Mass: What Khamehchi 2017 Actually Does

The experiment (PRL 118, 155301): a $^{87}$Rb BEC in an optical trap with spin-orbit coupling (Raman lasers). The dispersion $E(k)$ acquires a region with $\partial^2E/\partial k^2\lt 0$, that is, $m^*=\hbar^2/(\partial^2E/\partial k^2)\lt 0$. An expanding cloud in this region decelerates and, instead of spreading at the edge, forms a shock wave: you push, and it accelerates backwards.

Honest limitations [derived]:
- $m^*$ is the effective mass of the *quasimomentum*. The true momentum is conserved, and the missing recoil is carried away by the laser field. For the rim the analogue is: the absorbed momentum goes into the *pumping* (the core of the gun, the source of the liquid), not into Rick.
- The range of the quasimomentum is limited: of order $\hbar k_r$ per atom ($\lambda\sim0.8$ μm, $\hbar k_r\approx8\cdot10^{-28}$ kg$\cdot$m/s, an atomic recoil of about 6 mm/s).

**Estimate for $m=70$ kg, $v=20$ m/s** (a fall from $h\approx20$ m): $p=mv=1400$ kg$\cdot$m/s, $E_k=14$ kJ (about 3.3 g of TNT).
- For a medium with a characteristic speed $v_c$, a rim mass $m_{rim}\gtrsim p/v_c$ is needed. At $v_c=20$ m/s we get 70 kg; at the speed of sound in a solid, 1 km/s, we get 1.4 kg; and for an Rb gas ($v_c\sim6$ mm/s) about 230 t: a rubidium BEC is unsuitable for this role.
- By Visser, in a flat-faced throat: $|M|\sim\frac{c^2}{8\pi G}\,|\delta|\,L$. At $\delta\sim\pi/2$ and rim perimeter $L=2\pi$ m we get $|M|\approx5\cdot10^{26}$ kg (of order 90 Earth masses) [assumption, order of magnitude]. The rim recoil is $\Delta v=p/|M|\approx3\cdot10^{-24}$ m/s. *[reconciled at synthesis] Adopted $|\delta|=2\pi$ (flat opening, 02): $|M|\approx2.1\cdot10^{27}$ kg, $\Delta v\approx7\cdot10^{-25}$ m/s, $p^2/2|M|\approx5\cdot10^{-22}$ J; the conclusions do not change.* Rick is not thrown back because the inertia of the rim is colossal. The negative sign gives only the direction: the rim receives $+p$ and is displaced *counter to* the motion of the body, and the energy of the rim decreases by $p^2/2|M|\sim10^{-21}$ J. The sum of the momenta adds up.

**A doubt about "the minus as a saviour"** [derived]: negative mass does *not reduce* the energy deficit. All 14 kJ must be dissipated elsewhere. For the "gun + Rick + rim with $M\lt 0$" assembly the total inertia decreases, and when positive and negative masses are coupled, a runaway motion arises (Bondi 1957). Therefore the rim must be tied to the shell, not to Rick's hands. This is an **assumption for the lore**.

**The "pile-up" problem** [derived]: if the body is decelerated instantly upon crossing the disk, the front part will stop while the rear is still flying at 20 m/s. Deceleration over the body length $d=0.5$ m gives $a=v^2/2d=400$ m/s$^2\approx41g$. For $10g$ one needs $d\approx2$ m. A soft landing requires an *increasing* coupling $\kappa(\tau)$ as the body passes through, or mode (K). Prediction: damping by mode (A) at high speeds causes injury.

## 5. Energetics

At $\kappa\lt 1$ the amount lost in the throat frame is
$$E_d=\tfrac12 m v_{rel}^2\,(1-\kappa^2),$$
and for full damping $E_d=14$ kJ. Where it goes [assumption]: heating of the portal liquid and the rim, then radiation. For 50 g of liquid with the heat capacity of water, $\Delta T\approx67$ K. *[reconciled at synthesis] 50 g is the whole cartridge, whereas what works is a dose of $\approx0.6$ g with an admissible thermal load $E_c\approx25$ J. Therefore $E_d$ leaves through the coupling channel to the anchor (E3), and only a fraction $f_{\rm loc}\sim5\cdot10^{-4}$ remains locally; the formula below is read as $\tau=\tau_0(1-f_{\rm loc}\sum E_d/E_c)$, see 00_summary.md.* Hence the **link with the lore**: the lifetime of the portal decreases as the accumulated thermal load grows, $\tau=\tau_0(1-\sum E_d/E_c)$, where $E_c$ is the destruction threshold [hypothesis]. The damping mode uses up the portal and the liquid faster. In the conservation mode $E_d=0$, and the portal lives longer, but the fall is not damped.

## 6. Gun Parameter: the "Frame-Coupling Mode"

**$\kappa\in[0,1]$** is the stiffness parameter of the frame gluing of the frames $E_1,E_2$:
- $\kappa=1$: the frame is transported without losses, $\mathbf v_{out}=\mathbf V_2+\mathcal R(\mathbf v_{in}-\mathbf V_1)$ — conservation. Combined with $\mathbf V_1=\mathbf V_2$ this is the "went in fast, came out fast" mode.
- $\kappa=0$: the exit "forgets" the velocity of the entrance. The body appears at rest in the frame of the exit — damping.
- $0\lt \kappa\lt 1$ — partial.
- The exit velocity $\mathbf V_2$ (the exit on a ship or a platform) gives mode (K) at $\kappa=1$.
- The switch is set at the moment the pair is created and is stored in the pair, because the shell is a property of the gluing.

Predictions for the episodes [hypothesis]:
1. **The mode belongs to the pair, not to the object.** Through a single portal both a ball and a person behave in the same way ($\kappa$ is common). Counterexample: one pair, different responses for living and nonliving objects.
2. **An exit fixed to a moving carrier (a ship, a car, a train) adds the carrier's velocity at $\kappa=1$.** An object falling into such a portal flies out with $\Delta\mathbf V$ and an orientation along $\mathbf n_2$: into a horizontal portal on a wall the body falls with a horizontal velocity equal to the speed of the fall.
3. **Damping shortens the life of the portal.** After a heavy fast body passes through a damping portal, the portal closes earlier: $\Delta\tau/\tau_0\approx m v^2(1-\kappa^2)/2E_c$. Test: compare the closing time of portals after a damping landing and without it.

## References

- Khamehchi M.A. et al., Negative-Mass Hydrodynamics in a Spin-Orbit-Coupled Bose-Einstein Condensate, *Phys. Rev. Lett.* **118**, 155301 (2017), arXiv:1612.04055.
- Israel W., Singular hypersurfaces and thin shells in general relativity, *Nuovo Cimento B* **44**, 1 (1966); erratum **48**, 463 (1967).
- Visser M., *Lorentzian Wormholes: From Einstein to Hawking*, AIP Press (1995).
- Visser M., Traversable wormholes from surgically modified Schwarzschild spacetimes, *Nucl. Phys. B* **328**, 203 (1989).
- Morris M.S., Thorne K.S., Yurtsever U., Wormholes, time machines, and the weak energy condition, *Phys. Rev. Lett.* **61**, 1446 (1988).
- Frolov V.P., Novikov I.D., Physical effects in wormholes and time machines, *Phys. Rev. D* **42**, 1057 (1990).
- Bondi H., Negative mass in general relativity, *Rev. Mod. Phys.* **29**, 423 (1957).
- Valve, *Portal* (2007): GLaDOS's line about momentum conservation; discussions: Omnimaga, "Portal physics"; Synopsys (formerly Ansys) developer blog, "Portal Paradox" (parts 3 and 4); Codidact Scientific Speculation, "Are portals possible?".
- Rick and Morty Wiki: `Portal_Gun`, `Portal_Technology`; Wikipedia: "Mort Dinner Rick Andre"; summary `01_lore.md`.
- The WSU Forbes Group site and sci.news on the Khamehchi result (popular retellings).

**Not verified:** I did not read the exact numbers in Khamehchi 2017 (the number of atoms, $\lambda$) in the original; the order of magnitude $\hbar k_r$ is taken. The references to Frolov–Novikov, Bondi, MTY and the Synopsys/Codidact pages are given from search and memory; I did not check the details of the conclusions in them.
