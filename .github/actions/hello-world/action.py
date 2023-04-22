import os

def run():
    name = os.getenv("INPUT_USER-NAME")
    print(f'::set-output name=greeting::Hello {name}!')

if __name__ == "__main__":
    run()