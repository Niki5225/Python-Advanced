from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 30)

    def details(self):
        result = f"{self.name} Main Service:\n"
        if self.robots:
            result += f"Robots: {' '.join([robot.name for robot in self.robots])}"
        else:
            result += "Robots: none"
        return result

