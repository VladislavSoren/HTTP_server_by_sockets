import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', type=str, help='Возвращать файлы по произвольному пути в DOCUMENT_ROOT',
                        default='/home/soren/PycharmProjects/HTTP_Server')
    parser.add_argument(
        '-w', type=int, help='Числов worker\'ов задается аргументом ĸомандной строĸи -w', default=1)
    return parser.parse_args()


parser = parse_arguments()
DOCUMENT_ROOT = parser.r
WORKERS = parser.w
