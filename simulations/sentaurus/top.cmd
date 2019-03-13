# Top-level file defining first steps of process

# 1D grid definition usually do not change
line x location=0.0 spacing=1<nm> tag=SiTop
line x location=20<nm> spacing=2<nm>
line x location=100<nm> spacing=10<nm>
line x location=600<nm> spacing=20<nm>
line x location=1<um> spacing=50<nm>
line x location=4<um> spacing=0.2<um> tag=SiBottom

# Initial simulation domain usually do not change
region Silicon xlo=SiTop xhi=SiBottom

# Initialize the simulation (2e15 cm-3 carrier concentration calculated from EE 212 notes)
init field=Boron concentration=2e15<cm-3> resistivity=7.5 wafer.orient=100

# Setting for automatic meshing usually do not change
mgoals min.normal.size=3<nm> max.lateral.size=0.2<um> normal.growth.ratio=1.4

# Blanket implant Boron (V_T adjust)
implant Boron energy=100<keV> dose=4e13<cm-2> tilt=7<degree> gaussian

# Pad formation, including ramping up and down
diffuse temperature=800<C> time=5<min> ramprate=10<C/min>
diffuse temperature=850<C> time=15<min> H2O
diffuse temperature=850<C> time=5<min> O2
diffuse temperature=850<C> time=5<min> ramprate=-10<C/min>

# P-well Activation Diffusion. The gas is N2, which means no oxidation
diffuse temperature=785<C> time=45<min> N2

# Create struct
struct tdr=top