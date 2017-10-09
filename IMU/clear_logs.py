

class Clear_logs():

    def __init__(self, rawdata=False, pointdata=False, additionalfile=''):

        if rawdata == True:
            try:
                open("logs/rawdata.csv", "w").close()
                print("File rawdata.csv Cleared.")
            except IOError:
                print("An Error Occurred Trying to Clear the File rawdata.csv")

        if pointdata == True:
            try:
                open("logs/pointdata.csv", "w").close()
                print("File pointdata.csv Cleared.")
            except IOError:
                print("An Error Occurred Trying to Clear the File pointdata.csv")

        if additionalfile != '':
            try:
                open("logs/" + additionalfile, "w").close()
            except IOError:
                print("An Error Occurred Trying to Clear the File " + additionalfile)

