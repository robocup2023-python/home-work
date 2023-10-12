#day7test2的封装并添加提示
def day2test02():
    import random
    import string
    import shutil
    import typing
    #int,str不需要调用typing模块（在day7中貌似没有找到需要调用list等类型的部分）

    def generate_random_string(length: int) -> str:
        character = string.printable.strip()
        return " ".join(random.choice(character) for _ in range(length))

    def create_random_file(file_name: str, num_lines: int) -> None:
        with open(file_name, "w") as file:
            for _ in range(num_lines):
                file.write(generate_random_string(random.randint(1, 100)) + "\n")

    def copy_file(old_file: str, new_file: str) -> None:
        shutil.copy(old_file, new_file)

    if __name__ == "__main__":
        l = int(input("l=:"))
        create_random_file("test.txt", l)
        copy_file("test.txt", "copy_test.txt")
