from importlib.metadata import version

packages = [
    "langchain-cohere",
    "cohere",
    "langchain-core",
    "langchain-tavily",
    "langgraph",
]

for package in packages:
    try:
        print(f"{package}: {version(package)}")
    except Exception as exc:
        print(f"{package}: {exc}")