#/bin/bash

#run this file in the terminal as "bash create_env.bash"
# it will ask you if you want to proceed, type y+enter 
#It will then tell you to activate the environment which you can do from the command line 
# or from the navigator

conda create -n BIOF_env python=3.8 numpy pandas matplotlib biopython scikit-learn seaborn scipy
