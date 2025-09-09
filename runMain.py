import subprocess
import yaml
from config import *
import pandas as pd
from collections import defaultdict

# Example values — update as needed
dsid_list = [410472, 521385]
campaign_list = ["mc20a", "mc20d", "mc20e"]


df_flist = pd.read_csv(inputDir+'filelist.txt', sep='\s+', header=None)
df_flist.columns = ['dsid', 'campaign', 'sim', 'path']

sample_info = yaml.safe_load(yaml_data)

df_sumw = pd.read_csv(inputDir+'sum_of_weights.txt', sep='\s+', header=None)
df_sumw.columns = ['dsid', 'campaign', 'sim', 'systematic', 'sumweight']


df_combined = pd.merge(df_flist, df_sumw, on=['dsid', 'campaign', 'sim'], how='left')

search_list = []
for sample in sample_info['samples']:
    dsids = sample.get('dsids', [])
    campaigns = sample.get('campaigns', [])
    for dsid in dsids:
        for campaign in campaigns:
            search_list.append((dsid, campaign))


grouped_files = defaultdict(list)

for _, row in df_combined.iterrows():
    key = (row['dsid'], row['campaign'])
    if key in search_list:
        if row['path'] in grouped_files[key]:
            continue
        else:
            grouped_files[key].append(row['path'])


for key, paths in grouped_files.items():
    dsid, campaign = key
    print(dsid, campaign)
    for i,s in enumerate(paths):
        job_name = f"job_{dsid}_{campaign}_{i}"
        slurm_filename = f"{job_name}_{i}.slurm"
        log_output = f"output_{dsid}_{campaign}_{i}.log"
        log_error = f"error_{dsid}_{campaign}_{i}.log"

        slurm_script = f"""#!/bin/bash
#SBATCH --job-name={job_name}
#SBATCH --output={log_output}
#SBATCH --error={log_error}
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=2:00:00

export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
source ${{ATLAS_LOCAL_ROOT_BASE}}/user/atlasLocalSetup.sh
lsetup "views LCG_107a_ATLAS_2 x86_64-el9-gcc13-opt"

cd /remote/nas00-0/shared/atlas/top/ttbar/atlas_toponium_rjr/

python makeSkim.py --dsid {dsid} --campaign {campaign} --inputfile {s}
"""

        # Write SLURM script
        with open(slurm_filename, "w") as f:
            f.write(slurm_script)

        # Submit job
        try:
            result = subprocess.run(["sbatch", slurm_filename], check=True, capture_output=True, text=True)
            print(f"Submitted {job_name}: {result.stdout.strip()}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to submit {job_name}: {e.stderr.strip()}")