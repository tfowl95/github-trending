import argparse

def cli_arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--duration',
        choices = ['day', 'week', 'month', 'year'],
        default = 'week',
        help="Specifies the time period (day, week, month, year). Default is week."
        )
    parser.add_argument(
        '--limit',
        type = int,
        default = 10,
        help="Specifies the number of repos to return. Default is 10."
        )
    return parser.parse_args()