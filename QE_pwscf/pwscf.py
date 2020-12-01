Class CONTROL:

  def __init__(self,title,nstep,iprint,outdir):
        self.calculation      =    "scf"                
        self.title            =     title
        self.verbosity        =    'low'        
        self.restart_mode     =    'from_scratch'         
        self.wf_collect       =    '.TRUE.'     
        self.nstep            =    nstep 
        self.iprint           =    iprint   
        self.tstress          =    '.FALSE.'     
        self.tprnfor          =    '.FALSE.'
        self.dt               =    dt
        self.outdir           =    outdir    
        self.wfcdir           =    outdir 
        self.prefix           =    'pwscf'    
        self.lkpoint_dir      =    '.TRUE.'          
        self.max_seconds      =    '1.D+7'         
        self.etot_conv_thr    =    '1.0D-4'           
        self.forc_conv_thr    =    '1.0D-3'           
        self.disk_io          =    'low'     
        self.pseudo_dir       =    pseudo_dir      
        self.tefield          =    '.FALSE.'    
        self.dipfield         =    '.FALSE.'   
        self.lelfield         =    '.FALSE.'    
        self.nberrycyc        =    '1'      
        self.lorbm            =    '.FALSE.'  
        self.lberry           =    '.FALSE.' 
        self.gdir             =     gdir
        self.nppstr           =     nppstr
        self.lfcpopt          =     '.FALSE.'    
        self.gate             =     '.FALSE.'  

Class SYSTEM:

    def __init__(self,ibrav)
        self.ibrav                           =  ibrav    

    def set_geom(self,A,B,C,alpha,beta,gamma):                                            
        self.A                               =   A   
        self.B                               =   B     
        self.C                               =   C   
        self.cosAB                           =  gamma        
        self.cosAC                           =  beta        
        self.cosBC                           =  alpha
                                  
    def system_nums(self,nat,ntyp):    

        self.nat                             =   nat     
        self.ntyp                            =   ntyp  

    def band_number(self,nbnd):

        self.nbnd                            =  nbnd

    def charges(tot_charge,starting_charge)        

        self.tot_charge                      =  tot_charge              
        self.starting_charge                 =  starting_charge

    def magnetization(self,tot_magnetization,starting_magnetization):

        self.tot_magnetization               =   tot_magnetization                     
        self.starting_magnetization          =   starting_magnetization 
        self.nspin                           =   nspin                
        self.noncolin                        =   noncolin

    def cutoff(ecutwfc,ecutrho) :             

        self.ecutwfc                         =  ecutwfc            
        self.ecutrho                         =  ecutrho            
        self.ecutfock                        =  ecutrho


    def charge_density_mesh(self,nr1,nr2,nr3):

        self.nr1                             =   nr1       
        self.nr2                             =   nr2       
        self.nr3                             =   nr3 

    def wave_function_mesh(self,nr1s,nr2s,nr3s):

        self.nr1s                            =  nr1s        
        self.nr2s                            =  nr2s        
        self.nr3s                            =  nr3s    

    def symmetry(self,nosym,nosym_evc,noinv,no_t_rev,force_symmorphic,use_all_frac):

        self.nosym                           = nosym            
        self.nosym_evc                       = nosym_evc               
        self.noinv                           = noinv                  
        self.no_t_rev                        = no_t_rev                    
        self.force_symmorphic                = force_symmorphic                                 
        self.use_all_frac                    = use_all_frac  

    def occupation_and_smearing(self,occupations,one_atom_occupations,starting_spin_angle,degauss,smearing):                      
        self.occupations                     =  occupations                       
        self.one_atom_occupations            =  one_atom_occupations                               
        self.starting_spin_angle             =  starting_spin_angle                               
        self.degauss                         =  degauss                   
        self.smearing                        =  smearing


                    
        self.ecfixed                         =                     
        self.qcutz                           =                   
        self.q2sigma                         =                     
        self.input_dft                       =                       
        self.ace                             =                 
        self.exx_fraction                    =                         
        self.screening_parameter             =                                 
        self.exxdiv_treatment                =                             
        self.x_gamma_extrapolation           =                                   
        self.ecutvcut                        =                     
        self.nqx1                            =                 
        self.nqx2                            =                 
        self.nqx3                            =                 
        self.localization_thr                =                             
        self.lda_plus_u                      =                       
        self.lda_plus_u_kind                 =                             
        self.Hubbard_U                       =                       
        self.Hubbard_J0                      =                       
        self.Hubbard_V                       =                       
        self.Hubbard_alpha                   =                           
        self.Hubbard_beta                    =                         
        self.Hubbard_J                       =                       
        self.starting_ns_eigenvalue          =                                   
        self.U_projection_type               =                               
        self.Hubbard_parameters              =                               
        self.ensemble_energies               =                               
        self.edir                            =                 
        self.emaxpos                         =                     
        self.eopreg                          =                   
        self.eamp                            =                 
        self.angle1                          =                   
        self.angle2                          =                   
        self.lforcet                         =                     
        self.constrained_magnetization       =                                       
        self.fixed_magnetization             =                                 
        self.lambda_val                      =                       
        self.report                          =                   
        self.lspinorb                        =                     
        self.assume_isolated                 =                             
        self.esm_bc                          =                                                           
        self.esm_w                           =                     
        self.esm_efield                      =                         
        self.esm_nfit                        =                       
        self.fcp_mu                          =                     
        self.vdw_corr                        =                       
        self.london                          =                     
        self.london_s6                       =                         
        self.london_c6                       =                         
        self.london_rvdw                     =                           
        self.london_rcut                     =                           
        self.dftd3_version                   =                             
        self.dftd3_threebody                 =                               
        self.ts_vdw_econv_thr                =                               
        self.ts_vdw_isolated                 =                               
        self.xdm                             =                   
        self.xdm_a1                          =                     
        self.xdm_a2                          =                     
        self.space_group                     =                           
        self.uniqueb                         =                       
        self.origin_choice                   =                             
        self.rhombohedral                    =                           
        self.zgate                           =                     
        self.relaxz                          =                     
        self.block                           =                     
        self.block_1                         =                       
        self.block_2                         =                       
        self.block_height                    =                           


 def ELECTRONS():                                       


    electron_maxstep                =                                    
    scf_must_converge               =                      
    conv_thr                        =            
    adaptive_thr                    =                
    conv_thr_init                   =                  
    conv_thr_multi                  =                  
    mixing_mode                     =                
    mixing_beta                     =                
    mixing_ndim                     =                
    mixing_fixed_ns                 =                    
    diagonalization                 =                    
    diago_thr_init                  =                  
    diago_cg_maxiter                =                    
    diago_david_ndim                =                    
    diago_full_acc                  =                  
    efield                          =          
    efield_cart                     =                
    efield_phase                    =                
    startingpot                     =                
    startingwfc                     =                
    tqr                             =        
    real_space                      =              

def IONS():

    ion_positions                   =                          
    ion_velocities                  =              
    ion_dynamics                    =            
    pot_extrapolation               =                  
    wfc_extrapolation               =                  
    remove_rigid_rot                =                
    ion_temperature                 =                
    tempw                           =      
    tolp                            =    
    delta_t                         =        
    nraise                          =      
    refold_pos                      =          
    upscale                         =        
    bfgs_ndim                       =          
    trust_radius_max                =                
    trust_radius_min                =                
    trust_radius_ini                =                
    w_1                             =    
    w_2                             =    

def CELL():

    cell_dynamics                   =                                    
    press                           =        
    wmass                           =        
    cell_factor                     =              
    press_conv_thr                  =                
    cell_dofree                     =              


