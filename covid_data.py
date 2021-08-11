class covid_data:

    def __init__(self,casetype=None,cases=None,difference=None,date=None,country=None,state=None,fips=None):
        self.Case_Type = casetype
        self.Cases = cases
        self.Difference = difference
        self.Date = date
        self.Country_Region = country
        self.Province_State = state
        self.FIPS = fips
        self.key = self._creatkey()
        self.data = self._returndata()

    def _creatkey(self):

        if (self.Case_Type == "Deaths"):
            date_key = self.Date.split('/')
            fips_key_clean = self.FIPS
            combinedkey = 'D' + date_key[0] + date_key[1] + date_key[2] + fips_key_clean
            return combinedkey
        else:
            date_key = self.Date.split('/')
            fips_key_clean = self.FIPS
            combinedkey = 'C' + date_key[0] + date_key[1] + date_key[2] + fips_key_clean
            return combinedkey

    def _returndata(self):
        if (self.Case_Type == "Deaths"):
            data = self.key + "|" + self.Case_Type + "|" + self.Cases + "|" + self.Difference + "|" + self.Date + "|" + self.Country_Region + "|" + self.Province_State + "|" + self.FIPS+"\n"
            return data
        else:
            data = self.key + "|" + self.Case_Type + "|" + self.Cases + "|" + self.Difference + "|" + self.Date + "|" + self.Country_Region + "|" + self.Province_State + "|" + self.FIPS+"\n"
            return data


    def get_key(self):
        return self.key

    def get_data(self):
        return self.data
