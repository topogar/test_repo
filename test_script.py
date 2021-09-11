import argparse


def make_nn(num_layers):
    return [1 for _ in range(num_layers)]


def add_relu(nn):
    nn.append('relu')
    return nn


if __name__ == "__main__":
    args_parser = argparse.ArgumentParser(
        description="Тестовый скрипт"
    )

    args_parser.add_argument("--numlayers", required=True, type=int)
    args_parser.add_argument("--userelu", action='store_true', default=False)

    # args = {'numlayers': ..., 'userelu': ...}
    args = vars(args_parser.parse_args())

    nn = make_nn(args['numlayers'])

    if args['userelu']:
        nn = add_relu(nn)

    print(nn)