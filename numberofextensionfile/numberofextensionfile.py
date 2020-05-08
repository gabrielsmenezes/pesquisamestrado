from utils import remove_next_line, output_write, find_paths


def create_extension_files():
    return {
        "*.java": "",
        "*.properties": "",
        "*.jar": "",
        "*build.gradle": "",
        "*pom.xml": "",
        "*manifest.xml": "",
        "*.xml": "",
        "*.bat": "",
        "*.md": "",
        "*.adoc": "",
        "*README.*": "",
        "*.yaml": "",
        "*.txt": "",
        "*.sh": "",
        "*travis.yml": "",
        "*.yml": "",
        "*.cmd": "",
        "*.kt": "",
        "*.json": "",
        "*": ""
    }


def concat_output(extensions):
    output = ""
    for extension in extensions:
        output = output + str(extensions[extension]) + ","
    return output


def count_others(extensions):
    return extensions["*"] - extensions["*.java"] - extensions["*.properties"] - extensions["*.jar"] - extensions["*build.gradle"] - extensions["*.xml"] - extensions["*.bat"] - extensions["*.md"] - extensions["*.adoc"] - extensions["*.yaml"] - extensions["*.txt"] - extensions["*.sh"] - extensions["*.yml"] - extensions["*.cmd"] - extensions["*.kt"] - extensions["*.json"]


def count_extension_files(extensions, sample):
    for extension in extensions:
        extensions[extension] = len(
            find_paths(extension, "/home/gabriel.menezes/Documentos/gabriel/pesquisamestrado/repositories/" + sample))


def numberofextensionfile(framework, projects):
    extensions = create_extension_files()
    measure = "numberofextensionfile"
    output_write(framework, measure,
                 'framework,project,java,properties,jar,build.gradle,pom.xml,manifest.xml,xml,bat,md,adoc,README,yaml,txt,sh,travis.yml,yml,cmd,kt,json,numberOfFiles,others',
                 True)
    with open(projects) as samples:
        for sample in samples:
            sample = remove_next_line(sample)
            count_extension_files(extensions, sample)
            others = count_others(extensions)
            output = concat_output(extensions) + str(others)
            output_write(framework, measure, framework+","+sample+","+output, False)
