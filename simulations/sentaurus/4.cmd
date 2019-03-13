# Load active struct
init tdr=active

# Setting for automatic meshing usually do not change
mgoals min.normal.size=3<nm> max.lateral.size=0.2<um> normal.growth.ratio=1.4

# Deposit Polysilicon
deposit poly type=anisotropic thickness=600<nm> temperature=400<C>

# N-Dope S/D Implant: implant another dopant, Arsenic
implant Arsenic energy=50<keV> dose=2.0e15<cm-2> gaussian

# Deposit LTO
deposit Oxide type=isotropic thickness=600<nm> temperature=400<C>

# LTO Densification
diffuse temperature=800<C> time=15<min> ramprate=10<C/min>
diffuse temperature=950<C> time=30<min> H2O
diffuse temperature=950<C> time=15<min> ramprate=-10<C/min>

# Create struct
struct tdr=cross4

# Outputs
layers
SheetResistance
