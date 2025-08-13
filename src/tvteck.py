from parameter.parameter_manager import ParameterManager
import argparse


def show_parameters():
    param_manager = ParameterManager()
    # param_manager.show_field_names()
    # print(param_manager.get_field_names())
    print(param_manager.get_all_category_field_names())
    param_manager.set_all_parameters()
    param_manager.dump_parameter("device")


def main():
    parser = argparse.ArgumentParser(
        description="TVTeck Client Script"
    )
    parser.add_argument(
        "--show-params",
        action="store_true",
        help="Show available parameters and their field names",
    )
    args = parser.parse_args()

    if args.show_params:
        show_parameters()
