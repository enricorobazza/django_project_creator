import os
from pathlib import Path
import yaml

from django.shortcuts import render, redirect
from main.forms.settings import SettingsForm

from core.settings import BASE_DIR, DESTINATION_URL, COOKIECUTTER_PROJECT

class IndexView():
    def index(request):
        if request.method == "POST":
            form = SettingsForm(request.POST)
            if form.is_valid:
                settings = form.save(commit=False)
                config_path = os.path.join(BASE_DIR, "cookiecutter.yaml")
                dict_file = {
                    'default_context': settings.as_dict(),
                }
                with open(config_path, 'w') as file:
                    yaml.dump(dict_file, file)
                os.system("cookiecutter --config-file %s %s --no-input -o %s"%(
                    config_path,
                    COOKIECUTTER_PROJECT, 
                    DESTINATION_URL)
                )
                print("Project created!!")
                return redirect('index')

            else:
                return render(request, 'index/index.html', {'form': form})
        form = SettingsForm()
        return render(request, 'index/index.html', {'form': form})