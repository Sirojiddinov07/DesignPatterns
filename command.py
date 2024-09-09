from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class TextEditor:
    def __init__(self):
        self.text = ""

    def add_text(self, new_text):
        self.text += new_text
        print(f"Text after adding: {self.text}")

    def remove_text(self, count):
        self.text = self.text[:-count]
        print(f"Text after removing: {self.text}")


class AddTextCommand(Command):
    def __init__(self, editor, text):
        self.editor = editor
        self.text = text

    def execute(self):
        self.editor.add_text(self.text)

    def undo(self):
        self.editor.remove_text(len(self.text))


class CommandInvoker:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)

    def undo_command(self):
        if self.history:
            command = self.history.pop()
            command.undo()
        else:
            print("No commands to undo.")


if __name__ == "__main__":
    editor = TextEditor()
    invoker = CommandInvoker()

    command1 = AddTextCommand(editor, "Hello, ")
    invoker.execute_command(command1)

    command2 = AddTextCommand(editor, "world!")
    invoker.execute_command(command2)

    # Undo the last command (remove "world!")
    invoker.undo_command()

    # Undo the previous command (remove "Hello, ")
    invoker.undo_command()
