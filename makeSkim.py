import ROOT
import pandas as pd
import yaml
from collections import defaultdict
import re
import os
from config import *
import argparse

ROOT.gErrorIgnoreLevel = ROOT.kWarning

parser = argparse.ArgumentParser(description="DSID and Campaign")

parser.add_argument(
    "--dsid", 
    type=int, 
    required=True, 
    help="mc id"
)

parser.add_argument(
    "--campaign", 
    type=str, 
    required=True, 
    help="Campaign"
)

parser.add_argument(
    "--inputfile", 
    type=str, 
    required=True, 
    help="inputfile"
)

args = parser.parse_args()


keep_branches = [

    # electrons
    "el_eta",
    "el_pt_NOSYS",
    "el_e_NOSYS",
    "el_phi",
    "el_charge",

    # muons
    "mu_eta",
    "mu_e_NOSYS",
    "mu_pt_NOSYS",
    "mu_phi",
    "mu_charge",

    # jet
    "jet_eta",
    "jet_phi",
    "jet_pt_NOSYS",
    "jet_e_NOSYS",

    # MET
]

def Analysis(df, dsid='0', campaign='none', xsection = 0, sumWeights=1, output=""):
    
    if not os.path.isdir(str(dsid)):
        ROOT.gSystem.mkdir(str(dsid))
    print("processing ", dsid, campaign, output)
    #f = ROOT.TFile.Open(str(dsid)+"/"+ campaign+"_"+output,"RECREATE")

    if campaign == 'mc20a':
        lumi = 36646.74
    if campaign == 'mc20d':
        lumi = 44630.6
    if campaign == 'mc20e':
        lumi = 58791.6

    df = df.Define("lumi","{}".format(lumi))
    df = df.Define("xsection","{}".format(xsection))
    df = df.Define("sumWeights","{}".format(sumWeights))

    df = df.Define("prodweight","weight_mc_NOSYS * weight_pileup_NOSYS * weight_jvt_effSF_NOSYS * globalTriggerEffSF_NOSYS * globalTriggerMatch_NOSYS* weight_ftag_effSF_GN2v01_Continuous_NOSYS")
    df = df.Define("netweight", "prodweight*lumi*xsection/sumWeights")

    branches_to_store_reco = [
    "pass_dilep_ee_NOSYS", "pass_dilep_emu_NOSYS", "pass_dilep_mumu_NOSYS","netweight", "met_phi_NOSYS",
    "met_met_NOSYS",
    ]

    for br in keep_branches:

        df = df.Define(f"{br}_std",
                        f"std::vector<float>({br}.begin(), {br}.end())")

    keep_branches_std = [f"{br}_std" for br in keep_branches]


    branches_to_store = keep_branches_std  + branches_to_store_reco
    opts = ROOT.RDF.RSnapshotOptions()
    opts.fMode = "RECREATE"

    df.Snapshot("events", str(dsid)+"/"+ campaign+"_"+output, branches_to_store, opts) 

    del df


cross_section = {
    410472: 87.8676,
    802381: 0.07
}


df_flist = pd.read_csv(inputDir+'filelist.txt', sep='\s+', header=None)
df_flist.columns = ['dsid', 'campaign', 'sim', 'path']

sample_info = yaml.safe_load(yaml_data)

df_sumw = pd.read_csv(inputDir+'sum_of_weights.txt', sep='\s+', header=None)
df_sumw.columns = ['dsid', 'campaign', 'sim', 'systematic', 'sumweight']

df_combined = pd.merge(df_flist, df_sumw, on=['dsid', 'campaign', 'sim'], how='left')

dsid, campaign = args.dsid, args.campaign

sumWeights = df_combined[(df_combined['dsid'] == dsid) & (df_combined['campaign'] == campaign)]['sumweight'].iloc[0]
xsection = cross_section[dsid]

s = args.inputfile
print("input file ", s)

outputname = os.path.basename(s)
print("output file ", outputname)

# Directly open the tree from the file
df_tree = ROOT.RDataFrame("reco", s)

Analysis(df_tree, dsid, campaign=campaign, xsection=xsection, sumWeights=sumWeights, output=outputname)





