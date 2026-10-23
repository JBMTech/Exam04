

def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    if not packages:
        return []

    dependencies_count = {}
    dependents = {}

    for package in packages:
        dependencies_count[package] = 0
        dependents[package] = []

    for package in packages:
        for dependency in packages[package]:
            if dependency in packages:
                dependencies_count[package] += 1
                dependents[dependency].append(package)

    queue = []
    names = list(packages)
    names.reverse()

    for package in names:
        if dependencies_count[package] == 0:
            queue.append(package)

    result = []

    while queue:
        package = queue.pop(0)
        result.append(package)

        for dependent in dependents[package]:
            dependencies_count[dependent] -= 1

            if dependencies_count[dependent] == 0:
                queue.append(dependent)

    if len(result) != len(packages):
        return []

    return result
