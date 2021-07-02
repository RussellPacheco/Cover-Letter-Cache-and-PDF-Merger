import os
import json


class CoverLetterMaintainer:
    def __init__(self):
        self.root = os.path.dirname(os.path.abspath(__file__))
        self.data_file_path = f"{self.root}\\data.json"
        self.resume_dir = "C:\\Users\\russ1\\Documents\\Important Documents\\Resume\\Software Engineer\\"
        self.cover_letter_path = self.resume_dir+"Cover Letters\\"
        self.resume_path = self.resume_dir+"Russell_Pacheco_resume.pdf"

    def start(self):
        UPDATEQUERIES = "update"
        SEARCH = "search"
        GETQUERIES = "get"
        SCAN = "scan"
        OPEN = "open"
        QUIT = "quit"

        COMMANDS = [SEARCH, GETQUERIES, SCAN, UPDATEQUERIES, OPEN, QUIT]
        print("Cover Letter Helper ©")
        print("Created By: BobSanders")

        self.update_check()

        while True:
            print("")
            print(f"Please choose: {COMMANDS}")
            COMMAND = input(">>>")

            COMMAND = COMMAND.split(" ")

            if COMMAND[0] == SEARCH:
                if not len(COMMAND) <= 1:
                    COMMAND.remove("search")
                    self.search(COMMAND)
                else:
                    print("search <search queries>")

            if COMMAND[0] == GETQUERIES:
                if not len(COMMAND) <= 1:
                    self.getqueries(COMMAND[1])
                else:
                    print("get <'all'> or <filename>")

            if COMMAND[0] == SCAN:
                print("Scanning for new files. If no files found, will do nothing.")
                self.update_check()

            if COMMAND[0] == UPDATEQUERIES:
                if not len(COMMAND) <= 1:
                    self.update_queries(COMMAND[1])
                else:
                    print("update <filename>")

            if COMMAND[0] == OPEN:
                if not len(COMMAND) <= 1:
                    self.open(COMMAND[1])

                else:
                    print("open <filename>")

            if COMMAND[0] == QUIT:
                break

    def update_check(self):

        if not os.path.exists(self.data_file_path):
            json_file = open("data.json", "w")
            json.dump({}, json_file)
            json_file.close()

        json_file = open(self.data_file_path)
        data = json.load(json_file)
        json_file.close()

        previous_data_filenames = [key for key in data.keys()]

        files = os.listdir(self.cover_letter_path)

        new_files = []
        for file in files:
            if file not in previous_data_filenames:
                new_files.append(file)

        if len(new_files) != 0:
            print(f"There are {len(new_files)} uncached file(s). Would you like to update?")
            command = input(">>>")

            if command == "yes":
                for filename in new_files:
                    self.add_search_queries(filename)
                    self.update_cache()

    def update_cache(self):

        json_file = open("data.json")
        data = json.load(json_file)
        json_file.close()
        data_keys = data.keys()

        files = os.listdir(self.cover_letter_path)

        print("Updating the File Cache")

        new_files = []

        for file in files:
            if file not in data_keys:
                new_files.append(file)

        for filename in new_files:
            data[filename]["queries"] = []

        with open(self.data_file_path, "w") as json_file:
            json.dump(data, json_file)
            json_file.close()

    def open(self, filename):
        if filename == "resume" or filename == "cv":
            print("Opening your resume...")
            os.startfile(self.resume_path)
            return

        json_file = open(self.data_file_path)
        data = json.load(json_file)
        json_file.close()

        for key in data.keys():
            if filename in key:
                print(f"Opening {key}...")
                os.startfile(self.cover_letter_path+key)

    def search(self, query_list):
        json_file = open(self.data_file_path)
        data = json.load(json_file)
        json_file.close()

        files = data.keys()

        matches = []

        for file in files:
            match = True
            for query in query_list:
                if query not in data[file]["queries"]:
                    match = False

            if match:
                matches.append(file)


        print(f"Your matches are {matches}")

    def add_search_queries(self, filename):
        json_file = open(self.data_file_path)
        data = json.load(json_file)
        json_file.close()

        print(f"Please type search queries for {filename}.")
        queries = input(">>>")
        query_list = queries.split(" ")

        data[filename] = {"queries": query_list}

        with open(self.data_file_path, "w") as json_file:
            json.dump(data, json_file)
            json_file.close()

    def getqueries(self, arg):
        json_file = open(self.data_file_path)
        data = json.load(json_file)
        json_file.close()

        available_files = data.keys()

        print()

        if arg != "all":
            for key in data.keys():
                if arg in key.lower():
                    print(f"The queries for {key} are {data[key]['queries']}")

        if arg == "all":
            print(f"""
========================================================================================================================

                                                 Available Files

========================================================================================================================
""")
            pointer = 1

            list1 = []
            list2 = []
            list3 = []
            for key in available_files:
                if pointer == 1:
                    list1.append(key)
                    pointer = 2
                elif pointer == 2:
                    list2.append(key)
                    pointer = 3
                elif pointer == 3:
                    list3.append(key)
                    pointer = 1

            for i in range(len(list1)):
                if len(list2) == 0 or len(list2) < i + 1:
                    print(f"{list1[i]}")
                elif len(list3) == 0:
                    print(f"{list1[i]}      {list2[i]}")
                else:

                    line1_spacing = " " * 17
                    line2_spacing = " " * 17

                    if len(list1[i]) > 27:
                        diff = len(list1[i]) - 27
                        line1_spacing = " " * (17 - diff)

                    if len(list2[i]) > 27:
                        diff = len(list2[i]) - 27
                        line2_spacing = " " * (17 - diff)

                    print(f"{list1[i]}{line1_spacing}{list2[i] or ''}{line2_spacing}{list3[i] or ''}")


    def update_queries(self, filename):
        json_file = open(self.data_file_path)
        data = json.load(json_file)
        json_file.close()

        toggle = False

        for key in data.keys():
            if filename in key.lower():

                toggle = True

                while True:

                    print(f"Current Search Queries: {data[key]['queries']}")
                    print("")
                    print("What would you like to do?")
                    print(
                        "COMMANDS: add <search queries>, delete <searchqueries>, edit <query_to_be_edited> <new_query>")

                    COMMAND = input(">>>")
                    COMMAND = COMMAND.split(" ")

                    if COMMAND[0] == "add":
                        COMMAND.remove("add")
                        for query in COMMAND:
                            data[key]['queries'].append(query)

                    if COMMAND[0] == "delete" or COMMAND[0] == "remove":
                        if COMMAND[0] == "delete":
                            COMMAND.remove("delete")
                        if COMMAND[0] == "remove":
                            COMMAND.remove("remove")

                        for query in COMMAND:
                            if query in data[key]["queries"]:
                                data[key]['queries'].remove(query)
                            else:
                                print("")
                                print(f"'{query}' not in {key} search queries")
                                print("")

                    if COMMAND[0] == "edit":
                        data[key]["queries"] = [COMMAND[2] if i == COMMAND[1] else i for i in data[key]["queries"]]

                    if COMMAND[0] == "quit" or COMMAND[0] == "exit":
                        with open(self.data_file_path, "w") as json_file:
                            json.dump(data, json_file)
                        break

        if not toggle:
            print("File not found.")

