import subprocess

class RunApplication:
    def run(self):
        subprocess.run(["python", "API/controller/RecommendationsController.py"])

if __name__ == "__main__":
    RunApplication().run()