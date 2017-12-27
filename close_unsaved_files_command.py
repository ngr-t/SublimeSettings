import os
import sublime_plugin


class CloseUnsavedFilesCommand(sublime_plugin.WindowCommand):
    def run(self):
        window = self.window
        for v in window.views():
            file_name = v.file_name()
            if file_name and not os.path.exists(file_name):
                print("Close: '{0}'".format(file_name))
                v.set_scratch(True)
                window.focus_view(v)
                window.run_command("close")
