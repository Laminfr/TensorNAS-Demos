if __name__ == "__main__":

    import argparse

    from Demos import (
        load_3Dglobals_from_config,
        load_tensorflow_params_from_config,
        get_global,
    )
    from Demos.DEAP import (
        load_genetic_params_from_config,
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

    load_3Dglobals_from_config(config)
    load_genetic_params_from_config(config)
    load_tensorflow_params_from_config(config)

    dataset_module = get_global("dataset_module")


    print(get_global("filter_function_args"))

    print("Done")
