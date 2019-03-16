""" Lab 2 """

import numpy as np
import matplotlib.pyplot as plt

import cmc_pylog as pylog
from cmcpack import integrate, DEFAULT, parse_args

from ex3_pendulum import PendulumParameters, pendulum_system


DEFAULT["label"] = [r"$\theta$ [rad]", r"$d\theta/dt$ [rad/s]"]


def exercise3(clargs):
    """ Exercise 3 """
    parameters = PendulumParameters()  # Checkout pendulum.py for more info
    pylog.info(parameters)
    # Simulation parameters
    time = np.arange(0, 30, 0.01)  # Simulation time
    x0 = [1, 0.0]  # Initial state

    # To use/modify pendulum parameters (See PendulumParameters documentation):
    # parameters.g = 9.81  # Gravity constant
    # parameters.m = 1.  # Mass
    # parameters.L = 1.  # Length
    # parameters.I = 1. # Inertia (Automatically computed!)
    # parameters.d = 0.3  # damping
    # parameters.sin = np.sin  # Sine function
    # parameters.dry = False  # Use dry friction (True or False)

    # ---------------------------------------------------------------------------
    # "Evolution of pendulum in normal conditions must be implemented"
    # ---------------------------------------------------------------------------
    res = integrate(pendulum_system, x0, time, args=(parameters,))
    res.plot_state("State - normal")
    res.plot_phase("Phase - normal")

    # ---------------------------------------------------------------------------
    # "Evolution of pendulum without damping must be implemented"
    # ---------------------------------------------------------------------------
    res = integrate(pendulum_system, x0, time, args=(PendulumParameters(d=0),))
    res.plot_state("State - d=0")
    res.plot_phase("Phase - d=0")

    # ---------------------------------------------------------------------------
    # "Evolution of pendulum with perturbations must be implemented"
    # ---------------------------------------------------------------------------
    res = integrate(pendulum_system, x0, time, args=(PendulumParameters(), -2.0))
    res.plot_state("State - torque")
    res.plot_phase("Phase - torque")

    # ---------------------------------------------------------------------------
    # "Evolution of pendulum with dry friction must be implemented"
    # ---------------------------------------------------------------------------
    res = integrate(pendulum_system, x0, time, args=(PendulumParameters(dry=True), 0.0))
    res.plot_state("State - dry")
    res.plot_phase("Phase - dry")

    # Show plots of all results
    if not clargs.save_figures:
        plt.show()


if __name__ == "__main__":
    CLARGS = parse_args()
    exercise3(CLARGS)

