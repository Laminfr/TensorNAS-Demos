import argparse

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

args.config = "DemoMNISTEASimple"

if __name__ == "__main__":

    from TensorNAS.Demos import (
        load_globals_from_config,
        load_tensorflow_params_from_config,
        set_test_train_data,
        get_global,
        evaluate_individual,
        mutate_individual,
    )
    from TensorNAS.Demos.DEAP import (
        load_genetic_params_from_config,
        run_deap_test,
        get_config,
    )
    from TensorNAS.Demos.Datasets.MNIST import GetData
    from TensorNAS.Core.Crossover import crossover_individuals_sp

    config = get_config(args=args)

    load_globals_from_config(config)
    load_genetic_params_from_config(config)
    load_tensorflow_params_from_config(config)

    images_test, images_train, labels_test, labels_train, input_tensor_shape = GetData()

    set_test_train_data(
        train_data=images_train,
        train_labels=labels_train,
        test_data=images_test,
        test_labels=labels_test,
        input_tensor_shape=input_tensor_shape,
        training_sample_size=get_global("training_sample_size"),
        test_sample_size=get_global("test_sample_size"),
    )

    from TensorNAS.Demos import gen_classification_ba

    pop, logbook, test = run_deap_test(
        generate_individual=gen_classification_ba,
        evaluate_individual=evaluate_individual,
        crossover=crossover_individuals_sp,
        mutate=mutate_individual,
    )

    print("Done")
