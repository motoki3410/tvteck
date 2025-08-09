from parameter.parameter_manager import ParameterManager
import argparse


def show_parameters():
    param_manager = ParameterManager()
    param_manager.show_field_name()


def main():
    show_parameters()


if __name__ == "__main__":
    main()
