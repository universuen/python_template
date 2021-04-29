def set_print_style(style: int, text_color: int, background_color: int) -> None:
    print(f'\033[{style};{text_color};{background_color}m', end='')


def reset_print_style() -> None:
    print('\033[0;0m')
