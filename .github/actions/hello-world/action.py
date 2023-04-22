import os

def run():
    name = os.getenv("INPUT_USER-NAME")
    greeting = f"Hello {name}!"
    add_variable('greeting', greeting)

def add_variable(variable, value):
    env_file_name = os.getenv('GITHUB_OUTPUT')

    with open(env_file_name, "a") as github_env_file:
        github_env_file.write(f"{variable}={value}")

if __name__ == "__main__":
    run()