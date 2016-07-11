from importlib import import_module

from django.conf import settings


class ModelAdmin(object):
    djadmin3_enabled = True

    # def __init__(self):
    #      self.model =self.model
    #
    # def __str__(self):
    #     return self.model


class AppStore(object):
    def __init__(self, module):
        self.models = []
        print("AppStore: " + str(module))
        print(module.__dict__.keys())
        for key in module.__dict__.keys():
            model_candidate = getattr(module, key)
            if hasattr(model_candidate, 'djadmin3_enabled') and hasattr(model_candidate, 'model'):
                print("model_candidate: " + str(model_candidate))
                self.add_model(model_candidate)

    def add_model(self, model):
        model.name = model.__name__
        self.models.append(model)

        print(self.models)


def get_admin3s():
    """ Returns a list of all admin3 implementations for the site """
    apps = []
    for app_name in [x for x in settings.INSTALLED_APPS if x != 'djadmin3']:
        name = "{0}.admin3".format(app_name)
        print(name)
        try:
            module = import_module(name)
        except ImportError as e:
            print(str(e))
            if str(e).startswith("No module named"):
                continue
            raise e

        app_store = AppStore(module)
        apps.append(dict(
            app_name=app_name,
            obj=app_store
        ))
    return apps
