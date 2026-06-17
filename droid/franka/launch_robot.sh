source /home/prism-droid-nuc/miniconda3/etc/profile.d/conda.sh
conda activate polymetis-local
pkill -9 run_server
pkill -9 franka_panda_cl
/home/prism-droid-nuc/miniconda3/envs/polymetis-local/bin/launch_robot.py robot_client=franka_hardware hydra.run.dir=/tmp/hydra_launch_robot
