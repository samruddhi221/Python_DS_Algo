# type1: worker -> pay, job_title  ($10000, "SWE"), ($12000, "TL")
# type2: team_member -> name, id
# team is a list of all team members, team members consist of 1 team_lead and 5 SWE

class Worker:
    def __init__(self, pay: int, job_title: str):
        self.__pay = pay
        self.__job_title = job_title

    def get_pay(self):
        return self.__pay

    def get_title(self):
        return self.__job_title


class TeamMember:
    def __init__(self, name: str, id: int):
        self.__name = name
        self.__id = id

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id


class TeamLead(Worker, TeamMember):
    def __init__(self, name: str, id: int, job_title: str, pay: int):
        Worker.__init__(self, pay, job_title)
        TeamMember.__init__(self, name, id)


class SWE(Worker, TeamMember):
    def __init__(self, name: str, id: int, job_title: str, pay: int):
        Worker.__init__(self, pay, job_title)
        TeamMember.__init__(self, name, id)

def average_team_pay(workers: list) -> None:
    """
    HR takes team information and calculates the average pay of the team.
    :return: None
    """
    average_pay = 0.
    for worker in workers:
        average_pay += worker.get_pay()
    average_pay /= len(workers)
    print("Average pay of the team is: ", average_pay)


def team_info(team_members: list):
    """
    Manager wants to list down the team info: name and id
    :return:
    """
    for member in team_members:
        print(f'member name: {member.get_name()}, member id: {member.get_id()}')


class Team(Worker, TeamMember):
    def __init__(self, team_size):


if __name__ == '__main__':
    tl = TeamLead("XYZ", 0, "TL", 12000)
    swe1 = SWE("A", 1, "SWE", 10000)
    swe2 = SWE("B", 2, "SWE", 10000)
    swe3 = SWE("C", 3, "SWE", 10000)
    swe4 = SWE("D", 4, "SWE", 10000)
    swe5 = SWE("E", 5, "SWE", 10000)
    team = [tl, swe1, swe2, swe3, swe4, swe5]
    team_info(team)
    average_team_pay(team)

