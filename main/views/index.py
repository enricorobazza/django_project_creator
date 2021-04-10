import os
from pathlib import Path
import yaml

from django.shortcuts import render, redirect
from main.forms.settings import SettingsForm

from core.settings import BASE_DIR

class IndexView():
    def index(request):
        if request.method == "POST":
            form = SettingsForm(request.POST)
            if form.is_valid:
                settings = form.save(commit=False)
                django_apps_path = Path(BASE_DIR).resolve().parent
                config_path = os.path.join(BASE_DIR, "cookiecutter.yaml")
                dict_file = {
                    'default_context': settings.as_dict(),
                }
                with open(config_path, 'w') as file:
                    yaml.dump(dict_file, file)
                cookiecutter_path = os.path.join(django_apps_path, "cookie_cutter")
                os.system("cookiecutter --config-file %s %s --no-input -o %s"%(config_path,cookiecutter_path, django_apps_path))
                print("Project created!!")
                return redirect('index')

            else:
                return render(request, 'index/index.html', {'form': form})
        form = SettingsForm()
        return render(request, 'index/index.html', {'form': form})