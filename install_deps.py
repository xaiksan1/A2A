import subprocess
import sys

try:
    import toml
except ModuleNotFoundError:
    print("toml module not found. Assuming it's ok.")
    import toml

def install_dependencies(pyproject_path):
    try:
        with open(pyproject_path, 'r') as f:
            data = toml.load(f)
            
        if 'project' in data and 'dependencies' in data['project']:
           dependencies = data['project']['dependencies']
           dependencies.append('pytest')
           for dep in dependencies:
                try:
                   __import__(dep.split('==')[0])
                except ModuleNotFoundError:
                   print(f"Installing dependency: {dep}")
                   subprocess.check_call([sys.executable, '-m', 'pip', 'install', dep])
        else:
            print(f"'dependencies' not found in {pyproject_path}")
    except FileNotFoundError:
        print(f"Error: File not found at {pyproject_path}")
    except toml.TomlDecodeError:
        print(f"Error: Could not decode toml file at {pyproject_path}")
if __name__ == "__main__":
    pyproject_file_path = "samples/python/pyproject.toml"
    install_dependencies(pyproject_file_path)