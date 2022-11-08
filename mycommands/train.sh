#!/usr/bin/bash
#SBATCH --mem=16gb                   # Job memory request
#SBATCH --time=0                      # Time limit hrs:min:sec
#SBATCH --gres=gpu:1                # Number of gpu
#SBATCH --cpus-per-task=4            # Number of CPU cores per task
#SBATCH --output=./log/%j.log   # Standard output and error log, the program output will be here
​
# you can always have this
eval "$(conda shell.bash hook)"
# you environment
source /home/nnishika/miniconda3/etc/profile.d/conda.sh
conda activate msdbert
​
export TQDM_DISABLE=1
# code

python run_classifier.py --data_dir ./toy_data/ --image_dir ./toy_images --output_dir ./output/MsdBERT_output/  --do_train --do_test --model_select MsdBERT --train_batch_size 16
