# Load top-level struct
init tdr=top

# Setting for automatic meshing usually do not change
mgoals min.normal.size=3<nm> max.lateral.size=0.2<um> normal.growth.ratio=1.4

# Boron isolation implant
implant Boron energy=30<keV> dose=1e15<cm-2> tilt=7<degree> gaussian

# Field oxidation
diffuse temperature=800<C> time=20<min> ramprate=10<C/min>
diffuse temperature=1000<C> time=105<min> H2O
diffuse temperature=1000<C> time=20<min> ramprate=-10<C/min>

# This solution will etch thermally grown oxide at approximately 2 nm/s at 25 C
etch material=Oxide type=isotropic time=45<s> rate=2<nm/s>

# Kooi oxidation
diffuse temperature=800<C> time=5<min> ramprate=10<C/min>
diffuse temperature=850<C> time=15<min> H2O
diffuse temperature=850<C> time=5<min> ramprate=-10<C/min>

# This solution will etch thermally grown oxide at approximately 2 nm/s at 25 C
etch material=Oxide type=isotropic time=45<s> rate=2<nm/s>

# Gate oxidation
diffuse temperature=800<C> time=10<min> ramprate=10<C/min>
diffuse temperature=900<C> time=20<min> O2
diffuse temperature=900<C> time=10<min> ramprate=-10<C/min>

# Create struct
struct tdr=field_oxide