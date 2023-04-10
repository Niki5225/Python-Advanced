from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 15)

    def details(self):
        result = f"{self.name} Secondary Service:\n"
        if self.robots:
            result += f"Robots: {' '.join([robot.name for robot in self.robots])}"
        else:
            result += "Robots: none"
        return result
