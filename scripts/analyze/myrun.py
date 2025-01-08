# Script to set up parameters for MibS instance path.
# Used to run experiments for diffrent cuts 
# Last edited by yux616
# Apr 2020

# Executable path and name
pbsfile = '/home/feb223/improvingDir/MibS/scripts/analyze/mibs_batch.pbs'

# Instance path
# Directory name and path containing test instances in .mps format
# Keys are used to name subdirs in output dir
instanceDirs = {
    # "ObjNotMatching" : "/home/feb223/Datasets/MIBLPLib/ObjNotMatching"
    "iblpDen"    : "/home/feb223/Datasets/MIBLPLib/iblpDen",
    "iblpDen2"   : "/home/feb223/Datasets/MIBLPLib/iblpDen2",
    "iblpZhang"  : "/home/feb223/Datasets/MIBLPLib/iblpZhang",
    "iblpZhang2" : "/home/feb223/Datasets/MIBLPLib/iblpZhang2",
    "iblpFis"    : "/home/feb223/Datasets/MIBLPLib/iblpFis",
    "interKpShi" : "/home/feb223/Datasets/MIBLPLib/interKpShi",
    "interDen"   : "/home/feb223/Datasets/MIBLPLib/interdDen",
    # "miblpXu"    : "/home/feb223/Datasets/MIBLPLib/miblpXu"
}

#versions = ['1.1', 'ib']
#versions = ['1.2-opt']
# versions = ['ipco', '1.2']
versions = ['idBC']

# Output parent path
outputDir = '/home/feb223/results/MibS'

# Name
testname = 'idBC'

# Write parameters into files?
writeParams = True

# Set up senarios
mibsParamsInputs = {}

commonParams = {
    'Alps_timeLimit': '3600',
    'Alps_msgLevel': '1',
    # 'Alps_nodeLimit': '0',
    # 'Blis_scaleConFactor': '10000000000',
    # 'Blis_heurStrategy': '0',             # -2: root, -1: auto, 0: disable, any positive integer
    # 'Blis_heurRound': '0',                # -2: root, -1: auto, 0: disable, any positive integer
    # 'MibS_usePreprocessor': '0',          # -1: auto, 0: false, 1: true
    # 'MibS_useLowerObjHeuristic': '0',     # -1: auto, 0: false, 1: true
    # 'MibS_useObjCutHeuristic': '0',       # -1: auto, 0: false, 1: true
    # 'MibS_useWSHeuristic': '0',           # -1: auto, 0: false, 1: true
    # 'MibS_useGreedyHeuristic': '0',       # 0: false, 1: true
    # 'MibS_objBoundStrategy': '0',         # 0: LL obj bound, 1: interdiction bound
    # 'MibS_blisCutStrategy': '0',         # -2: root, -1: auto, 0: disable, any positive integer
    # 'MibS_warmStartLL': '0',
    # 'MibS_maxThreadsLL': '1',
    # 'MibS_allowRemoveCut': '0',           # 0: false, 1: true
    # 'MibS_whichCutsLL': '2',              # 0: no cuts, 1: gomory only, 2: all cuts
    # 'MibS_doDualFixing': '0',
    # 'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
    # 'MibS_feasCheckSolver': 'SYMPHONY',
    "MibS_useFractionalCuts" : "1",
    'MibS_useImprovingDirectionPool' : '0',
    'MibS_printParameters': '1'
} 

#--------------------------------------------------
# idB&C k = 2 dBnd = 10 Configurations
#--------------------------------------------------

# mibsParamsInputs['idBC-LS-k_2-dBnd_Inf_fracB'] = {
#     "MibS_branchStrategy" : "0",
#     "MibS_useImprovingDirectionOracle" : "1",
#     "MibS_turnOffDefaultCuts" : "1",
#     "MibS_useIntersectionCut" : "1",
#     "MibS_useImprovingSolutionIC" : "0",
#     "MibS_useImprovingDirectionIC" : "1",
#     "MibS_improvingDirectionType" : "1",
#     "MibS_maxSizeNeighborhood" : "2",
#     "MibS_maxFeasImprovingDirections" : "10",
#     "MibS_useLocalSearchDepthLb" : "0",
#     "MibS_useLocalSearchDepthUb" : "10000",
#     "MibS_solveSecondLevelWhenXYVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenXVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenLVarsFixed"  : "0",
#     "MibS_solveSecondLevelWhenLVarsInt"  : "0",
#     "MibS_solveSecondLevelEveryIteration" :  "0",
#     "MibS_computeBestUBWhenXVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsFixed"  : "0"
# }

# mibsParamsInputs['idBC-LS-k_2-dBnd_0_10_fracB'] = {
#     "MibS_branchStrategy" : "0",
#     "MibS_useImprovingDirectionOracle" : "1",
#     "MibS_turnOffDefaultCuts" : "1",
#     "MibS_useIntersectionCut" : "1",
#     "MibS_useImprovingSolutionIC" : "0",
#     "MibS_useImprovingDirectionIC" : "1",
#     "MibS_improvingDirectionType" : "1",
#     "MibS_maxSizeNeighborhood" : "2",
#     "MibS_maxFeasImprovingDirections" : "10",
#     "MibS_useLocalSearchDepthLb" : "0",
#     "MibS_useLocalSearchDepthUb" : "10",
#     "MibS_solveSecondLevelWhenXYVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenXVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenLVarsFixed"  : "0",
#     "MibS_solveSecondLevelWhenLVarsInt"  : "0",
#     "MibS_solveSecondLevelEveryIteration" :  "0",
#     "MibS_computeBestUBWhenXVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsFixed"  : "0"
# }

# mibsParamsInputs['idBC-LS-k_2-dBnd_10_Inf_fracB'] = {
#     "MibS_branchStrategy" : "0",
#     "MibS_useImprovingDirectionOracle" : "1",
#     "MibS_turnOffDefaultCuts" : "1",
#     "MibS_useIntersectionCut" : "1",
#     "MibS_useImprovingSolutionIC" : "0",
#     "MibS_useImprovingDirectionIC" : "1",
#     "MibS_improvingDirectionType" : "1",
#     "MibS_maxSizeNeighborhood" : "2",
#     "MibS_maxFeasImprovingDirections" : "10",
#     "MibS_useLocalSearchDepthLb" : "10",
#     "MibS_useLocalSearchDepthUb" : "10000",
#     "MibS_solveSecondLevelWhenXYVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenXVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenLVarsFixed"  : "0",
#     "MibS_solveSecondLevelWhenLVarsInt"  : "0",
#     "MibS_solveSecondLevelEveryIteration" :  "0",
#     "MibS_computeBestUBWhenXVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsFixed"  : "0"
# }

# mibsParamsInputs['idBC-k_2-MILP_fracB'] = {
#     "MibS_branchStrategy" : "0",
#     "MibS_useImprovingDirectionOracle" : "1",
#     "MibS_turnOffDefaultCuts" : "1",
#     "MibS_useIntersectionCut" : "1",
#     "MibS_useImprovingSolutionIC" : "0",
#     "MibS_useImprovingDirectionIC" : "1",
#     "MibS_improvingDirectionType" : "0",
#     "MibS_maxSizeNeighborhood" : "2",
#     "MibS_solveSecondLevelWhenXYVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenXVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenLVarsFixed"  : "0",
#     "MibS_solveSecondLevelWhenLVarsInt"  : "0",
#     "MibS_solveSecondLevelEveryIteration" :  "0",
#     "MibS_computeBestUBWhenXVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsFixed"  : "0"
# }

#--------------------------------------------------
# idB&C k = 3 dBnd = 10 Configurations
#--------------------------------------------------

# mibsParamsInputs['idBC-LS-k_3-dBnd_Inf_fracB'] = {
#     "MibS_branchStrategy" : "0",
#     "MibS_useImprovingDirectionOracle" : "1",
#     "MibS_turnOffDefaultCuts" : "1",
#     "MibS_useIntersectionCut" : "1",
#     "MibS_useImprovingSolutionIC" : "0",
#     "MibS_useImprovingDirectionIC" : "1",
#     "MibS_improvingDirectionType" : "1",
#     "MibS_maxSizeNeighborhood" : "3",
#     "MibS_maxFeasImprovingDirections" : "10",
#     "MibS_useLocalSearchDepthLb" : "0",
#     "MibS_useLocalSearchDepthUb" : "10000",
#     "MibS_solveSecondLevelWhenXYVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenXVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenLVarsFixed"  : "0",
#     "MibS_solveSecondLevelWhenLVarsInt"  : "0",
#     "MibS_solveSecondLevelEveryIteration" :  "0",
#     "MibS_computeBestUBWhenXVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsFixed"  : "0"
# }

# mibsParamsInputs['idBC-LS-k_3-dBnd_0_10_fracB'] = {
#     "MibS_branchStrategy" : "0",
#     "MibS_useImprovingDirectionOracle" : "1",
#     "MibS_turnOffDefaultCuts" : "1",
#     "MibS_useIntersectionCut" : "1",
#     "MibS_useImprovingSolutionIC" : "0",
#     "MibS_useImprovingDirectionIC" : "1",
#     "MibS_improvingDirectionType" : "1",
#     "MibS_maxSizeNeighborhood" : "3",
#     "MibS_maxFeasImprovingDirections" : "10",
#     "MibS_useLocalSearchDepthLb" : "0",
#     "MibS_useLocalSearchDepthUb" : "10",
#     "MibS_solveSecondLevelWhenXYVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenXVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenLVarsFixed"  : "0",
#     "MibS_solveSecondLevelWhenLVarsInt"  : "0",
#     "MibS_solveSecondLevelEveryIteration" :  "0",
#     "MibS_computeBestUBWhenXVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsFixed"  : "0"
# }

# mibsParamsInputs['idBC-LS-k_3-dBnd_10_Inf_fracB'] = {
#     "MibS_branchStrategy" : "0",
#     "MibS_useImprovingDirectionOracle" : "1",
#     "MibS_turnOffDefaultCuts" : "1",
#     "MibS_useIntersectionCut" : "1",
#     "MibS_useImprovingSolutionIC" : "0",
#     "MibS_useImprovingDirectionIC" : "1",
#     "MibS_improvingDirectionType" : "1",
#     "MibS_maxSizeNeighborhood" : "3",
#     "MibS_maxFeasImprovingDirections" : "10",
#     "MibS_useLocalSearchDepthLb" : "10",
#     "MibS_useLocalSearchDepthUb" : "10000",
#     "MibS_solveSecondLevelWhenXYVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenXVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenLVarsFixed"  : "0",
#     "MibS_solveSecondLevelWhenLVarsInt"  : "0",
#     "MibS_solveSecondLevelEveryIteration" :  "0",
#     "MibS_computeBestUBWhenXVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsFixed"  : "0"
# }

# mibsParamsInputs['idBC-k_3-MILP_fracB'] = {
#     "MibS_branchStrategy" : "0",
#     "MibS_useImprovingDirectionOracle" : "1",
#     "MibS_turnOffDefaultCuts" : "1",
#     "MibS_useIntersectionCut" : "1",
#     "MibS_useImprovingSolutionIC" : "0",
#     "MibS_useImprovingDirectionIC" : "1",
#     "MibS_improvingDirectionType" : "0",
#     "MibS_maxSizeNeighborhood" : "3",
#     "MibS_solveSecondLevelWhenXYVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenXVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenLVarsFixed"  : "0",
#     "MibS_solveSecondLevelWhenLVarsInt"  : "0",
#     "MibS_solveSecondLevelEveryIteration" :  "0",
#     "MibS_computeBestUBWhenXVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsFixed"  : "0"
# }

#--------------------------------------------------
# idB&C k = 3 dBnd = 8 Configurations
#--------------------------------------------------

# mibsParamsInputs['idBC-LS-k_3-dBnd_0_8_fracB'] = {
#     "MibS_branchStrategy" : "0",
#     "MibS_useImprovingDirectionOracle" : "1",
#     "MibS_turnOffDefaultCuts" : "1",
#     "MibS_useIntersectionCut" : "1",
#     "MibS_useImprovingSolutionIC" : "0",
#     "MibS_useImprovingDirectionIC" : "1",
#     "MibS_improvingDirectionType" : "1",
#     "MibS_maxSizeNeighborhood" : "3",
#     "MibS_maxFeasImprovingDirections" : "10",
#     "MibS_useLocalSearchDepthLb" : "0",
#     "MibS_useLocalSearchDepthUb" : "8",
#     "MibS_solveSecondLevelWhenXYVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenXVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenLVarsFixed"  : "0",
#     "MibS_solveSecondLevelWhenLVarsInt"  : "0",
#     "MibS_solveSecondLevelEveryIteration" :  "0",
#     "MibS_computeBestUBWhenXVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsFixed"  : "0"
# }

# mibsParamsInputs['idBC-LS-k_3-dBnd_8_Inf_fracB'] = {
#     "MibS_branchStrategy" : "0",
#     "MibS_useImprovingDirectionOracle" : "1",
#     "MibS_turnOffDefaultCuts" : "1",
#     "MibS_useIntersectionCut" : "1",
#     "MibS_useImprovingSolutionIC" : "0",
#     "MibS_useImprovingDirectionIC" : "1",
#     "MibS_improvingDirectionType" : "1",
#     "MibS_maxSizeNeighborhood" : "3",
#     "MibS_maxFeasImprovingDirections" : "10",
#     "MibS_useLocalSearchDepthLb" : "8",
#     "MibS_useLocalSearchDepthUb" : "10000",
#     "MibS_solveSecondLevelWhenXYVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenXVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenLVarsFixed"  : "0",
#     "MibS_solveSecondLevelWhenLVarsInt"  : "0",
#     "MibS_solveSecondLevelEveryIteration" :  "0",
#     "MibS_computeBestUBWhenXVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsFixed"  : "0"
# }

# #--------------------------------------------------
# # idB&C k = 3 dBnd = 12 Configurations
# #--------------------------------------------------

# mibsParamsInputs['idBC-LS-k_3-dBnd_0_12_fracB'] = {
#     "MibS_branchStrategy" : "0",
#     "MibS_useImprovingDirectionOracle" : "1",
#     "MibS_turnOffDefaultCuts" : "1",
#     "MibS_useIntersectionCut" : "1",
#     "MibS_useImprovingSolutionIC" : "0",
#     "MibS_useImprovingDirectionIC" : "1",
#     "MibS_improvingDirectionType" : "1",
#     "MibS_maxSizeNeighborhood" : "3",
#     "MibS_maxFeasImprovingDirections" : "10",
#     "MibS_useLocalSearchDepthLb" : "0",
#     "MibS_useLocalSearchDepthUb" : "12",
#     "MibS_solveSecondLevelWhenXYVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenXVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenLVarsFixed"  : "0",
#     "MibS_solveSecondLevelWhenLVarsInt"  : "0",
#     "MibS_solveSecondLevelEveryIteration" :  "0",
#     "MibS_computeBestUBWhenXVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsFixed"  : "0"
# }

# mibsParamsInputs['idBC-LS-k_3-dBnd_12_Inf_fracB'] = {
#     "MibS_branchStrategy" : "0",
#     "MibS_useImprovingDirectionOracle" : "1",
#     "MibS_turnOffDefaultCuts" : "1",
#     "MibS_useIntersectionCut" : "1",
#     "MibS_useImprovingSolutionIC" : "0",
#     "MibS_useImprovingDirectionIC" : "1",
#     "MibS_improvingDirectionType" : "1",
#     "MibS_maxSizeNeighborhood" : "3",
#     "MibS_maxFeasImprovingDirections" : "10",
#     "MibS_useLocalSearchDepthLb" : "12",
#     "MibS_useLocalSearchDepthUb" : "10000",
#     "MibS_solveSecondLevelWhenXYVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenXVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenLVarsFixed"  : "0",
#     "MibS_solveSecondLevelWhenLVarsInt"  : "0",
#     "MibS_solveSecondLevelEveryIteration" :  "0",
#     "MibS_computeBestUBWhenXVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsFixed"  : "0"
# }


#--------------------------------------------------
# idB&C k = 4 dBnd = 10 Configurations
#--------------------------------------------------

# mibsParamsInputs['idBC-LS-k_4-dBnd_Inf_fracB'] = {
#     "MibS_branchStrategy" : "0",
#     "MibS_useImprovingDirectionOracle" : "1",
#     "MibS_turnOffDefaultCuts" : "1",
#     "MibS_useIntersectionCut" : "1",
#     "MibS_useImprovingSolutionIC" : "0",
#     "MibS_useImprovingDirectionIC" : "1",
#     "MibS_improvingDirectionType" : "1",
#     "MibS_maxSizeNeighborhood" : "4",
#     "MibS_maxFeasImprovingDirections" : "10",
#     "MibS_useLocalSearchDepthLb" : "0",
#     "MibS_useLocalSearchDepthUb" : "10000",
#     "MibS_solveSecondLevelWhenXYVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenXVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenLVarsFixed"  : "0",
#     "MibS_solveSecondLevelWhenLVarsInt"  : "0",
#     "MibS_solveSecondLevelEveryIteration" :  "0",
#     "MibS_computeBestUBWhenXVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsFixed"  : "0"
# }

# mibsParamsInputs['idBC-LS-k_4-dBnd_0_10_fracB'] = {
#     "MibS_branchStrategy" : "0",
#     "MibS_useImprovingDirectionOracle" : "1",
#     "MibS_turnOffDefaultCuts" : "1",
#     "MibS_useIntersectionCut" : "1",
#     "MibS_useImprovingSolutionIC" : "0",
#     "MibS_useImprovingDirectionIC" : "1",
#     "MibS_improvingDirectionType" : "1",
#     "MibS_maxSizeNeighborhood" : "4",
#     "MibS_maxFeasImprovingDirections" : "10",
#     "MibS_useLocalSearchDepthLb" : "0",
#     "MibS_useLocalSearchDepthUb" : "10",
#     "MibS_solveSecondLevelWhenXYVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenXVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenLVarsFixed"  : "0",
#     "MibS_solveSecondLevelWhenLVarsInt"  : "0",
#     "MibS_solveSecondLevelEveryIteration" :  "0",
#     "MibS_computeBestUBWhenXVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsFixed"  : "0"
# }

# mibsParamsInputs['idBC-LS-k_4-dBnd_10_Inf_fracB'] = {
#     "MibS_branchStrategy" : "0",
#     "MibS_useImprovingDirectionOracle" : "1",
#     "MibS_turnOffDefaultCuts" : "1",
#     "MibS_useIntersectionCut" : "1",
#     "MibS_useImprovingSolutionIC" : "0",
#     "MibS_useImprovingDirectionIC" : "1",
#     "MibS_improvingDirectionType" : "1",
#     "MibS_maxSizeNeighborhood" : "4",
#     "MibS_maxFeasImprovingDirections" : "10",
#     "MibS_useLocalSearchDepthLb" : "10",
#     "MibS_useLocalSearchDepthUb" : "10000",
#     "MibS_solveSecondLevelWhenXYVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenXVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenLVarsFixed"  : "0",
#     "MibS_solveSecondLevelWhenLVarsInt"  : "0",
#     "MibS_solveSecondLevelEveryIteration" :  "0",
#     "MibS_computeBestUBWhenXVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsFixed"  : "0"
# }

# mibsParamsInputs['idBC-k_4-MILP_fracB'] = {
#     "MibS_branchStrategy" : "0",
#     "MibS_useImprovingDirectionOracle" : "1",
#     "MibS_turnOffDefaultCuts" : "1",
#     "MibS_useIntersectionCut" : "1",
#     "MibS_useImprovingSolutionIC" : "0",
#     "MibS_useImprovingDirectionIC" : "1",
#     "MibS_improvingDirectionType" : "0",
#     "MibS_maxSizeNeighborhood" : "4",
#     "MibS_solveSecondLevelWhenXYVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenXVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenLVarsFixed"  : "0",
#     "MibS_solveSecondLevelWhenLVarsInt"  : "0",
#     "MibS_solveSecondLevelEveryIteration" :  "0",
#     "MibS_computeBestUBWhenXVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsFixed"  : "0"
# }


#--------------------------------------------------
# idB&C k = 5 dBnd = 10 Configurations
#--------------------------------------------------

# mibsParamsInputs['idBC-LS-k_5-dBnd_Inf_fracB'] = {
#     "MibS_branchStrategy" : "0",
#     "MibS_useImprovingDirectionOracle" : "1",
#     "MibS_turnOffDefaultCuts" : "1",
#     "MibS_useIntersectionCut" : "1",
#     "MibS_useImprovingSolutionIC" : "0",
#     "MibS_useImprovingDirectionIC" : "1",
#     "MibS_improvingDirectionType" : "1",
#     "MibS_maxSizeNeighborhood" : "5",
#     "MibS_maxFeasImprovingDirections" : "10",
#     "MibS_useLocalSearchDepthLb" : "0",
#     "MibS_useLocalSearchDepthUb" : "10000",
#     "MibS_solveSecondLevelWhenXYVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenXVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenLVarsFixed"  : "0",
#     "MibS_solveSecondLevelWhenLVarsInt"  : "0",
#     "MibS_solveSecondLevelEveryIteration" :  "0",
#     "MibS_computeBestUBWhenXVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsFixed"  : "0"
# }

# mibsParamsInputs['idBC-LS-k_5-dBnd_0_10_fracB'] = {
#     "MibS_branchStrategy" : "0",
#     "MibS_useImprovingDirectionOracle" : "1",
#     "MibS_turnOffDefaultCuts" : "1",
#     "MibS_useIntersectionCut" : "1",
#     "MibS_useImprovingSolutionIC" : "0",
#     "MibS_useImprovingDirectionIC" : "1",
#     "MibS_improvingDirectionType" : "1",
#     "MibS_maxSizeNeighborhood" : "5",
#     "MibS_maxFeasImprovingDirections" : "10",
#     "MibS_useLocalSearchDepthLb" : "0",
#     "MibS_useLocalSearchDepthUb" : "10",
#     "MibS_solveSecondLevelWhenXYVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenXVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenLVarsFixed"  : "0",
#     "MibS_solveSecondLevelWhenLVarsInt"  : "0",
#     "MibS_solveSecondLevelEveryIteration" :  "0",
#     "MibS_computeBestUBWhenXVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsFixed"  : "0"
# }

# mibsParamsInputs['idBC-LS-k_5-dBnd_10_Inf_fracB'] = {
#     "MibS_branchStrategy" : "0",
#     "MibS_useImprovingDirectionOracle" : "1",
#     "MibS_turnOffDefaultCuts" : "1",
#     "MibS_useIntersectionCut" : "1",
#     "MibS_useImprovingSolutionIC" : "0",
#     "MibS_useImprovingDirectionIC" : "1",
#     "MibS_improvingDirectionType" : "1",
#     "MibS_maxSizeNeighborhood" : "5",
#     "MibS_maxFeasImprovingDirections" : "10",
#     "MibS_useLocalSearchDepthLb" : "10",
#     "MibS_useLocalSearchDepthUb" : "10000",
#     "MibS_solveSecondLevelWhenXYVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenXVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenLVarsFixed"  : "0",
#     "MibS_solveSecondLevelWhenLVarsInt"  : "0",
#     "MibS_solveSecondLevelEveryIteration" :  "0",
#     "MibS_computeBestUBWhenXVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsFixed"  : "0"
# }

# mibsParamsInputs['idBC-k_5-MILP_fracB'] = {
#     "MibS_branchStrategy" : "0",
#     "MibS_useImprovingDirectionOracle" : "1",
#     "MibS_turnOffDefaultCuts" : "1",
#     "MibS_useIntersectionCut" : "1",
#     "MibS_useImprovingSolutionIC" : "0",
#     "MibS_useImprovingDirectionIC" : "1",
#     "MibS_improvingDirectionType" : "0",
#     "MibS_maxSizeNeighborhood" : "5",
#     "MibS_solveSecondLevelWhenXYVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenXVarsInt"  : "0",
#     "MibS_solveSecondLevelWhenLVarsFixed"  : "0",
#     "MibS_solveSecondLevelWhenLVarsInt"  : "0",
#     "MibS_solveSecondLevelEveryIteration" :  "0",
#     "MibS_computeBestUBWhenXVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsInt"  : "0",
#     "MibS_computeBestUBWhenLVarsFixed"  : "0"
# }



#--------------------------------------------------
# MibS 1.2 Configurations
#--------------------------------------------------

# # Mibs 1.2 default (IDICs may be turned off) 
# mibsParamsInputs['MibS_1_2_defaultB'] = {
#     "MibS_useImprovingDirectionOracle" : "0"
# }

# # Mibs 1.2 default (IDICs)
# mibsParamsInputs['MibS_1_2_IDIC_defaultB'] = {
#     "MibS_useImprovingDirectionOracle" : "0",
#     "MibS_useImprovingDirectionIC" : "1",
#     "MibS_improvingDirectionType" : "0"
# }

# # Mibs 1.2 default (IDICs on with LS)
# mibsParamsInputs['MibS_1_2-LS-k_3_defaultB'] = {
#     "MibS_useImprovingDirectionOracle" : "0",
#     "MibS_useImprovingDirectionIC" : "1",
#     "MibS_improvingDirectionType" : "1",
#     "MibS_maxSizeNeighborhood" : "3",
#     "MibS_maxFeasImprovingDirections" : "10",
#     "MibS_useLocalSearchDepthLb" : "10",
#     "MibS_useLocalSearchDepthUb" : "10000"
# }

# Mibs 1.2 default (IDICs on with LS)
mibsParamsInputs['MibS_1_2-LS-k_2_defaultB'] = {
    "MibS_useImprovingDirectionOracle" : "0",
    "MibS_useImprovingDirectionIC" : "1",
    "MibS_improvingDirectionType" : "1",
    "MibS_maxSizeNeighborhood" : "2",
    "MibS_maxFeasImprovingDirections" : "10",
    "MibS_useLocalSearchDepthLb" : "10",
    "MibS_useLocalSearchDepthUb" : "10000"
}

# # Mibs 1.2 (only IDICs)
# mibsParamsInputs['MibS_onlyIDIC_fracB'] = {
#     "MibS_branchStrategy" : "0",
#     "MibS_useImprovingDirectionOracle" : "0",
#     "MibS_turnOffDefaultCuts" : "1",
#     "MibS_useIntersectionCut" : "1",
#     "MibS_useImprovingSolutionIC" : "0",
#     "MibS_useImprovingDirectionIC" : "1",
#     "MibS_improvingDirectionType" : "0"
# }



# mibsParamsInputs['kSwaps+IDP_fracB'] = {
#     'MibS_turnOffDefaultCuts': '1',
#     'MibS_useIntersectionCut': '1',
#     'MibS_useImprovingSolutionIC': '0',
#     'MibS_useImprovingDirectionIC': '1',
#     'MibS_improvingDirectionType': '1',
#     'MibS_maxSizeNeighborhood': '3',
#     'MibS_useFractionalCuts': '1',
#     'MibS_useImprovingDirectionPool': '1'
# }

# mibsParamsInputs['watermelon+IDP_fracB'] = {
#     'MibS_turnOffDefaultCuts': '1',
#     'MibS_useIntersectionCut': '1',
#     'MibS_useImprovingSolutionIC': '0',
#     'MibS_useImprovingDirectionIC': '1',
#     'MibS_improvingDirectionType': '0',
#     'MibS_useFractionalCuts': '1',
#     'MibS_useImprovingDirectionPool': '1'
# }

# mibsParamsInputs['kSwaps_fracB'] = {
#     'MibS_turnOffDefaultCuts': '1',
#     'MibS_useIntersectionCut': '1',
#     'MibS_useImprovingSolutionIC': '0',
#     'MibS_useImprovingDirectionIC': '1',
#     'MibS_improvingDirectionType': '1',
#     'MibS_maxSizeNeighborhood': '3',
#     'MibS_useFractionalCuts': '1',
#     'MibS_useImprovingDirectionPool': '0'
# }

# mibsParamsInputs['watermelon_fracB'] = {
#     'MibS_turnOffDefaultCuts': '1',
#     'MibS_useIntersectionCut': '1',
#     'MibS_useImprovingSolutionIC': '0',
#     'MibS_useImprovingDirectionIC': '1',
#     'MibS_improvingDirectionType': '0',
#     'MibS_useFractionalCuts': '1',
#     'MibS_useImprovingDirectionPool': '0'   
# }

# mibsParamsInputs['default'] = {
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
# }

# mibsParamsInputs['default+NoFractionalCutsAndLinking'] = {
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_useFractionalCuts': '0',
# }

# mibsParamsInputs['default+NoFractionalCutsAndFrac'] = {
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     'MibS_useFractionalCuts': '0',           # 0: fractional, 1: linking
# }

#mibsParamsInputs['default+NoFractionalCutswithExtraOutput'] = {
#    'MibS_useFractionalCuts': '0',           # 0: fractional, 1: linking
#}

#mibsParamsInputs['default'] = {
#    'MibS_feasCheckSolver': 'CPLEX',           # 0: fractional, 1: linking
#}

#mibsParamsInputs['default+MIP'] = {
#    'MibS_blisCutStrategy': '-1',           # 0: fractional, 1: linking
#}

#mibsParamsInputs['default+FracRoot'] = {
#    'MibS_useFractionalCutsRootOnly': '1',           # 0: fractional, 1: linking
#}

#mibsParamsInputs['default+Parallel'] = {
#    'MibS_maxThreadsLL': '16',           # 0: fractional, 1: linking
#}

#mibsParamsInputs['default+ParallelCplex'] = {
#    'MibS_maxThreadsLL': '16',           # 0: fractional, 1: linking
#    'MibS_feasCheckSolver' : 'CPLEX',
#}

#mibsParamsInputs['default+WS'] = {
#    'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#    'MibS_warmStartLL': '1',
#    'MibS_whichCutsLL': '0',
#}

# mibsParamsInputs['default-frac'] = {
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
# }

#mibsParamsInputs['noGood+type1+pureInteger'] = {
#    'MibS_turnOffOtherCuts': '1',
#    'MibS_useGeneralNoGoodCut':'1',
#    'MibS_useTypeIC': '1',
#    'MibS_bilevelFreeSetTypeIC': '0',     # 0: Intersection Cut Type I; 1: Intersection Cut Type II; only valid when use inters#ectionCutTypeIC
#    'MibS_usePureIntegerCut':'1',
#    'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#    'MibS_solveSecondLevelWhenLVarsInt': '1',
#}

# mibsParamsInputs['watermelon+type1+incObj-frac'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useIncObjCut':'1',
#     'MibS_useTypeWatermelon': '1',
#     'MibS_useTypeIC': '1',
#     'MibS_bilevelFreeSetTypeIC': '0',     # 0: Intersection Cut Type I; 1: Intersection Cut Type II; only valid when use intersectionCutTypeIC
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '0',
# }

# mibsParamsInputs['watermelon+type1+incObj-frac-LV'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useIncObjCut':'1',
#     'MibS_useTypeWatermelon': '1',
#     'MibS_useTypeIC': '1',
#     'MibS_bilevelFreeSetTypeIC': '0',     # 0: Intersection Cut Type I; 1: Intersection Cut Type II; only valid when use intersectionCutTypeIC
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '1',
# }

# mibsParamsInputs['watermelon+type1-frac'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useTypeWatermelon': '1',
#     'MibS_useTypeIC': '1',
#     'MibS_bilevelFreeSetTypeIC': '0',     # 0: Intersection Cut Type I; 1: Intersection Cut Type II; only valid when use intersectionCutTypeIC
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '0',
# }

# mibsParamsInputs['watermelon+type1-frac-LV'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useTypeWatermelon': '1',
#     'MibS_useTypeIC': '1',
#     'MibS_bilevelFreeSetTypeIC': '0',     # 0: Intersection Cut Type I; 1: Intersection Cut Type II; only valid when use intersectionCutTypeIC
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '1',
# }

# mibsParamsInputs['benders'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useBendersCut':'1',
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '1',
# }

# mibsParamsInputs['benders-frac'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useBendersCut':'1',
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
# }

# mibsParamsInputs['benders+fracidic'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useBendersCut':'1',
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_useImprovingDirectionIC': '1',
#     'MibS_useFractionalCuts': '1',
# }

# mibsParamsInputs['benders+fracidic-frac'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useBendersCut':'1',
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     'MibS_useImprovingDirectionIC': '1',
#     'MibS_useFractionalCuts': '1',
# }

# mibsParamsInputs['benders+idic'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useBendersCut':'1',
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_useImprovingDirectionIC': '1',
#     'MibS_useFractionalCuts': '0',
# }

# mibsParamsInputs['benders+idic-frac'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useBendersCut':'1',
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     'MibS_useImprovingDirectionIC': '1',
#     'MibS_useFractionalCuts': '0',
# }

# mibsParamsInputs['benders-cplex'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useBendersCut':'1',
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '1',
#     'MibS_feasCheckSolver' : 'CPLEX'
# }

# mibsParamsInputs['benders-frac-cplex'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useBendersCut':'1',
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     'MibS_feasCheckSolver' : 'CPLEX'
# }

# mibsParamsInputs['incObj'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useIncObjCut':'1',
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '1',
# }

# mibsParamsInputs['incObj-frac'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useIncObjCut':'1',
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '0',
# }

# mibsParamsInputs['genNoGood'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useGeneralNoGoodCut':'1',
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '1',           # 0: fractional, 1: linking
# }

# mibsParamsInputs['genNoGood-frac'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useGeneralNoGoodCut':'1',
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
# }

# mibsParamsInputs['watermelon'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useTypeWatermelon': '1',
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
# }

# mibsParamsInputs['watermelon-frac'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useTypeWatermelon': '1',
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
# }

# mibsParamsInputs['watermelon-frac-LV'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useTypeWatermelon': '1',
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '1',           # 0: fractional, 1: linking
# }

# mibsParamsInputs['fracWatermelon'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useTypeWatermelon': '1',
#     'MibS_useFractionalCuts': '1',
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
# }

# mibsParamsInputs['fracIDIC'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useImprovingDirectionIC': '1',
#     'MibS_useFractionalCuts': '1',
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
# }

# mibsParamsInputs['IDIC'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useImprovingDirectionIC': '1',
#     'MibS_useFractionalCuts': '0',
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
# }

#mibsParamsInputs['IDIC-frac'] = {
#    'MibS_turnOffOtherCuts': '1',
#    'MibS_useImprovingDirectionIC': '1',
#    'MibS_useFractionalCuts': '0',
#    'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#    'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
#}

# mibsParamsInputs['IDIC+MIP-frac'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useImprovingDirectionIC': '1',
#     'MibS_useFractionalCuts': '0',
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
#     'MibS_blisCutStrategy': '2'
# }

# mibsParamsInputs['fracIDIC'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useImprovingDirectionIC': '1',
#     'MibS_useFractionalCuts': '1',
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
# }

#mibsParamsInputs['fracIDIC-frac'] = {
#    'MibS_turnOffOtherCuts': '1',
#    'MibS_useImprovingDirectionIC': '1',
#    'MibS_useFractionalCuts': '1',
#    'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#    'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
#}

# mibsParamsInputs['fracIDIC+MIP-frac'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useImprovingDirectionIC': '1',
#     'MibS_useFractionalCuts': '1',
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
#     'MibS_blisCutStrategy': '2'
# }

# mibsParamsInputs['fracWatermelon-frac'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useTypeWatermelon': '1',
#     'MibS_useFractionalCuts': '1',
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
# }

# mibsParamsInputs['fracWatermelon-frac-cplex'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useTypeWatermelon': '1',
#     'MibS_useFractionalCuts': '1',
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
#     'MibS_feasCheckSolver' : 'CPLEX'
# }

# mibsParamsInputs['fracWatermelon-frac-cplex-d10'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useTypeWatermelon': '1',
#     'MibS_useFractionalCuts': '1',
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
#     'MibS_feasCheckSolver' : 'CPLEX',
#     'MibS_maxCutDepth' : '10'
# }

# mibsParamsInputs['fracWatermelon-frac-cplex-d20'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useTypeWatermelon': '1',
#     'MibS_useFractionalCuts': '1',
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
#     'MibS_feasCheckSolver' : 'CPLEX',
#     'MibS_maxCutDepth' : '20'
# }

# mibsParamsInputs['type1'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useTypeIC': '1',
#     'MibS_bilevelFreeSetTypeIC': '0',     # 0: Intersection Cut Type I; 1: Intersection Cut Type II; only valid when use intersectionCutTypeIC
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '1',           # 0: fractional, 1: linking
# }

# mibsParamsInputs['ISICType1'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useImprovingSolutionIC': '1',
#     'MibS_bilevelFreeSetTypeISIC': '0',     # 0: Intersection Cut Type I; 1: Intersection Cut Type II; only valid when use intersectionCutTypeIC
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '1',           # 0: fractional, 1: linking
# }

# mibsParamsInputs['type1-WS'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useTypeIC': '1',
#     'MibS_bilevelFreeSetTypeIC': '0',     # 0: Intersection Cut Type I; 1: Intersection Cut Type II; only valid when use intersectionCutTypeIC
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '1',           # 0: fractional, 1: linking
#     'MibS_warmStartLL': '1'
# }

# mibsParamsInputs['type1-cplex'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useTypeIC': '1',
#     'MibS_bilevelFreeSetTypeIC': '0',     # 0: Intersection Cut Type I; 1: Intersection Cut Type II; only valid when use intersectionCutTypeIC
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '1',           # 0: fractional, 1: linking
#     'MibS_feasCheckSolver' : 'CPLEX'
# }

# mibsParamsInputs['fracType1-frac-cplex'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useTypeIC': '1',
#     'MibS_bilevelFreeSetTypeIC': '0',     # 0: Intersection Cut Type I; 1: Intersection Cut Type II; only valid when use intersectionCutTypeIC
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelEveryIteration': '1',           # 0: fractional, 1: linking
#     'MibS_feasCheckSolver' : 'CPLEX'
# }

# mibsParamsInputs['fracType1-frac-cplex-d10'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useTypeIC': '1',
#     'MibS_bilevelFreeSetTypeIC': '0',     # 0: Intersection Cut Type I; 1: Intersection Cut Type II; only valid when use intersectionCutTypeIC
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelEveryIteration': '1',           # 0: fractional, 1: linking
#     'MibS_feasCheckSolver' : 'CPLEX',
#     'MibS_maxCutDepth' : '10'
# }

# mibsParamsInputs['fracType1-frac-cplex-d20'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useTypeIC': '1',
#     'MibS_bilevelFreeSetTypeIC': '0',     # 0: Intersection Cut Type I; 1: Intersection Cut Type II; only valid when use intersectionCutTypeIC
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelEveryIteration': '1',           # 0: fractional, 1: linking
#     'MibS_feasCheckSolver' : 'CPLEX',
#     'MibS_maxCutDepth' : '20'
# }

# mibsParamsInputs['type1-frac'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useTypeIC': '1',
#     'MibS_bilevelFreeSetTypeIC': '0',     # 0: Intersection Cut Type I; 1: Intersection Cut Type II; only valid when use intersectionCutTypeIC
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
# }

# mibsParamsInputs['type2'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useTypeIC': '1',
#     'MibS_bilevelFreeSetTypeIC': '1',     # 0: Intersection Cut Type I; 1: Intersection Cut Type II; only valid when use intersectionCutTypeIC
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
# }

# mibsParamsInputs['fracISICType2'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useImprovingSolutionIC': '1',
#     'MibS_bilevelFreeSetTypeISIC': '1',     # 0: Intersection Cut Type I; 1: Intersection Cut Type II; only valid when use intersectionCutTypeIC
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     #'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
# }

# mibsParamsInputs['ISICType2'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useImprovingSolutionIC': '1',
#     'MibS_bilevelFreeSetTypeISIC': '1',     # 0: Intersection Cut Type I; 1: Intersection Cut Type II; only valid when use intersectionCutTypeIC
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_useFractionalCuts': '0',
#     #'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
# }

# mibsParamsInputs['type2-frac'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useTypeIC': '1',
#     'MibS_bilevelFreeSetTypeIC': '1',     # 0: Intersection Cut Type I; 1: Intersection Cut Type II; only valid when use intersectionCutTypeIC
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
# }

# mibsParamsInputs['fracISICType2-frac'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useImprovingSolutionIC': '1',
#     'MibS_bilevelFreeSetTypeISIC': '1',     # 0: Intersection Cut Type I; 1: Intersection Cut Type II; only valid when use intersectionCutTypeIC
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     #'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
# }

# mibsParamsInputs['ISICType2-frac'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useImprovingSolutionIC': '1',
#     'MibS_bilevelFreeSetTypeISIC': '1',     # 0: Intersection Cut Type I; 1: Intersection Cut Type II; only valid when use intersectionCutTypeIC
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     'MibS_useFractionalCuts': '0',
#     #'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
# }

# mibsParamsInputs['hyper'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useTypeHypercubeIC': '1',
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '1',           # 0: fractional, 1: linking
# }

# mibsParamsInputs['hyper-frac'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useTypeHypercubeIC': '1',
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
# }

# mibsParamsInputs['intNoGood'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_useIntNoGood':'1',
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
# }

#mibsParamsInputs['pureInteger'] = {
#    'MibS_turnOffOtherCuts': '1',
#    'MibS_usePureIntegerCut':'1',
#    'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#    'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
#}

# mibsParamsInputs['pureInteger-frac'] = {
#     'MibS_turnOffOtherCuts': '1',
#     'MibS_usePureIntegerCut':'1',
#     'MibS_branchStrategy': '0',           # 0: fractional, 1: linking
#     'MibS_solveSecondLevelWhenLVarsInt': '0',           # 0: fractional, 1: linking
# }

# mibsParamsInputs['noCut'] = {
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_cutStrategy': '0'
# }

# mibsParamsInputs['noCut-cplex'] = {
#      'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#      'MibS_cutStrategy': '0',
#      'MibS_feasCheckSolver' : 'CPLEX',
# }

# mibsParamsInputs['noCut-WS'] = {
#     'MibS_branchStrategy': '1',           # 0: fractional, 1: linking
#     'MibS_cutStrategy': '0',
#     'MibS_warmStartLL': '1'
# }

