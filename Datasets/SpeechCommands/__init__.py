from Demos.Datasets import tmp_dir
import os

data_folder = "SpeechCommands"
data_dir = os.path.join(tmp_dir, data_folder)


def GetData():

    from Demos.Datasets.SpeechCommands.kws_util import parse_command
    from Demos.Datasets.SpeechCommands.get_dataset import get_training_data

    Flags, unparsed = parse_command()
    Flags.data_dir = data_dir

    ds_train, ds_test, ds_val = get_training_data(Flags)

    ds_train = ds_train.repeat()
    ds_test = ds_test.repeat()

    train_len = 85511
    validation_len = 10102
    test_len = 4890

    import tensorflow as tf

    shape = tuple(tf.compat.v1.data.get_output_shapes(ds_train)[0].as_list()[1:])

    return {
        "train_generator": ds_train,
        "train_len": train_len,
        "validation_generator": ds_val,
        "validation_len": validation_len,
        "test_generator": ds_test,
        "test_len": test_len,
        "input_tensor_shape": shape,
    }


def GetInputShape():

    return (49, 10, 1)
