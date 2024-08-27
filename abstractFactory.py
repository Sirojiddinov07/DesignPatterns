from abc import ABC, abstractmethod

# Abstract Product A
class Button(ABC):
    @abstractmethod
    def click(self):
        pass

# Abstract Product B
class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass
# Concrete Product A1
class WindowsButton(Button):
    def click(self):
        print("Windows Button clicked!")

# Concrete Product B1
class WindowsCheckbox(Checkbox):
    def check(self):
        print("Windows Checkbox checked!")

# Concrete Product A2
class MacOSButton(Button):
    def click(self):
        print("MacOS Button clicked!")

# Concrete Product B2
class MacOSCheckbox(Checkbox):
    def check(self):
        print("MacOS Checkbox checked!")


# Abstract Factory
class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


# Concrete Factory 1
class WindowsFactory(UIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

# Concrete Factory 2
class MacOSFactory(UIFactory):
    def create_button(self) -> Button:
        return MacOSButton()

    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()


def client_code(factory: UIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.click()
    checkbox.check()


# Example Usage
if __name__ == "__main__":
    print("Client: Testing client code with WindowsFactory")
    client_code(WindowsFactory())

    print("\nClient: Testing client code with MacOSFactory")
    client_code(MacOSFactory())
