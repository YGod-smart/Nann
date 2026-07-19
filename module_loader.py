import os
import importlib

class ModuleLoader:

    def __init__(self):
        self.modules = {}

    def load_modules(self):

        files = os.listdir("modules")

        for file in files:

            if file.endswith(".py") and not file.startswith("_"):

                module_name = file[:-3]

                module = importlib.import_module(
                    f"modules.{module_name}"
                )

                class_name = module_name.capitalize()

                module_class = getattr(module, class_name)

                module_object = module_class()

                self.modules[module_name] = module_object

                print(f"Loaded: {module_name}")

        return self.modules