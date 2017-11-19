# Cara 1 8. Modules and Packages
import my_modul_and_packages
my_modul_and_packages.func_in_module() # namamodul diikuti method modulnya

# Cara 2 dengan alias as 8. Modules and Packages
import my_modul_and_packages as mm # bisa pakai alias agar lebih simple
mm.func_in_module() # namamodul aliasnya mm diikuti method modulnya

from my_modul_and_packages import * # dengan * mengimport semua modul/method yang ada di folder atau modul my_modul_and_packages
func_in_module()