class custom_colors:
    def use_hex(self, hex_code: str):
        hex_code = hex_code.lstrip("#")  # Remove the "#" symbol if present
        rgb = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))  # Convert hex to RGB
        return f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m"

    def use_hex_bg(self, hex_code: str):
        hex_code = hex_code.lstrip("#")
        if len(hex_code) != 6:
            raise ValueError("Hex code must be 6 characters long (e.g., 'RRGGBB').")
        rgb = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
        return f"\033[48;2;{rgb[0]};{rgb[1]};{rgb[2]}m{self.use_hex('000000')}"

    def __init__(self):
        self.cream = "\033[38;2;255;245;151m"
        self.beige = "\033[38;2;245;245;220m"
        self.green = "\033[38;2;52;199;89m"
        self.red = self.use_hex("#d53410")
        self.yellow = self.use_hex("#eed204")
        self.esc = "\033[0m"
