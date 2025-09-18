# toponium_restframe_ATLAS



setupATLAS
lsetup "root recommended"

Need to have installation of RestFrames


and then run 

```root toponium.C``` with modified file names and path

To work with ATLAS sample, we need to ensure TChain is used - this needs to be developed
But for a start we can use one of MC20a files for toponium and ttbar

The toponium.C file needs to be updated 


The NTuples are stored at: /remote/nas00-0/shared/atlas/top/ttbar/atlas_toponium_rjr/

410472: ttbar
521385: toponium - mg5

PDG IDs

410472/mc20a_user.jnesbitt.44244453._000001.syst_scout.root
521385/mc20a_user.jnesbitt.45480013._000001.nominal_modelling_toponium.root





Branches stored in the root files


*Br    0 :el_eta_std : vector<float>                                         *
*Entries :     9674 : Total  Size=     171746 bytes  File Size  =      72916 *
*Baskets :        7 : Basket Size=      32000 bytes  Compression=   2.35     *
*............................................................................*
*Br    1 :el_pt_NOSYS_std : vector<float>                                    *
*Entries :     9674 : Total  Size=     171801 bytes  File Size  =      70141 *
*Baskets :        7 : Basket Size=      32000 bytes  Compression=   2.44     *
*............................................................................*
*Br    2 :el_e_NOSYS_std : vector<float>                                     *
*Entries :     9674 : Total  Size=     171790 bytes  File Size  =      70742 *
*Baskets :        7 : Basket Size=      32000 bytes  Compression=   2.42     *
*............................................................................*
*Br    3 :el_phi_std : vector<float>                                         *
*Entries :     9674 : Total  Size=     171746 bytes  File Size  =      72875 *
*Baskets :        7 : Basket Size=      32000 bytes  Compression=   2.35     *
*............................................................................*
*Br    4 :el_charge_std : vector<float>                                      *
*Entries :     9674 : Total  Size=     171779 bytes  File Size  =      35000 *
*Baskets :        7 : Basket Size=      32000 bytes  Compression=   4.89     *
*............................................................................*
*Br    5 :mu_eta_std : vector<float>                                         *
*Entries :     9674 : Total  Size=     178754 bytes  File Size  =      80175 *
*Baskets :        7 : Basket Size=      32000 bytes  Compression=   2.22     *
*............................................................................*
*Br    6 :mu_e_NOSYS_std : vector<float>                                     *
*Entries :     9674 : Total  Size=     178798 bytes  File Size  =      77814 *
*Baskets :        7 : Basket Size=      32000 bytes  Compression=   2.29     *
*............................................................................*
*Br    7 :mu_pt_NOSYS_std : vector<float>                                    *
*Entries :     9674 : Total  Size=     178809 bytes  File Size  =      77120 *
*Baskets :        7 : Basket Size=      32000 bytes  Compression=   2.31     *
*............................................................................*
*Br    8 :mu_phi_std : vector<float>                                         *
*Entries :     9674 : Total  Size=     178754 bytes  File Size  =      80394 *
*Baskets :        7 : Basket Size=      32000 bytes  Compression=   2.22     *
*............................................................................*
*Br    9 :mu_charge_std : vector<float>                                      *
*Entries :     9674 : Total  Size=     178787 bytes  File Size  =      36013 *
*Baskets :        7 : Basket Size=      32000 bytes  Compression=   4.95     *
*............................................................................*
*Br   10 :jet_eta_std : vector<float>                                        *
*Entries :     9674 : Total  Size=     253589 bytes  File Size  =     156735 *
*Baskets :       10 : Basket Size=      32000 bytes  Compression=   1.61     *
*............................................................................*
*Br   11 :jet_phi_std : vector<float>                                        *
*Entries :     9674 : Total  Size=     253589 bytes  File Size  =     156535 *
*Baskets :       10 : Basket Size=      32000 bytes  Compression=   1.62     *
*............................................................................*
*Br   12 :jet_pt_NOSYS_std : vector<float>                                   *
*Entries :     9674 : Total  Size=     253659 bytes  File Size  =     151389 *
*Baskets :       10 : Basket Size=      32000 bytes  Compression=   1.67     *
*............................................................................*
*Br   13 :jet_e_NOSYS_std : vector<float>                                    *
*Entries :     9674 : Total  Size=     253645 bytes  File Size  =     152158 *
*Baskets :       10 : Basket Size=      32000 bytes  Compression=   1.66     *
*............................................................................*
*Br   14 :pass_dilep_ee_NOSYS : pass_dilep_ee_NOSYS/B                        *
*Entries :     9674 : Total  Size=      12513 bytes  File Size  =       4573 *
*Baskets :       23 : Basket Size=        512 bytes  Compression=   2.56     *
*............................................................................*
*Br   15 :pass_dilep_emu_NOSYS : pass_dilep_emu_NOSYS/B                      *
*Entries :     9674 : Total  Size=      12540 bytes  File Size  =       5084 *
*Baskets :       23 : Basket Size=        512 bytes  Compression=   2.31     *
*............................................................................*
*Br   16 :pass_dilep_mumu_NOSYS : pass_dilep_mumu_NOSYS/B                    *
*Entries :     9674 : Total  Size=      12567 bytes  File Size  =       4896 *
*Baskets :       23 : Basket Size=        512 bytes  Compression=   2.40     *
*............................................................................*
*Br   17 :netweight : netweight/D                                            *
*Entries :     9674 : Total  Size=      78135 bytes  File Size  =      72320 *
*Baskets :        3 : Basket Size=      32000 bytes  Compression=   1.07     *
*............................................................................*
*Br   18 :met_phi_NOSYS : met_phi_NOSYS/F                                    *
*Entries :     9674 : Total  Size=      43317 bytes  File Size  =      42107 *
*Baskets :       42 : Basket Size=       1024 bytes  Compression=   1.00     *
*............................................................................*
*Br   19 :met_met_NOSYS : met_met_NOSYS/F                                    *
*Entries :     9674 : Total  Size=      43317 bytes  File Size  =      40603 *
*Baskets :       42 : Basket Size=       1024 bytes  Compression=   1.04     *
*............................................................................*
*Br   20 :jet_GN2v01_FixedCutBEff_65_select : ROOT::VecOps::RVec<char>       *
*Entries :     9674 : Total  Size=     165992 bytes  File Size  =      44156 *
*Baskets :        7 : Basket Size=      32000 bytes  Compression=   3.75     *
*............................................................................*
*Br   21 :jet_GN2v01_FixedCutBEff_70_select : ROOT::VecOps::RVec<char>       *
*Entries :     9674 : Total  Size=     165992 bytes  File Size  =      43382 *
*Baskets :        7 : Basket Size=      32000 bytes  Compression=   3.81     *
*............................................................................*
*Br   22 :jet_GN2v01_FixedCutBEff_77_select : ROOT::VecOps::RVec<char>       *
*Entries :     9674 : Total  Size=     165992 bytes  File Size  =      41396 *
*Baskets :        7 : Basket Size=      32000 bytes  Compression=   4.00     *
*............................................................................*
*Br   23 :jet_GN2v01_FixedCutBEff_85_select : ROOT::VecOps::RVec<char>       *
*Entries :     9674 : Total  Size=     165992 bytes  File Size  =      41558 *
*Baskets :        7 : Basket Size=      32000 bytes  Compression=   3.98     *
*............................................................................*
*Br   24 :jet_GN2v01_pb : ROOT::VecOps::RVec<float>                          *
*Entries :     9674 : Total  Size=     253617 bytes  File Size  =     147472 *
*Baskets :       10 : Basket Size=      32000 bytes  Compression=   1.72     *
*............................................................................*
*Br   25 :jet_GN2v01_pc : ROOT::VecOps::RVec<float>                          *
*Entries :     9674 : Total  Size=     253617 bytes  File Size  =     158316 *
*Baskets :       10 : Basket Size=      32000 bytes  Compression=   1.60     *
*............................................................................*
*Br   26 :jet_GN2v01_ptau : ROOT::VecOps::RVec<float>                        *
*Entries :     9674 : Total  Size=     253645 bytes  File Size  =     161757 *
*Baskets :       10 : Basket Size=      32000 bytes  Compression=   1.56     *
*............................................................................*
*Br   27 :jet_GN2v01_pu : ROOT::VecOps::RVec<float>                          *
*Entries :     9674 : Total  Size=     253617 bytes  File Size  =     156584 *
*Baskets :       10 : Basket Size=      32000 bytes  Compression=   1.62     *
*............................................................................*
