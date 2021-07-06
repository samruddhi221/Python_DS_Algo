"""
Problem Statement:
1. Find the right locker for the package according to its size.
lockerSize >= packageSize
2. only 1 package in a locker

Functional Requirements:
1. User:
- Open the locker with the code
- pick the package

2. Delivery Guy:
- place the package to the locker

3. Locker System:
- find the available lockers
- generate code
- send the generated code to the user
- keep track of empty and full lockers

ASSUME: there is always an available locker

flow of events:
1. Delivery Person reaches the hub with n
"""
from enum import Enum
import numpy as np
import uuid

class Size(Enum):
    small = 1
    medium = 2
    large = 3

class PackageStatus(Enum):
    shipped = 1
    in_transit = 2
    delivered = 3

class Locker:
    """
    1. add package
    2. remove package
    """
    def __init__(self, size: Size, id: int):
        self.id = id
        self.size = size
        self.package = None

    def addPackage(self, package: Package)->None:
        self.package = package

    def removePackage(self):
        self.package = None

class Code:
    def __init__(self):
        self.uuid = uuid.uuid1()

    def __eq__(self, other):
        return self.uuid == other.uuid

class User:
    """
    1. generate code
    2. notify user
    """
    def __init__(self, name, address):
        self.user_name = name
        self.address = address
        self.code = None

    def generate_code(self):
        self.code = Code()

    def notify(self):
        # send code to user
        print("code sent to the recepient.")

    def authenticate_user(self, code):
        return self.code == code

class Package:
    """

    """
    def __init__(self, size: Size, id: int, user: User, status: PackageStatus):
        self.id = id
        self.size = size
        self.state = status
        self.recipient = user

    def delivered(self, package):
        self.state = PackageStatus.delivered

class LockerManager:
    """
    1. receive the package
    2. check if the locker is available
    3. accept/reject package
    4. assign and update locker state
    5. authenticate user
    6. deliver package and update the locker state
    """
    def __init__(self, id, locationId):
        self.id = id
        self.locationId = locationId
        self.n_small = 10 # 10
        self.n_medium = 10 # 10
        self.n_large = 10 # 10
        self.smallEmpty = [Locker(Size.small, i) for i in range(self.n_small)]
        self.smallFull = []
        self.mediumEmpty = [Locker(Size.medium, i+self.n_small) for i in range(self.n_medium)]
        self.mediumFull = []
        self.largeEmpty = [Locker(Size.large, i+self.n_small+self.n_medium) for i in range(self.n_large)]
        self.largeFull = []
        self.lockerUserMap = {}
        self.assignLockerMap = {}

    def receive_package(self, pacuserkage: Package) -> bool:
        """
        :param package: package object
        :return: True if package is accepted(assigned locker) in the locker
        """
        locker = self.__find_locker(package)
        if not locker:
            return False # None of the lockers are free, reject the package
        else:
            # assign package to locker
            locker.addPackage(package)
            # # assign code to the locker
            # self.assignLockerMap[code] = locker
            # notify user
            locker.package.recipient.notify()
            # move package to occupied list
            self.__update_locker_state_to_occupied(locker)
            return True

    def deliver_package(self, code:Code) -> bool:
        """
        1. Verify the code
        2. Open the locker and deliver package
        3. update the locker state
        :param code:
        :return: True if package was successfully delivered else false
        """
        locker = self.__get_locker_from_code(code)
        if not locker:
            return False
        locker.package.delivered()
        self.__update_locker_state_to_empty(locker)
        return True


    def __find_locker(self, package: Package):
        if len(self.smallEmpty)+len(self.mediumEmpty)+len(self.largeEmpty) == 0:
            return None
        else:
            package_size = package.size

            if package_size == Size.large:
                return self.__get_large_locker()
            elif package_size == Size.medium:
                locker = self.__get_medium_locker()
                if not locker:
                    locker = self.__get_large_locker()
                return locker
            elif package_size == Size.small:
                locker = self.__get_small_locker()
                if not locker:
                    locker = self.__get_medium_locker()
                if not locker:
                    locker = self.__get_large_locker()
                return locker

    def __get_small_locker(self):
        if len(self.smallEmpty) > 0:
            locker = self.smallEmpty.pop()
            return locker
        else:
            return None

    def __get_medium_locker(self):
        if len(self.mediumEmpty) > 0:
            locker = self.mediumEmpty.pop()
            return locker
        else:
            return None

    def __get_large_locker(self):
        if len(self.largeEmpty) > 0:
            locker = self.largeEmpty.pop()
            return locker
        else:
            return None

    def __update_locker_state_to_occupied(self, locker: Locker):
        if locker.size == Size.small:
            self.smallFull.append(locker)
        elif locker.size == Size.medium:
            self.mediumFull.append(locker)
        else:
            self.largeFull.append(locker)

    def __get_locker_from_code(self, code: Code):
        for locker in self.smallFull:
            if locker.package.recipient.authenticate_user(code):
                return locker
        for locker in self.mediumFull:
            if locker.package.recipient.authenticate_user(code):
                return locker
        for locker in self.largeFull:
            if locker.package.recipient.authenticate_user(code):
                return locker
        return None

    def __update_locker_state_to_empty(self, locker: Locker):
        if locker.size == Size.small:
            self.smallFull.remove(locker)
            self.smallEmpty.append(locker)
        elif locker.size == Size.medium:
            self.mediumFull.remove(locker)
            self.mediumEmpty.append(locker)
        else:
            self.largeFull.remove(locker)
            self.largeEmpty.append(locker)




