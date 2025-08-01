import pkg_resources
import requests
from packaging import version
import argparse

def get_latest_version(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["info"]["version"]
    except Exception as e:
        return None

def check_installed_packages(outdated_only=False, save_file=None, exclude_list=None):
    exclude_list = exclude_list or []
    results = []

    for dist in pkg_resources.working_set:
        name = dist.project_name
        if name in exclude_list:
            continue
        current = dist.version
        latest = get_latest_version(name)

        if latest:
            current_v = version.parse(current)
            latest_v = version.parse(latest)

            if current_v < latest_v:
                line = f"🔺 {name}: {current} → {latest}"
                if not outdated_only:
                    print(line)
                results.append(line)
            else:
                line = f"✅ {name} is up to date."
                if not outdated_only:
                    print(line)
                results.append(line)
        else:
            line = f"❌ {name}: Not found on PyPI."
            if not outdated_only:
                print(line)
            results.append(line)

    if save_file:
        with open(save_file, "w") as f:
            for line in results:
                f.write(line + "\n")
        print(f"Results saved to {save_file}")

def main():
    parser = argparse.ArgumentParser(description="Check Python packages for updates.")
    parser.add_argument("--outdated-only", action="store_true", help="Show only outdated packages.")
    parser.add_argument("--save", type=str, help="Save output to a file.")
    parser.add_argument("--exclude", nargs="*", default=[], help="List of packages to exclude.")

    args = parser.parse_args()
    check_installed_packages(args.outdated_only, args.save, args.exclude)

if __name__ == "__main__":
    main()
import pkg_resources
import requests
from packaging import version

def get_latest_version(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["info"]["version"]
    return None

def check_installed_packages():
    for dist in pkg_resources.working_set:
        name = dist.project_name
        current = dist.version
        latest = get_latest_version(name)

        if latest:
            current_v = version.parse(current)
            latest_v = version.parse(latest)

            if current_v < latest_v:
                print(f"🔺 {name}: {current} → {latest}")
            else:
                print(f"✅ {name} is up to date.")
        else:
            print(f"❌ {name}: Not found on PyPI.")

if __name__ == "__main__":
    check_installed_packages()

