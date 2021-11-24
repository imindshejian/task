from sys import argv
from pymatgen.ext.matproj import MPRester
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.core.surface import Slab, SlabGenerator, Structure
from pymatgen.io.vasp.inputs import Poscar

USER_API_KEY = argv[1]
mpr = MPRester(USER_API_KEY)
m_id = "mp-22526"

#We can get conventional cell directly like this

structure = mpr.get_structure_by_material_id(m_id, 
                                             conventional_unit_cell = True)
slab = SlabGenerator(initial_structure = structure, 
                     miller_index = [1, 0, 4],
                     min_slab_size = 10, 
                     min_vacuum_size = 10)

#add a for loop here maybe better though not need in this case

for n, slabs in enumerate(slab.get_slabs()):
    slabs.make_supercell([[2,0,0],
                          [0,2,0],
                          [0,0,1]])
    open('POSCAR' + str(n) , 'w').write(str(Poscar(slabs)))




