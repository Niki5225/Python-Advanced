from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = ["MainService", "SecondaryService"]
    VALID_ROBOTS = ["MaleRobot", "FemaleRobot"]

    def __init__(self):
        self.robots = []
        self.services = []

    def __find_robot(self, robot_name):
        for robot in self.robots:
            if robot.name == robot_name:
                return robot

    def __find_service(self, service_name):
        for service in self.services:
            if service.name == service_name:
                return service

    def __find_robot_in_service(self, robot_name, service):
        for robot in service.robots:
            if robot.name == robot_name:
                return robot
        else:
            raise Exception("No such robot in this service!")

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICES:
            raise Exception("Invalid service type!")

        if service_type == "MainService":
            self.services.append(MainService(name))
        elif service_type == "SecondaryService":
            self.services.append(SecondaryService(name))

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOTS:
            raise Exception("Invalid robot type!")

        if robot_type == "MaleRobot":
            self.robots.append(MaleRobot(name, kind, price))
        elif robot_type == "FemaleRobot":
            self.robots.append(FemaleRobot(name, kind, price))

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.__find_robot(robot_name)
        service = self.__find_service(service_name)
        if robot.__class__.__name__ == "MaleRobot":
            if service.__class__.__name__ == "SecondaryService":
                return "Unsuitable service."
        elif robot.__class__.__name__ == "FemaleRobot":
            if service.__class__.__name__ == "MainService":
                return "Unsuitable service."

        if len(service.robots) == service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.__find_service(service_name)
        robot = self.__find_robot_in_service(robot_name, service)

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.__find_service(service_name)

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self.__find_service(service_name)
        total_price = 0
        for robot in service.robots:
            total_price += robot.price
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = []
        for service in self.services:
            result.append(service.details())
        return "\n".join(result)
