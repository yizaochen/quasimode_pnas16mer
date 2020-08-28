from os import path
import numpy as np

KBOLTZ = 1.987191e-3  # Unit: kcal mol-1 K-1
TEMP = 310
RTEMP = KBOLTZ * TEMP # Unit: kcal mol-1

class QuasiEigvalue:

    d_natoms = {'arna+arna': 676, 'bdna+bdna': 650}
    def __init__(self, rootfolder, type_na):
        self.type_na = type_na
        self.n_atoms = self.d_natoms[type_na]
        self.dof = 3 * self.n_atoms # Degree of Freedom
        self.na_folder = path.join(rootfolder, type_na)
        self.f_in = path.join(self.na_folder, 'qha.eigenvalue.txt') 
        self.qha_eigvalues = dict()

    def get_c_square_array(self, start_modeid, end_modeid):
        """
           Get <c_i^2>
        """
        qha_eigenvalues = self.__get_qha_eigenvalues()
        qha_eigenvalues = qha_eigenvalues[start_modeid-1:end_modeid]
        c_square_array =  RTEMP/qha_eigenvalues
        return c_square_array

    def __get_qha_eigenvalues(self):
        temp = np.genfromtxt(self.f_in)
        temp = temp.flatten()
        for mode in range(1, self.dof+1):
            idx = self.dof - mode
            self.qha_eigvalues[mode] = temp[idx]
        qha_eigenvalues = [self.qha_eigvalues[modeid] for modeid in range(1, self.dof+1)]
        qha_eigenvalues = np.array(qha_eigenvalues)
        qha_eigenvalues[-6:] = np.zeros(6)
        return qha_eigenvalues
    
