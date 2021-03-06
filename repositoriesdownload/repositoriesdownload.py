import os
from git import Repo

from utils import get_samples


def download(git_url, repo_dir, sample):
    Repo.clone_from(git_url, repo_dir + sample)


def create_url_from_github(sample):
    return "https://github.com/" + sample + ".git"


def remove_especial_caracters(sample):
    return sample.replace('\n', '')


def repositoriesdownload(framework, projects):
    print('framework: ' + framework)
    samples = get_samples(projects)
    for sample in samples:
        sample = remove_especial_caracters(sample)
        git_url = create_url_from_github(sample)
        print("Downloading %s" % sample)
        repo_dir = "repositories/"
        isdir = os.path.isdir(repo_dir+sample)
        if isdir:
            print("Project " + sample + " downloaded")
            continue
        download(git_url, repo_dir, sample)
        print("%s downloaded" % sample)
