from ase.build import bulk
from koopmans.kpoints import Kpoints
from koopmans.workflows import WannierizeWorkflow

# Use ASE to create bulk silicon
atoms = bulk('Si')

# Create the workflow
workflow = SinglepointWorkflow(atoms=atoms,
        kpoints=Kpoints(grid=[8, 8, 8], cell=atoms.cell))

# Run the workflow
workflow.run()
