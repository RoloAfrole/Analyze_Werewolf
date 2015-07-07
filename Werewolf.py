RoleTuple = ("Human", "Werewolf", "Prophet", "Knight", "Psychic", "Hunter", "Sharer", "Traitor", "Vampire")


class Human(object):
    """docstring for Human"""
    def __init__(self, ChID, Name, Role="Human", Life=True):
        self.ChID = ChID
        self.Name = Name
        self.Role = Role
        self.Life = Life
        self.CORole = "Human"
        self.SuspectID = None
        self.VoteList = []

    def SetName(self, Name):
        self.Name = Name
        return self.Name

    def GetName(self):
        return self.Name

    def SetRole(self, Role):
        self.Role = Role
        return self.Role

    def GetRole(self):
        return self.Role

    def SetChID(self, ChID):
        self.ChID = ChID
        return self.ChID

    def GetChID(self):
        return self.ChID

    def SetLife(self, Life):
        self.Life = Life
        return self.Life

    def GetLife(self):
        return self.Life

    def VotePhase(self, choice):
        self.VoteList.append(choice)
        return choice

    def GetVoteList(self):
        return self.VoteList

    def ComingOut(self, Role):
        self.CORole = Role
        return self.CORole

    def GetCORole(self):
        return self.CORole

    def Suspect(self, choice):
        self.SuspectID = choice
        return self.SuspectID

    def GetSuspect(self):
        return self.SuspectID

    def NightPhase(self, choice):
        pass

class Werewolf(Human):
    """docstring for Werewolf"""
    def __init__(self, ChID, Name, Role="Werewolf", Life=True):
        super(Werewolf, self).__init__(ChID, Name, Role, Life=True)

    def NightPhase(self):
        pass


class Prophet(Human):
    """docstring for Prophet"""
    def __init__(self, ChID, Name, Role="Prophet", Life=True):
        super(Prophet, self).__init__(ChID, Name, Role, Life=True)

    def NightPhase(self):
        pass


class Knight(Human):
    """docstring for Knight"""
    def __init__(self, ChID, Name, Role="Knight", Life=True):
        super(Knight, self).__init__(ChID, Name, Role, Life=True)

    def NightPhase(self):
        pass


class Psychic(Human):
    """docstring for Psychic"""
    def __init__(self, ChID, Name, Role="Psychic", Life=True):
        super(Psychic, self).__init__(ChID, Name, Role, Life=True)

    def NightPhase(self):
        pass


class Hunter(Human):
    """docstring for Hunter"""
    def __init__(self, ChID, Name, Role="Hunter", Life=True):
        super(Hunter, self).__init__(ChID, Name, Role, Life=True)

    def NightPhase(self):
        pass


class Sharer(Human):
    """docstring for Sharer"""
    def __init__(self, ChID, Name, Role="Sharer", Life=True):
        super(Sharer, self).__init__(ChID, Name, Role, Life=True)

    def NightPhase(self):
        pass


class Traitor(Human):
    """docstring for Traitor"""
    def __init__(self, ChID, Name, Role="Traitor", Life=True):
        super(Traitor, self).__init__(ChID, Name, Role, Life=True)

    def NightPhase(self):
        pass


class Vampire(Human):
    """docstring for Vampire"""
    def __init__(self, ChID, Name, Role="Vampire", Life=True):
        super(Vampire, self).__init__(ChID, Name, Role, Life=True)

    def NightPhase(self):
        pass


RoleClassDict = {"Human": Human, "Werewolf": Werewolf, "Prophet": Prophet, "Knight": Knight, "Psychic": Psychic, "Hunter": Hunter, "Sharer": Sharer, "Traitor": Traitor, "Vampire": Vampire}


class MainFrame(object):
    """docstring for MainFrame"""
    def __init__(self, MemberSettingDict):
        self.MemberSettingDict = MemberSettingDict
        self.CharaList = []
        self.PhaseList = []

    def GeneChara(self):
        count = 0
        for role in RoleTuple:
            if self.MemberSettingDict[role] > 0:
                for x in range(self.MemberSettingDict[role]):
                    self.CharaList.append(RoleClassDict[role](count, "{0}{1}".format(role, x)))
                    count += 1

    def NightPhase(self):
        pass

    def NoonPhase(self):
        pass


if __name__ == '__main__':
    MemberNum = [5, 2, 1, 1, 0, 0, 0, 0, 0]
    MemberSettingDict = {k: v for k, v in zip(RoleTuple, MemberNum)}
    print(MemberSettingDict)
    print(MainFrame)
    b = RoleClassDict["Human"](1, "name")
    print(b.GetRole())
    print(range(MemberSettingDict["Human"]))
    a = MainFrame(MemberSettingDict)
    a.GeneChara()
    print(a.CharaList)
    for x in a.CharaList:
        print("{0}, {1}, {2}".format(x.GetRole(), x.GetName(), x.GetChID()))
