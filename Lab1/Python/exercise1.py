""" Lab 1 - Exercise 1 """

from ex1_functions import function, function_rk, analytic_function
from ex1_integration import (
    example_integrate,
    euler_integrate,
    ode_integrate,
    ode_integrate_rk,
    plot_integration_methods
)
from ex1_errors import compute_error, error

import numpy as np
import matplotlib.pyplot as plt

import cmc_pylog as pylog
from cmcpack import Result


def display_error(errors, method):
    err = error(errors, n=1)
    err_max = error(errors)

    pylog.debug(
        "Obtained an error of {} using {} method (max={}, len={})".format(
            err, method, err_max, len(method)
        )
    )


def exercise1(clargs):
    """ Exercise 1 """
    # Setup
    pylog.info("Running exercise 1")

    # Setup
    time_max = 5  # Maximum simulation time
    time_step = 0.2  # Time step for ODE integration in simulation
    x0 = np.array([1.])  # Initial state

    # Integration methods (Exercises 1.a - 1.d)
    pylog.info("Running function integration using different methods")

    # Example
    pylog.debug("Running example plot for integration (remove)")
    example = example_integrate(x0, time_max, time_step)
    example.plot_state(figure="Example", label="Example", marker=".")

    # Analytical (1.a)
    time = np.arange(0, time_max, time_step)  # Time vector
    x_a = analytic_function(time)
    analytical = Result(x_a, time) if x_a is not None else None

    # Euler (1.b)
    euler = euler_integrate(function, x0, time_max, time_step)
    display_error(euler.state - analytical.state, "Euler")

    # ODE (1.c)
    ode = ode_integrate(function, x0, time_max, time_step)
    display_error(ode.state - analytical.state, "LSODA")

    # ODE Runge-Kutta (1.c)
    ode_rk = ode_integrate_rk(function_rk, x0, time_max, time_step)
    display_error(ode_rk.state - analytical.state, "Runge-Kutta")

    # Euler with lower time step (1.d)
    euler_time_step = 0.05
    euler_ts_small = (
        euler_integrate(function, x0, time_max, euler_time_step)
        if euler_time_step is not None
        else None
    )

    # New analytical time step
    time_step_small = 0.05
    time_small = np.arange(0, time_max, time_step_small)  # Time vector
    x_a_small = analytic_function(time_small)
    analytical_small = Result(x_a_small, time_small) if x_a_small is not None else None

    display_error(euler_ts_small.state - analytical_small.state, "Euler small")

    # Plot integration results
    plot_integration_methods(
        analytical=analytical_small, euler=euler,
        ode=ode, ode_rk=ode_rk, euler_ts_small=euler_ts_small,
        euler_timestep=time_step_small, euler_timestep_small=euler_time_step
    )

    # Error analysis (Exercise 1.e)
    pylog.warning("Error analysis must be implemented")
    dt_list = np.logspace(-3, 0, 20)  # List of timesteps (powers of 10)
    integration_errors = [["L1", 1], ["L2", 2], ["Linf", 0]]
    methods = [
        ["Euler", euler_integrate, function],
        ["Lsoda", ode_integrate, function],
        ["RK", ode_integrate_rk, function_rk]
    ]
    for error_name, error_index in integration_errors:
        for name, integration_function, f in methods:
            compute_error(
                f, analytic_function, integration_function, x0, dt_list,
                time_max=time_max,
                figure=error_name,
                label=name,
                n=error_index
            )

    # Show plots of all results
    if not clargs.save_figures:
        plt.show()
    return


if __name__ == "__main__":
    from cmcpack import parse_args
    CLARGS = parse_args()
    exercise1(CLARGS)

