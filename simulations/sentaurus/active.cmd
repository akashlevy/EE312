# Load top-level struct
init tdr=top

# Setting for automatic meshing usually do not change
mgoals min.normal.size=3<nm> max.lateral.size=0.2<um> normal.growth.ratio=1.4

# Diffusion from field-oxide region
diffuse temperature=800<C> time=20<min> ramprate=10<C/min>
diffuse temperature=1000<C> time=105<min>
diffuse temperature=1000<C> time=20<min> ramprate=-10<C/min>

# Strip oxide
strip Oxide

# Kooi oxidation
diffuse temperature=800<C> time=10<min> ramprate=10<C/min>
diffuse temperature=850<C> time=15<min> H2O
diffuse temperature=850<C> time=10<min> ramprate=-10<C/min>
strip Oxide

# Gate oxidation
diffuse temperature=800<C> time=10<min> ramprate=10<C/min>
diffuse temperature=900<C> time=20<min> O2
diffuse temperature=900<C> time=10<min> ramprate=-10<C/min>

# Create struct
struct tdr=active