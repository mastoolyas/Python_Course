import myModules.Utils as utils # look for Utils under myMdoules sub dir
# import from first go to current dir and subs or in variable PYTHONPATH or in Python install dir
# other path need to be define in the system var
# power shell: Get-ChildItem Env:
import sys
from myModules.Infra import add  # without saving the name space , not recommended
run_time_path = r"C:\temp"
sys.path.append(run_time_path)  # add the path to sys path and then python can look also there for modules

res = utils.add(3, 9, 11)  # call function from Utils - import
print(res)
res = add(2, 3)          # using add function form the last from
print(res)
