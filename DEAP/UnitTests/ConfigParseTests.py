"""=========================Parsing========================="""
import argparse

from Demos.DEAP import (
     get_config,
    )

parser = argparse.ArgumentParser()

parser.add_argument(
    "--folder",
    help="Absolute path to folder where interrupted test's output is stored",
    default=None,
)
parser.add_argument(
    "--gen", help="Generation from which the test should resume", type=int
)

parser.add_argument(
    "--config",
    help="Location of config file to be used, default is to use first found config file in current working directory, then parent directories",
    type=str,
    default=None,
)

args = parser.parse_args()

config = get_config(args=args)

"""=================================================="""

from TestingTools import Compare

from TensorNAS.Tools.ConfigParse import (
    _GenVector,
_GetVariableGoal,
_GetGoalParamVectorStart,
_GetGoalParamVectorEnd,
_GetGoalAccVectorStart,
_GetGoalAccVectorEnd,
_GetGoal3DVectorStart,
_GetGoal3DVectorEnd,
_GetGoalVectorSteps,
_GetNormalizationPlane,
_GetNormalizationParamVectorStart,
_GetNormalizationParamVectorEnd,
_GetNormalizationAccVectorStart,
_GetNormalizationAccVectorEnd,
_GetNormalizationVectorSteps,
_GetGoalVector,
_GenVectorsVariableNormilization
)

def _Gen3DVariableVectors(p1_start, p1_stop, p2_start, p2_stop, p3_start, p3_stop, steps):

    v1 = _GenVector(p1_start, p1_stop, steps)
    v2 = _GenVector(p2_start, p2_stop, steps)
    v3 = _GenVector(p3_start, p3_stop, steps)

    return list(zip(v1, v2, v3))

def _Gen3DVectorsVariableGoal(
    g_param_start, g_param_stop, g_acc_start, g_acc_stop, g_3D_start, g_3D_stop, steps, n1, n2, n3
):

    goal_vectors = _Gen3DVariableVectors(
        g_param_start, g_param_stop, g_acc_start, g_acc_stop, g_3D_start, g_3D_stop, steps
    )

    normalization_plane = [(n1, n2, n3) for _ in range(len(goal_vectors))]

    return goal_vectors, normalization_plane

def Get3DFilterFunctionArgs(config):

    if _GetVariableGoal(config):
        # Goal vector varies, normilization vector is static
        g_param_start = _GetGoalParamVectorStart(config)
        if(not Compare(3000, g_param_start)):
            print("failed to get g_param_start")
            print("expected:{} but got: {}".format(1,g_param_start))
        g_param_stop = _GetGoalParamVectorEnd(config)
        if (not Compare(3000, g_param_stop)):
            print("failed to get g_param_stop")
            print("expected:{} but got: {}".format(1, g_param_stop))
        g_acc_start = _GetGoalAccVectorStart(config)
        if (not Compare(90, g_acc_start)):
            print("failed to get g_acc_start")
            print("expected:{} but got: {}".format(1, g_acc_start))
        g_acc_stop = _GetGoalAccVectorEnd(config)
        if (not Compare(90, g_acc_stop)):
            print("failed to get g_acc_stop")
            print("expected:{} but got: {}".format(1, g_acc_stop))
        g_3D_start = _GetGoal3DVectorStart(config)
        if (not Compare(9, g_3D_start)):
            print("failed to get g_3D_start")
            print("expected:{} but got: {}".format(1, g_3D_start))
        g_3D_stop = _GetGoal3DVectorEnd(config)
        if (not Compare(9, g_3D_stop)):
            print("failed to get g_3D_stop")
            print("expected:{} but got: {}".format(1, g_3D_stop))
        steps = _GetGoalVectorSteps(config)
        if (not Compare(1, steps)):
            print("failed to get steps")
            print("expected:{} but got: {}".format(1, steps))
        n1, n2, n3 = _GetNormalizationPlane(config)
        if (not Compare(500, n1)):
            print("failed to get n1")
            print("expected:{} but got: {}".format(1, n1))
        if (not Compare(1, n2)):
            print("failed to get n2")
            print("expected:{} but got: {}".format(1, n2))
        if (not Compare(0.1, n3)):
            print("failed to get n3")
            print("expected:{} but got: {}".format(1, n3))

        return _Gen3DVectorsVariableGoal(
            g_param_start, g_param_stop, g_acc_start, g_acc_stop,  g_3D_start,  g_3D_stop, steps, n1, n2, n3
        )
    else:
        print("Goal is not variable!")
""""==================================MAIN=================================="""

print(Get3DFilterFunctionArgs(config))