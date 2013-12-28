import sublime, sublime_plugin

# Prints the scope name of the first character in the selection
class NameScopeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        region = view.sel()[0]
        print(view.scope_name(region.begin()))
        view.sel().clear()
        view.sel().add(view.extract_scope(region.begin()))

# Runs scope selector and adds to selection
class FindScopeCommand(sublime_plugin.TextCommand):
    def run(self, edit, scope):
        self.view.sel().clear()
        regions = self.view.find_by_selector(scope)
        self.view.sel().add_all(regions)

class NextFunctionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        start = self.view.sel()[0].begin()
        regions = self.view.find_by_selector("entity.name.function")
        for region in regions:
            if region.end() > start and region != self.view.sel()[0]:
                self.view.sel().clear()
                self.view.sel().add(region)
                self.view.show(region)
                break

class PrevFunctionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        start = self.view.sel()[0].begin()
        regions = self.view.find_by_selector("entity.name.function")
        for region in reversed(regions):
            if region.begin() < start and region != self.view.sel()[0]:
                self.view.sel().clear()
                self.view.sel().add(region)
                self.view.show(region)
                break