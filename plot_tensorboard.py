import matplotlib.pyplot as plt
from tensorboard.backend.event_processing.event_accumulator import EventAccumulator

tag_name = "psnr"
path_to_folder = "./opt/ckpt/mva_logo_small/"
tf_event_file = (
    path_to_folder + "events.out.tfevents.1701873353.LAPTOP-NJJEBVVK.14212.0"
)


def extract_curve_from_tensorboard(logdir, tag):
    event_acc = EventAccumulator(logdir)
    event_acc.Reload()

    # Extracting data for the specified tag
    data = event_acc.scalars.Items(tag)

    steps = [event.step for event in data]
    values = [event.value for event in data]

    return steps, values


value_list = extract_curve_from_tensorboard(tf_event_file, tag_name)
print(value_list)
plt.plot(value_list[0], value_list[1])
plt.title("Evolution of the PSNR depending on the number of training iterations")
plt.xlabel("Number of iteration")
plt.ylabel("PSNR")
plt.savefig(path_to_folder + tag_name + ".png")
