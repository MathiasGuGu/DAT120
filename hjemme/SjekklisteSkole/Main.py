"""

En app som noterer hvilke timer du har vært i og hvilke timer du ikke har vært i.
gir deg riktig video ID til timene du ikke har vært i og gir deg en slags belønning for hver time du deltar i.
forløpig en terminal app, men kan konverteres til PyGUI og kanskje en mobil app med java, swift etc...


Finn ut om mediaSite har en måte å vise alle video IDene. Hvis ikke må du scrape den på en måte. 
Ha sjekkbokser for hver uke. Og siden du vet det er 3 matte timer og en fysikk time hver uke kan du skrive det opp. 


"""


class Timeedit:

    URL = "https://cloud.timeedit.net/uis/web/student_u/ri103v566562ZYQY75Q037gXZ700559574X515Yy668YQQ.html"

    def __init__(self, user_id: int, user_password: str) -> None:
        self.user_id = user_id
        self.user_password = user_password
    
    def get_weekly_plan(self, user_id: int, user_password: str, week_nr: int):
        pass

    def get_available_classes():
        pass

    def get_attended_classes():
        pass

    def get_unattended_classes():
        pass


class Mediasite:
    
    dat120 = "https://mediasite.uis.no/Mediasite/Channel/da202f37dd904302b0cb69665b897b215f"
    mat100 = "https://mediasite.uis.no/Mediasite/Channel/mat100-h2021"
    red102 = "https://mediasite.uis.no/Mediasite/Channel/red102-h2021"

    def __init__(self, user_id: int, user_password: str) -> None:
        self.user_id = user_id
        self.user_password = user_password

    def get_unattended_stream():
        pass

    def get_attended_stream():
        pass

class Main:

    classes_number = [3, 1]
    classes_names = ["Matematikk", "Fysikk"]


    def __init__(self, classes_number: int, classes_names: list[str]) -> None:
        self.classes_number = classes_number
        self.classes_names = classes_names
    
    def Calculate_attendence(self, classes_number, classes_names):
        pass




if __name__ == "__main__":
    Main.Calculate_attendence()